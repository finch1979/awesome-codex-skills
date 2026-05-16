Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"

$defaultFolder = "C:\Users\finch\Documents\fMRI"
$defaultAttachment = "C:\Users\finch\Documents\fMRI.zip"
$logPath = Join-Path $PSScriptRoot "send-mail-gui.log"

function Get-ExceptionDetails {
    param([System.Exception]$Exception)

    $messages = New-Object System.Collections.Generic.List[string]
    $current = $Exception
    while ($null -ne $current) {
        $messages.Add(($current.GetType().FullName + ": " + $current.Message))
        $current = $current.InnerException
    }

    return ($messages -join [Environment]::NewLine)
}

function Write-Log {
    param([string]$Message)

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $logPath -Encoding UTF8 -Value "[$timestamp] $Message"
}

function ConvertTo-Base64Lines {
    param([byte[]]$Bytes)

    $base64 = [Convert]::ToBase64String($Bytes)
    $lines = New-Object System.Collections.Generic.List[string]
    for ($i = 0; $i -lt $base64.Length; $i += 76) {
        $length = [Math]::Min(76, $base64.Length - $i)
        $lines.Add($base64.Substring($i, $length))
    }
    return ($lines -join "`r`n")
}

function ConvertTo-MimeWord {
    param([string]$Text)

    if ($Text -match "^[\x00-\x7F]+$") {
        return $Text
    }

    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    return "=?UTF-8?B?$([Convert]::ToBase64String($bytes))?="
}

function Escape-CurlConfigValue {
    param([string]$Value)

    return ($Value -replace "\\", "\\" -replace '"', '\"')
}

function New-MimeMessageFile {
    param(
        [string]$From,
        [string]$To,
        [string]$Subject,
        [string]$Body,
        [string]$Attachment
    )

    $boundary = "----=_CodexYahooMailer_$([Guid]::NewGuid().ToString("N"))"
    $attachmentName = [System.IO.Path]::GetFileName($Attachment)
    $bodyBase64 = ConvertTo-Base64Lines ([System.Text.Encoding]::UTF8.GetBytes($Body))
    $attachmentBase64 = ConvertTo-Base64Lines ([System.IO.File]::ReadAllBytes($Attachment))
    $encodedSubject = ConvertTo-MimeWord $Subject
    $encodedAttachmentName = ConvertTo-MimeWord $attachmentName

    $content = @"
From: <$From>
To: $To
Subject: $encodedSubject
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="$boundary"

--$boundary
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: base64

$bodyBase64
--$boundary
Content-Type: application/zip; name="$encodedAttachmentName"
Content-Disposition: attachment; filename="$encodedAttachmentName"
Content-Transfer-Encoding: base64

$attachmentBase64
--$boundary--
"@

    $path = Join-Path ([System.IO.Path]::GetTempPath()) "codex-yahoo-mail-$([Guid]::NewGuid().ToString("N")).eml"
    [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)
    return $path
}

function Set-Status {
    param(
        [System.Windows.Forms.Label]$Label,
        [string]$Text,
        [System.Drawing.Color]$Color
    )

    $Label.Text = $Text
    $Label.ForeColor = $Color
    [System.Windows.Forms.Application]::DoEvents()
}

function New-Label {
    param([string]$Text, [int]$X, [int]$Y)

    $label = New-Object System.Windows.Forms.Label
    $label.Text = $Text
    $label.Location = New-Object System.Drawing.Point($X, $Y)
    $label.Size = New-Object System.Drawing.Size(130, 24)
    $label.TextAlign = [System.Drawing.ContentAlignment]::MiddleRight
    return $label
}

function New-TextBox {
    param([string]$Text, [int]$X, [int]$Y, [int]$Width, [int]$Height = 28)

    $box = New-Object System.Windows.Forms.TextBox
    $box.Text = $Text
    $box.Location = New-Object System.Drawing.Point($X, $Y)
    $box.Size = New-Object System.Drawing.Size($Width, $Height)
    return $box
}

