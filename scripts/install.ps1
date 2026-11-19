# Install all focused skills globally (Windows PowerShell)
# Usage: powershell -ExecutionPolicy Bypass -File scripts\install.ps1
$ErrorActionPreference = "Stop"
$Skills = Join-Path $PSScriptRoot "..\skills"
$Targets = @(
  "$HOME\.claude\skills",            # Claude Code
  "$HOME\.agents\skills",            # Codex, Gemini CLI, generic Agent Skills
  "$HOME\.codex\skills",             # Codex (older versions)
  "$HOME\.gemini\skills",            # Gemini CLI
  "$HOME\.config\opencode\skills"    # OpenCode
)
foreach ($t in $Targets) {
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  $old = Join-Path $t "deep-research-domain-council"   # v16 and earlier: one big skill
  if (Test-Path $old) { Remove-Item -Recurse -Force $old }
  Get-ChildItem $Skills -Directory | ForEach-Object {
    $dst = Join-Path $t $_.Name
    if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
    Copy-Item -Recurse $_.FullName $dst
  }
  Write-Host "Installed skills -> $t"
}
Write-Host "Done. Restart your agent, then check with /skills."
