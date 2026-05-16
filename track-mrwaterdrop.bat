@echo off
set "SCRIPT_DIR=%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%track-youtube-channel.ps1" -ChannelId "UCeTLfPD7thTMabtL7w87Aug" -ChannelName "清流君" -OpenReport
