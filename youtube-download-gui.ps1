param([switch]$NoGui)

$ErrorActionPreference = "Stop"

$script:RepoRoot = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($script:RepoRoot)) {
    $script:RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
}

$script:DefaultStatePath = Join-Path $script:RepoRoot "youtube-tracker-state.json"
$script:DefaultOutputPath = Join-Path ([Environment]::GetFolderPath("MyVideos")) "MrWaterDrop"
$script:YtDlpPath = Join-Path $script:RepoRoot "tools\yt-dlp.exe"
$script:DownloadLogPath = Join-Path $script:RepoRoot "youtube-download-gui.log"

function Write-DownloadLog {
    param([string]$Message)

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $script:DownloadLogPath -Encoding UTF8 -Value "[$timestamp] $Message"
}

function Read-YouTubeDownloadState {
    param([string]$Path = $script:DefaultStatePath)

    if (-not (Test-Path -LiteralPath $Path)) {
        return @()
    }

    $json = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ([string]::IsNullOrWhiteSpace($json)) {
        return @()
    }

    return @($json | ConvertFrom-Json)
}

function Get-YtDlpFormat {
    param(
        [string]$Quality,
        [switch]$AudioOnly
    )

    if ($AudioOnly) {
        return "bestaudio/best"
    }

    switch ($Quality) {
        "best" { return "bestvideo+bestaudio/best" }
        "worst" { return "worstvideo+worstaudio/worst" }
        default {
            $height = $Quality -replace "p", ""
            return "bestvideo[height<=$height]+bestaudio/best[height<=$height]"
        }
    }
}