function Compress-FmriFolder {
    param([string]$Folder, [string]$ZipPath)

    if (-not (Test-Path -LiteralPath $Folder)) {
        throw "找不到資料夾：$Folder"
    }

    $files = Get-ChildItem -LiteralPath $Folder -File
    if ($files.Count -eq 0) {
        throw "資料夾沒有可壓縮的檔案：$Folder"
    }

    if (Test-Path -LiteralPath $ZipPath) {
        Remove-Item -LiteralPath $ZipPath -Force
    }

    Compress-Archive -LiteralPath ($files | ForEach-Object { $_.FullName }) -DestinationPath $ZipPath -Force
}

function Send-YahooMail {
    param(
        [string]$From,
        [string]$Password,
        [string]$To,
        [string]$Subject,
        [string]$Body,
        [string]$Attachment
    )

    if ([string]::IsNullOrWhiteSpace($From)) {
        throw "請輸入 Yahoo 寄件信箱。"
    }
    if ([string]::IsNullOrWhiteSpace($Password)) {
        throw "請輸入 Yahoo App Password。"
    }
    $Password = $Password -replace "\s", ""
    if ([string]::IsNullOrWhiteSpace($To)) {
        throw "請輸入收件人。"
    }
    if (-not (Test-Path -LiteralPath $Attachment)) {
        throw "找不到附件：$Attachment"
    }
    if ($From -notmatch "@yahoo\.") {
        throw "寄件信箱看起來不是 Yahoo 信箱。請輸入完整 Yahoo 信箱，例如 name@yahoo.com 或 name@yahoo.com.tw。"
    }

    $curl = Get-Command curl.exe -ErrorAction SilentlyContinue
    if ($null -eq $curl) {
        throw "找不到 curl.exe。此版本需要 Windows 內建 curl 來使用 Yahoo SMTPS。"
    }

    $recipients = $To -split "[,;]" | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    if ($recipients.Count -eq 0) {
        throw "請輸入至少一個收件人。"
    }

    $emlPath = $null
    $configPath = $null

    try {
        $emlPath = New-MimeMessageFile -From $From -To ($recipients -join ", ") -Subject $Subject -Body $Body -Attachment $Attachment
        $configPath = Join-Path ([System.IO.Path]::GetTempPath()) "codex-yahoo-curl-$([Guid]::NewGuid().ToString("N")).conf"

        $config = New-Object System.Collections.Generic.List[string]
        $config.Add('url = "smtps://smtp.mail.yahoo.com:465"')
        $config.Add('ssl-reqd')
        $config.Add('ssl-no-revoke')
        $config.Add('silent')
        $config.Add('show-error')
        $config.Add(('user = "' + (Escape-CurlConfigValue "$From`:$Password") + '"'))
        $config.Add(('mail-from = "' + (Escape-CurlConfigValue $From) + '"'))
        foreach ($recipient in $recipients) {
            $config.Add(('mail-rcpt = "' + (Escape-CurlConfigValue $recipient) + '"'))
        }
        $config.Add(('upload-file = "' + (Escape-CurlConfigValue $emlPath) + '"'))
        [System.IO.File]::WriteAllLines($configPath, $config.ToArray(), [System.Text.Encoding]::ASCII)

        $stdoutPath = Join-Path ([System.IO.Path]::GetTempPath()) "codex-yahoo-curl-out-$([Guid]::NewGuid().ToString("N")).txt"
        $stderrPath = Join-Path ([System.IO.Path]::GetTempPath()) "codex-yahoo-curl-err-$([Guid]::NewGuid().ToString("N")).txt"
        $process = Start-Process -FilePath $curl.Source -ArgumentList @("--config", $configPath) -NoNewWindow -Wait -PassThru -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
        $exitCode = $process.ExitCode
        $output = @()
        if (Test-Path -LiteralPath $stdoutPath) {
            $output += Get-Content -LiteralPath $stdoutPath -ErrorAction SilentlyContinue
            Remove-Item -LiteralPath $stdoutPath -Force -ErrorAction SilentlyContinue
        }
        if (Test-Path -LiteralPath $stderrPath) {
            $output += Get-Content -LiteralPath $stderrPath -ErrorAction SilentlyContinue
            Remove-Item -LiteralPath $stderrPath -Force -ErrorAction SilentlyContinue
        }
        Write-Log ("curl exit code: $exitCode")
        Write-Log (($output | Out-String).Trim())

        if ($exitCode -ne 0) {
            throw "curl 寄送失敗，exit code $exitCode。`n$($output | Out-String)"
        }
    }
    finally {
        if ($configPath -and (Test-Path -LiteralPath $configPath)) {
            Remove-Item -LiteralPath $configPath -Force
        }
        if ($emlPath -and (Test-Path -LiteralPath $emlPath)) {
            Remove-Item -LiteralPath $emlPath -Force
        }
    }
}

