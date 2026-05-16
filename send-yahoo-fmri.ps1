param(
    [string]$From,
    [string]$To = "finchlwb@yahoo.com.tw",
    [string]$Subject = "fMRI",
    [string]$Body = "Hello, please find the attached document.",
    [string]$Attachment = "C:\Users\finch\Documents\fMRI.zip"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Attachment)) {
    throw "Attachment not found: $Attachment"
}

if ([string]::IsNullOrWhiteSpace($From)) {
    $From = Read-Host "Yahoo sender email"
}

$securePassword = Read-Host "Yahoo app password" -AsSecureString
$credential = New-Object System.Net.NetworkCredential($From, $securePassword)

$message = New-Object System.Net.Mail.MailMessage
$message.From = $From
$message.To.Add($To)
$message.Subject = $Subject
$message.Body = $Body
$message.BodyEncoding = [System.Text.Encoding]::UTF8
$message.SubjectEncoding = [System.Text.Encoding]::UTF8
$message.Attachments.Add($Attachment) | Out-Null

$client = New-Object System.Net.Mail.SmtpClient("smtp.mail.yahoo.com", 587)
$client.EnableSsl = $true
$client.Credentials = $credential

try {
    $client.Send($message)
    Write-Host "Sent to $To with attachment $Attachment"
}
finally {
    $message.Dispose()
    $client.Dispose()
}
