$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$scriptPath = Join-Path $repoRoot "track-youtube-channel.ps1"

if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing tracker script: $scriptPath"
}

. $scriptPath

$sampleFeed = @'
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015"
      xmlns:media="http://search.yahoo.com/mrss/"
      xmlns="http://www.w3.org/2005/Atom">
  <title>清流君</title>
  <entry>
    <yt:videoId>abc123</yt:videoId>
    <title>第一支影片</title>
    <link rel="alternate" href="https://www.youtube.com/watch?v=abc123"/>
    <published>2026-05-10T13:40:00+00:00</published>
  </entry>
  <entry>
    <yt:videoId>def456</yt:videoId>
    <title>第二支影片</title>
    <link rel="alternate" href="https://www.youtube.com/watch?v=def456"/>
    <published>2026-02-23T05:30:00+00:00</published>
  </entry>
</feed>
'@

$videos = ConvertFrom-YouTubeFeed -XmlText $sampleFeed
if ($videos.Count -ne 2) {
    throw "Expected 2 parsed videos, got $($videos.Count)"
}
if ($videos[0].Title -ne "第一支影片") {
    throw "Unexpected first title: $($videos[0].Title)"
}
if ($videos[0].VideoId -ne "abc123") {
    throw "Unexpected first video id: $($videos[0].VideoId)"
}

$known = @(
    [pscustomobject]@{ VideoId = "def456"; Title = "第二支影片" }
)
$newVideos = @(Compare-TrackedVideos -CurrentVideos $videos -KnownVideos $known)
if ($newVideos.Count -ne 1) {
    throw "Expected 1 new video, got $($newVideos.Count)"
}
if ($newVideos[0].VideoId -ne "abc123") {
    throw "Unexpected new video id: $($newVideos[0].VideoId)"
}

"youtube tracker tests passed"