function Get-SafeFileNameTemplate {
    param([string]$OutputPath)

    $cleanPath = $OutputPath.TrimEnd("\", "/")
    return (Join-Path $cleanPath "%(upload_date)s - %(title).150B [%(id)s].%(ext)s")
}

function ConvertTo-ProcessArgument {
    param([string]$Value)

    if ($Value -match '^[A-Za-z0-9_\-./:=?&%+,\[\]<>]+$') {
        return $Value
    }

    return '"' + ($Value -replace '\\', '\\' -replace '"', '\"') + '"'
}

function Install-YtDlp {
    param([string]$Destination = $script:YtDlpPath)

    $folder = Split-Path -Parent $Destination
    if (-not (Test-Path -LiteralPath $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
    }

    $url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
    Invoke-WebRequest -Uri $url -OutFile $Destination -UseBasicParsing

    if (-not (Test-Path -LiteralPath $Destination)) {
        throw "yt-dlp.exe 下載失敗。"
    }

    return $Destination
}

function Resolve-YtDlpPath {
    if (Test-Path -LiteralPath $script:YtDlpPath) {
        return $script:YtDlpPath
    }

    $fromPath = Get-Command yt-dlp.exe -ErrorAction SilentlyContinue
    if ($null -ne $fromPath) {
        return $fromPath.Source
    }

    return $null
}

function Invoke-YouTubeDownload {
    param(
        [Parameter(Mandatory = $true)][string]$Url,
        [Parameter(Mandatory = $true)][string]$OutputPath,
        [string]$Quality = "720p",
        [string]$Format = "mp4",
        [switch]$AudioOnly
    )

    if ([string]::IsNullOrWhiteSpace($Url)) {
        throw "請選擇影片。"
    }

    if (-not (Test-Path -LiteralPath $OutputPath)) {
        New-Item -ItemType Directory -Path $OutputPath | Out-Null
    }

    $ytDlp = Resolve-YtDlpPath
    if ($null -eq $ytDlp) {
        throw "找不到 yt-dlp.exe。請先按「安裝/更新 yt-dlp」。"
    }

    $args = New-Object System.Collections.Generic.List[string]
    $args.Add("--no-playlist")
    $args.Add("--windows-filenames")
    $args.Add("--newline")
    $args.Add("-o")
    $args.Add((Get-SafeFileNameTemplate -OutputPath $OutputPath))

    if ($AudioOnly) {
        $args.Add("-x")
        $args.Add("--audio-format")
        $args.Add("mp3")
        $args.Add("-f")
        $args.Add((Get-YtDlpFormat -Quality $Quality -AudioOnly))
    }
    else {
        $args.Add("-f")
        $args.Add((Get-YtDlpFormat -Quality $Quality))
        $args.Add("--merge-output-format")
        $args.Add($Format)
    }

    $args.Add($Url)

    Write-DownloadLog ("Running: " + $ytDlp + " " + ($args -join " "))
    $stdoutPath = Join-Path ([System.IO.Path]::GetTempPath()) "codex-ytdlp-out-$([Guid]::NewGuid().ToString("N")).txt"
    $stderrPath = Join-Path ([System.IO.Path]::GetTempPath()) "codex-ytdlp-err-$([Guid]::NewGuid().ToString("N")).txt"

    try {
        $argumentLine = ($args | ForEach-Object { ConvertTo-ProcessArgument $_ }) -join " "
        $process = Start-Process `
            -FilePath $ytDlp `
            -ArgumentList $argumentLine `
            -NoNewWindow `
            -Wait `
            -PassThru `
            -RedirectStandardOutput $stdoutPath `
            -RedirectStandardError $stderrPath
        $exitCode = $process.ExitCode

        $stdout = ""
        $stderr = ""
        if (Test-Path -LiteralPath $stdoutPath) {
            $stdout = Get-Content -LiteralPath $stdoutPath -Raw -ErrorAction SilentlyContinue
        }
        if (Test-Path -LiteralPath $stderrPath) {
            $stderr = Get-Content -LiteralPath $stderrPath -Raw -ErrorAction SilentlyContinue
        }

        Write-DownloadLog ("yt-dlp exit code: $exitCode")
        if (-not [string]::IsNullOrWhiteSpace($stdout)) {
            Write-DownloadLog $stdout.Trim()
        }
        if (-not [string]::IsNullOrWhiteSpace($stderr)) {
            Write-DownloadLog $stderr.Trim()
        }
    }
    finally {
        Remove-Item -LiteralPath $stdoutPath, $stderrPath -Force -ErrorAction SilentlyContinue
    }

    if ($exitCode -ne 0) {
        throw "下載失敗，exit code $exitCode。`n$stderr"
    }

    return ($stdout + "`n" + $stderr)
}

if (-not $NoGui) {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing

    function Set-Status {
        param([string]$Text, [System.Drawing.Color]$Color)
        $statusLabel.Text = $Text
        $statusLabel.ForeColor = $Color
        [System.Windows.Forms.Application]::DoEvents()
    }

    $font = New-Object System.Drawing.Font("Microsoft JhengHei UI", 10)
    $titleFont = New-Object System.Drawing.Font("Microsoft JhengHei UI", 14, [System.Drawing.FontStyle]::Bold)

    $form = New-Object System.Windows.Forms.Form
    $form.Text = "YouTube 影片下載器"
    $form.Size = New-Object System.Drawing.Size(860, 650)
    $form.StartPosition = "CenterScreen"
    $form.Font = $font

    $title = New-Object System.Windows.Forms.Label
    $title.Text = "清流君影片下載器"
    $title.Font = $titleFont
    $title.Location = New-Object System.Drawing.Point(24, 18)
    $title.Size = New-Object System.Drawing.Size(780, 32)
    $form.Controls.Add($title)

    $note = New-Object System.Windows.Forms.Label
    $note.Text = "請只下載你有權保存或符合 YouTube 條款的影片。清單來自 youtube-tracker-state.json。"
    $note.Location = New-Object System.Drawing.Point(28, 54)
    $note.Size = New-Object System.Drawing.Size(780, 26)
    $note.ForeColor = [System.Drawing.Color]::FromArgb(80, 80, 80)
    $form.Controls.Add($note)

    $listBox = New-Object System.Windows.Forms.ListBox
    $listBox.Location = New-Object System.Drawing.Point(30, 92)
    $listBox.Size = New-Object System.Drawing.Size(790, 260)
    $listBox.DisplayMember = "Display"
    $form.Controls.Add($listBox)

    $refreshButton = New-Object System.Windows.Forms.Button
    $refreshButton.Text = "重新讀取清單"
    $refreshButton.Location = New-Object System.Drawing.Point(30, 365)
    $refreshButton.Size = New-Object System.Drawing.Size(130, 34)
    $form.Controls.Add($refreshButton)

    $installButton = New-Object System.Windows.Forms.Button
    $installButton.Text = "安裝/更新 yt-dlp"
    $installButton.Location = New-Object System.Drawing.Point(170, 365)
    $installButton.Size = New-Object System.Drawing.Size(150, 34)
    $form.Controls.Add($installButton)

    $qualityLabel = New-Object System.Windows.Forms.Label
    $qualityLabel.Text = "畫質"
    $qualityLabel.Location = New-Object System.Drawing.Point(30, 418)
    $qualityLabel.Size = New-Object System.Drawing.Size(60, 28)
    $form.Controls.Add($qualityLabel)

    $qualityBox = New-Object System.Windows.Forms.ComboBox
    $qualityBox.Location = New-Object System.Drawing.Point(90, 416)
    $qualityBox.Size = New-Object System.Drawing.Size(110, 28)
    $qualityBox.DropDownStyle = "DropDownList"
    [void]$qualityBox.Items.AddRange(@("best", "1080p", "720p", "480p", "360p", "worst"))
    $qualityBox.SelectedItem = "720p"
    $form.Controls.Add($qualityBox)

    $formatLabel = New-Object System.Windows.Forms.Label
    $formatLabel.Text = "格式"
    $formatLabel.Location = New-Object System.Drawing.Point(220, 418)
    $formatLabel.Size = New-Object System.Drawing.Size(60, 28)
    $form.Controls.Add($formatLabel)

    $formatBox = New-Object System.Windows.Forms.ComboBox
    $formatBox.Location = New-Object System.Drawing.Point(280, 416)
    $formatBox.Size = New-Object System.Drawing.Size(100, 28)
    $formatBox.DropDownStyle = "DropDownList"
    [void]$formatBox.Items.AddRange(@("mp4", "webm", "mkv"))
    $formatBox.SelectedItem = "mp4"
    $form.Controls.Add($formatBox)

    $audioOnlyBox = New-Object System.Windows.Forms.CheckBox
    $audioOnlyBox.Text = "只下載 MP3 音訊"
    $audioOnlyBox.Location = New-Object System.Drawing.Point(405, 417)
    $audioOnlyBox.Size = New-Object System.Drawing.Size(160, 28)
    $form.Controls.Add($audioOnlyBox)

    $outputLabel = New-Object System.Windows.Forms.Label
    $outputLabel.Text = "輸出資料夾"
    $outputLabel.Location = New-Object System.Drawing.Point(30, 466)
    $outputLabel.Size = New-Object System.Drawing.Size(100, 28)
    $form.Controls.Add($outputLabel)

    $outputBox = New-Object System.Windows.Forms.TextBox
    $outputBox.Text = $script:DefaultOutputPath
    $outputBox.Location = New-Object System.Drawing.Point(130, 464)
    $outputBox.Size = New-Object System.Drawing.Size(555, 28)
    $form.Controls.Add($outputBox)

    $browseButton = New-Object System.Windows.Forms.Button
    $browseButton.Text = "選擇..."
    $browseButton.Location = New-Object System.Drawing.Point(700, 462)
    $browseButton.Size = New-Object System.Drawing.Size(120, 34)
    $form.Controls.Add($browseButton)

    $downloadButton = New-Object System.Windows.Forms.Button
    $downloadButton.Text = "下載選取影片"
    $downloadButton.Location = New-Object System.Drawing.Point(630, 515)
    $downloadButton.Size = New-Object System.Drawing.Size(190, 42)
    $downloadButton.BackColor = [System.Drawing.Color]::FromArgb(30, 115, 190)
    $downloadButton.ForeColor = [System.Drawing.Color]::White
    $downloadButton.FlatStyle = "Flat"
    $form.Controls.Add($downloadButton)

    $statusLabel = New-Object System.Windows.Forms.Label
    $statusLabel.Text = "狀態：等待操作"
    $statusLabel.Location = New-Object System.Drawing.Point(30, 575)
    $statusLabel.Size = New-Object System.Drawing.Size(790, 28)
    $statusLabel.ForeColor = [System.Drawing.Color]::FromArgb(80, 80, 80)
    $form.Controls.Add($statusLabel)

    function Load-VideoList {
        $listBox.Items.Clear()
        $videos = Read-YouTubeDownloadState
        foreach ($video in $videos) {
            $item = [pscustomobject]@{
                Display = "$($video.Published) - $($video.Title)"
                Url = $video.Url
                Title = $video.Title
            }
            [void]$listBox.Items.Add($item)
        }
        Set-Status "狀態：已載入 $($videos.Count) 支影片" ([System.Drawing.Color]::FromArgb(80, 80, 80))
    }

    $refreshButton.Add_Click({ Load-VideoList })

    $installButton.Add_Click({
        try {
            $installButton.Enabled = $false
            Set-Status "狀態：正在安裝/更新 yt-dlp.exe..." ([System.Drawing.Color]::FromArgb(80, 80, 80))
            $path = Install-YtDlp
            Set-Status "狀態：yt-dlp 已可用：$path" ([System.Drawing.Color]::FromArgb(30, 120, 60))
            [System.Windows.Forms.MessageBox]::Show("yt-dlp 已安裝/更新完成。", "完成", "OK", "Information") | Out-Null
        }
        catch {
            Write-DownloadLog $_.Exception.ToString()
            Set-Status "錯誤：$($_.Exception.Message)" ([System.Drawing.Color]::Firebrick)
            [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, "安裝失敗", "OK", "Error") | Out-Null
        }
        finally {
            $installButton.Enabled = $true
        }
    })

    $browseButton.Add_Click({
        $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
        $dialog.Description = "選擇下載輸出資料夾"
        if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
            $outputBox.Text = $dialog.SelectedPath
        }
    })

    $downloadButton.Add_Click({
        try {
            if ($null -eq $listBox.SelectedItem) {
                throw "請先選擇一支影片。"
            }

            $downloadButton.Enabled = $false
            Set-Status "狀態：正在下載，請稍候..." ([System.Drawing.Color]::FromArgb(80, 80, 80))

            Invoke-YouTubeDownload `
                -Url $listBox.SelectedItem.Url `
                -OutputPath $outputBox.Text `
                -Quality $qualityBox.SelectedItem `
                -Format $formatBox.SelectedItem `
                -AudioOnly:$audioOnlyBox.Checked | Out-Null

            Set-Status "狀態：下載完成，已存到 $($outputBox.Text)" ([System.Drawing.Color]::FromArgb(30, 120, 60))
            [System.Windows.Forms.MessageBox]::Show("下載完成。", "完成", "OK", "Information") | Out-Null
        }
        catch {
            Write-DownloadLog $_.Exception.ToString()
            Set-Status "錯誤：$($_.Exception.Message)" ([System.Drawing.Color]::Firebrick)
            [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, "下載失敗", "OK", "Error") | Out-Null
        }
        finally {
            $downloadButton.Enabled = $true
        }
    })

    [System.Windows.Forms.Application]::EnableVisualStyles()
    Load-VideoList
    [System.Windows.Forms.Application]::Run($form)
}
