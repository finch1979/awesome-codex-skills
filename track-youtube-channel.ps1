param(
    [string]$ChannelId = "UCeTLfPD7thTMabtL7w87Aug",
    [string]$ChannelName = "清流君",
    [string]$StatePath = "$PSScriptRoot\youtube-tracker-state.json",
    [string]$ReportPath = "$PSScriptRoot\youtube-tracker-report.md",
    [switch]$OpenReport
)

$ErrorActionPreference = "Stop"

function ConvertFrom-YouTubeFeed {
    param([Parameter(Mandatory = $true)][string]$XmlText)

    [xml]$xml = $XmlText
    $entries = $xml.SelectNodes("//*[local-name()='entry']")
    $videos = New-Object System.Collections.Generic.List[object]

    foreach ($entry in $entries) {
        $videoIdNode = $entry.SelectSingleNode("*[local-name()='videoId']")
        $titleNode = $entry.SelectSingleNode("*[local-name()='title']")
        $publishedNode = $entry.SelectSingleNode("*[local-name()='published']")
        $linkNode = $entry.SelectSingleNode("*[local-name()='link' and @rel='alternate']")

        if ($null -eq $videoIdNode -or $null -eq $titleNode) {
            continue
        }

        $url = "https://www.youtube.com/watch?v=$($videoIdNode.InnerText)"
        if ($null -ne $linkNode -and $linkNode.HasAttribute("href")) {
            $url = $linkNode.GetAttribute("href")
        }

        $videos.Add([pscustomobject]@{
            VideoId = $videoIdNode.InnerText
            Title = $titleNode.InnerText
            Published = $publishedNode.InnerText
            Url = $url
        })
    }

    return $videos.ToArray()
}

function Compare-TrackedVideos {
    param(
        [Parameter(Mandatory = $true)][object[]]$CurrentVideos,
        [object[]]$KnownVideos = @()
    )

    $knownIds = @{}
    foreach ($video in @($KnownVideos)) {
        if ($video.VideoId) {
            $knownIds[$video.VideoId] = $true
        }
    }

    return @($CurrentVideos | Where-Object { -not $knownIds.ContainsKey($_.VideoId) })
}

function Read-TrackedVideos {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return @()
    }

    $json = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ([string]::IsNullOrWhiteSpace($json)) {
        return @()
    }

    return @($json | ConvertFrom-Json)
}

function Write-TrackedVideos {
    param(
        [string]$Path,
        [object[]]$Videos
    )

    $Videos |
        Sort-Object Published -Descending |
        ConvertTo-Json -Depth 5 |
        Set-Content -LiteralPath $Path -Encoding UTF8
}

function Write-TrackerReport {
    param(
        [string]$Path,
        [string]$ChannelName,
        [string]$ChannelId,
        [object[]]$CurrentVideos,
        [object[]]$NewVideos
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add("# YouTube 追蹤報告")
    $lines.Add("")
    $lines.Add("頻道：$ChannelName")
    $lines.Add("")
    $lines.Add("Channel ID：``$ChannelId``")
    $lines.Add("")
    $lines.Add("更新時間：$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
    $lines.Add("")
    $lines.Add("## 新影片")
    $lines.Add("")

    if ($NewVideos.Count -eq 0) {
        $lines.Add("目前沒有偵測到新影片。")
    }
    else {
        foreach ($video in $NewVideos) {
            $lines.Add("- [$($video.Title)]($($video.Url))")
            $lines.Add("  - 發布時間：$($video.Published)")
        }
    }

    $lines.Add("")
    $lines.Add("## RSS 目前最新影片")
    $lines.Add("")
    foreach ($video in $CurrentVideos) {
        $lines.Add("- [$($video.Title)]($($video.Url))")
        $lines.Add("  - 發布時間：$($video.Published)")
    }

    Set-Content -LiteralPath $Path -Encoding UTF8 -Value $lines
}

function Invoke-YouTubeTracker {
    param(
        [string]$ChannelId,
        [string]$ChannelName,
        [string]$StatePath,
        [string]$ReportPath,
        [switch]$OpenReport
    )

    $feedUrl = "https://www.youtube.com/feeds/videos.xml?channel_id=$ChannelId"
    $response = Invoke-WebRequest -Uri $feedUrl -UseBasicParsing -TimeoutSec 30
    $currentVideos = @(ConvertFrom-YouTubeFeed -XmlText $response.Content)
    $knownVideos = @(Read-TrackedVideos -Path $StatePath)
    $newVideos = @(Compare-TrackedVideos -CurrentVideos $currentVideos -KnownVideos $knownVideos)

    Write-TrackedVideos -Path $StatePath -Videos $currentVideos
    Write-TrackerReport -Path $ReportPath -ChannelName $ChannelName -ChannelId $ChannelId -CurrentVideos $currentVideos -NewVideos $newVideos

    if ($OpenReport) {
        Start-Process -FilePath $ReportPath
    }

    [pscustomobject]@{
        ChannelName = $ChannelName
        ChannelId = $ChannelId
        CurrentVideoCount = $currentVideos.Count
        NewVideoCount = $newVideos.Count
        ReportPath = $ReportPath
        StatePath = $StatePath
    }
}

if ($MyInvocation.InvocationName -ne ".") {
    Invoke-YouTubeTracker `
        -ChannelId $ChannelId `
        -ChannelName $ChannelName `
        -StatePath $StatePath `
        -ReportPath $ReportPath `
        -OpenReport:$OpenReport
}