$font = New-Object System.Drawing.Font("Microsoft JhengHei UI", 10)
$titleFont = New-Object System.Drawing.Font("Microsoft JhengHei UI", 14, [System.Drawing.FontStyle]::Bold)

$form = New-Object System.Windows.Forms.Form
$form.Text = "Yahoo 寄信工具"
$form.Size = New-Object System.Drawing.Size(720, 570)
$form.StartPosition = "CenterScreen"
$form.FormBorderStyle = "FixedDialog"
$form.MaximizeBox = $false
$form.Font = $font

$title = New-Object System.Windows.Forms.Label
$title.Text = "Yahoo 寄信工具"
$title.Font = $titleFont
$title.Location = New-Object System.Drawing.Point(24, 18)
$title.Size = New-Object System.Drawing.Size(640, 34)
$form.Controls.Add($title)

$note = New-Object System.Windows.Forms.Label
$note.Text = "請使用 Yahoo App Password，不要輸入一般登入密碼。附件預設為 fMRI.zip。"
$note.Location = New-Object System.Drawing.Point(28, 54)
$note.Size = New-Object System.Drawing.Size(650, 28)
$note.ForeColor = [System.Drawing.Color]::FromArgb(80, 80, 80)
$form.Controls.Add($note)

$fromLabel = New-Label "寄件信箱" 24 98
$fromBox = New-TextBox "" 170 98 480
$form.Controls.AddRange(@($fromLabel, $fromBox))

$passwordLabel = New-Label "App Password" 24 138
$passwordBox = New-TextBox "" 170 138 480
$passwordBox.UseSystemPasswordChar = $true
$form.Controls.AddRange(@($passwordLabel, $passwordBox))

$toLabel = New-Label "收件人" 24 178
$toBox = New-TextBox "finchlwb@yahoo.com.tw" 170 178 480
$form.Controls.AddRange(@($toLabel, $toBox))

$subjectLabel = New-Label "主旨" 24 218
$subjectBox = New-TextBox "fMRI" 170 218 480
$form.Controls.AddRange(@($subjectLabel, $subjectBox))

$bodyLabel = New-Label "信件內容" 24 258
$bodyBox = New-Object System.Windows.Forms.TextBox
$bodyBox.Text = "您好，附件是我要寄給您的文件，請查收。"
$bodyBox.Location = New-Object System.Drawing.Point(170, 258)
$bodyBox.Size = New-Object System.Drawing.Size(480, 96)
$bodyBox.Multiline = $true
$bodyBox.ScrollBars = "Vertical"
$form.Controls.AddRange(@($bodyLabel, $bodyBox))

$attachmentLabel = New-Label "附件" 24 374
$attachmentBox = New-TextBox $defaultAttachment 170 374 365
$browseButton = New-Object System.Windows.Forms.Button
$browseButton.Text = "選擇..."
$browseButton.Location = New-Object System.Drawing.Point(545, 372)
$browseButton.Size = New-Object System.Drawing.Size(105, 32)
$form.Controls.AddRange(@($attachmentLabel, $attachmentBox, $browseButton))

$zipButton = New-Object System.Windows.Forms.Button
$zipButton.Text = "重新壓縮 fMRI 資料夾"
$zipButton.Location = New-Object System.Drawing.Point(170, 420)
$zipButton.Size = New-Object System.Drawing.Size(190, 36)
$form.Controls.Add($zipButton)

$sendButton = New-Object System.Windows.Forms.Button
$sendButton.Text = "寄出"
$sendButton.Location = New-Object System.Drawing.Point(480, 420)
$sendButton.Size = New-Object System.Drawing.Size(170, 36)
$sendButton.BackColor = [System.Drawing.Color]::FromArgb(30, 115, 190)
$sendButton.ForeColor = [System.Drawing.Color]::White
$sendButton.FlatStyle = "Flat"
$form.Controls.Add($sendButton)

