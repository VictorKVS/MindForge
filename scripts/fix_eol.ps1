# fix_eol.ps1
# Normalize line endings CRLF → LF and log changes

Write-Host "Start normalization of line endings..."

# Extensions to process
$extensions = @("*.py", "*.md", "*.yml", "*.yaml", "*.toml", "*.txt", "*.gitignore", "*.gitattributes")

# Root of project
$root = Get-Location
$logFile = Join-Path $PSScriptRoot "fix_eol.log"

# Очистим лог перед новым запуском
"" | Out-File -FilePath $logFile -Encoding utf8

foreach ($ext in $extensions) {
    Get-ChildItem -Path $root -Recurse -Include $ext | ForEach-Object {
        try {
            $content = Get-Content $_.FullName -Raw
            $normalized = $content -replace "`r`n", "`n"

            if ($content -ne $normalized) {
                Set-Content $_.FullName $normalized -NoNewline -Encoding utf8
                Write-Host "Updated:" $_.FullName
                "Updated: $($_.FullName)" | Out-File -FilePath $logFile -Append -Encoding utf8
            }
        }
        catch {
            Write-Warning "Error processing: $($_.FullName)"
            "Error: $($_.FullName)" | Out-File -FilePath $logFile -Append -Encoding utf8
        }
    }
}

Write-Host "Done. All line endings are normalized to LF"
"Done. Normalization completed at $(Get-Date)" | Out-File -FilePath $logFile -Append -Encoding utf8