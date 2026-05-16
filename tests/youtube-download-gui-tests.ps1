$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$scriptPath = Join-Path $repoRoot "youtube-download-gui.ps1"

if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing GUI script: $scriptPath"
}

. $scriptPath -NoGui

$tempState = Join-Path ([System.IO.Path]::GetTempPath()) "youtube-state-test-$([Guid]::NewGuid().ToString('N')).json"
try {
    @(
        [pscustomobject]@{
            VideoId = "abc123"
            Title = "測試影片"
            Published = "2026-05-10T13:48:37+00:00"
            Url = "https://www.youtube.com/watch?v=abc123"
        }
    ) | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $tempState -Encoding UTF8

    $videos = @(Read-YouTubeDownloadState -Path $tempState)
    if ($videos.Count -ne 1) {
        throw "Expected 1 video, got $($videos.Count)"
    }
    if ($videos[0].Title -ne "測試影片") {
        throw "Unexpected title: $($videos[0].Title)"
    }

    $format = Get-YtDlpFormat -Quality "720p" -AudioOnly:$false
    if ($format -ne "bestvideo[height<=720]+bestaudio/best[height<=720]") {
        throw "Unexpected 720p format: $format"
    }

    $audioFormat = Get-YtDlpFormat -Quality "best" -AudioOnly:$true
    if ($audioFormat -ne "bestaudio/best") {
        throw "Unexpected audio format: $audioFormat"
    }

    $quoted = ConvertTo-ProcessArgument "C:\Users\finch\Videos\MrWaterDrop\%(upload_date)s - %(title)s.%(ext)s"
    if (-not ($quoted.StartsWith('"') -and $quoted.EndsWith('"'))) {
        throw "Expected spaced argument to be quoted: $quoted"
    }

    "youtube download gui tests passed"
}
finally {
    Remove-Item -LiteralPath $tempState -Force -ErrorAction SilentlyContinue
}