$statusLabel = New-Object System.Windows.Forms.Label
$statusLabel.Text = "狀態：等待操作"
$statusLabel.Location = New-Object System.Drawing.Point(28, 476)
$statusLabel.Size = New-Object System.Drawing.Size(650, 34)
$statusLabel.ForeColor = [System.Drawing.Color]::FromArgb(80, 80, 80)
$form.Controls.Add($statusLabel)

$browseButton.Add_Click({
    $dialog = New-Object System.Windows.Forms.OpenFileDialog
    $dialog.Title = "選擇附件"
    $dialog.Filter = "Zip/PDF files (*.zip;*.pdf)|*.zip;*.pdf|All files (*.*)|*.*"
    if (Test-Path -LiteralPath $defaultFolder) {
        $dialog.InitialDirectory = $defaultFolder
    }

    if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        $attachmentBox.Text = $dialog.FileName
        Set-Status $statusLabel "狀態：已選擇附件 $($dialog.FileName)" ([System.Drawing.Color]::FromArgb(80, 80, 80))
    }
})

$zipButton.Add_Click({
    try {
        $zipButton.Enabled = $false
        Set-Status $statusLabel "狀態：正在壓縮 fMRI 資料夾..." ([System.Drawing.Color]::FromArgb(80, 80, 80))
        Compress-FmriFolder $defaultFolder $defaultAttachment
        $attachmentBox.Text = $defaultAttachment
        Set-Status $statusLabel "狀態：壓縮完成，附件已設為 $defaultAttachment" ([System.Drawing.Color]::FromArgb(30, 120, 60))
    }
    catch {
        $details = Get-ExceptionDetails $_.Exception
        Write-Log "Zip error: $details"
        Set-Status $statusLabel "錯誤：$($_.Exception.Message)" ([System.Drawing.Color]::Firebrick)
        [System.Windows.Forms.MessageBox]::Show($details, "壓縮失敗", "OK", "Error") | Out-Null
    }
    finally {
        $zipButton.Enabled = $true
    }
})

$sendButton.Add_Click({
    try {
        $sendButton.Enabled = $false
        $zipButton.Enabled = $false
        Set-Status $statusLabel "狀態：正在寄出，請稍候..." ([System.Drawing.Color]::FromArgb(80, 80, 80))

        Send-YahooMail `
            -From $fromBox.Text `
            -Password $passwordBox.Text `
            -To $toBox.Text `
            -Subject $subjectBox.Text `
            -Body $bodyBox.Text `
            -Attachment $attachmentBox.Text

        Set-Status $statusLabel "狀態：已送出。請到 Yahoo 寄件備份確認。" ([System.Drawing.Color]::FromArgb(30, 120, 60))
        [System.Windows.Forms.MessageBox]::Show("信件已送出。請到 Yahoo 寄件備份確認。", "寄送完成", "OK", "Information") | Out-Null
    }
    catch {
        $details = Get-ExceptionDetails $_.Exception
        $hint = @"
$details

常見原因：
1. App Password 不是 Yahoo 產生的 App Password，而是一般登入密碼。
2. 寄件信箱與 App Password 所屬帳號不一致。
3. Yahoo 帳號未啟用第三方 App Password，或帳號安全設定阻擋 SMTP。
4. 防火牆或網路阻擋 smtp.mail.yahoo.com:465。
5. Windows 憑證撤銷檢查暫時連不到伺服器；此工具已用 curl 的 ssl-no-revoke 避免這個 Windows Schannel 問題。

詳細紀錄：$logPath
"@
        Write-Log "Send error: $details"
        Set-Status $statusLabel "錯誤：$($_.Exception.Message)" ([System.Drawing.Color]::Firebrick)
        [System.Windows.Forms.MessageBox]::Show($hint, "寄送失敗", "OK", "Error") | Out-Null
    }
    finally {
        $sendButton.Enabled = $true
        $zipButton.Enabled = $true
    }
})

[System.Windows.Forms.Application]::EnableVisualStyles()
[System.Windows.Forms.Application]::Run($form)
