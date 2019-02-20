<# Variables #>
$PROJECT_NAME = "DJANGOCMS_HTML_TAGS"

if ($env:ENV -eq "PROD") {
    $env_str = "production"
    $env_prefix = "prod"
}
elseif ($env:ENV -eq "STAGING") {
    $env_str = "staging"
    $env_prefix = "staging"
}
else {
    if ($env:ENV -ne "DEV") {
        $env:ENV = "DEV"
    }
    $env_str = "development"
    $env_prefix = "dev"
}

<# Functions #>
function Get-Help {
    Write-Host -ForegroundColor Cyan "Available Environments"
    Write-Output "  - DEV (default)"
    Write-Output "  - PROD"
    Write-Output "  - STAGING"
    Write-Output ""

    Write-Host -ForegroundColor Cyan "Available commands"
    Write-Output "  > docker [:command]      Run a Docker command."
    Write-Output "  > runtests               Run unit tests."
    Write-Output "  > shell                  Open Bash session in the backend service."
}

function Start-Docker ([string] $subParams) {
    if ($subParams -eq "") {
        $command = "docker-compose --help"
    }
    else {
        $conf1 = "docker\docker-compose.yml"
        $conf2 = "docker\docker-compose.$env_prefix.yml"
        $command = "docker-compose -p $PROJECT_NAME -f $conf1 -f $conf2 $subParams"
    }

    Write-Host -ForegroundColor Cyan -NoNewLine "    Command: "
    Write-Output $command
    Write-Output ""

    Invoke-Expression $command
}

function Start-Runtests ([string] $subParams) {
    $test_command = "'
        coverage run setup.py test &&
        coverage html
    '"
    Start-Docker "run --rm backend sh -c $test_command"
}

function Start-Shell ([string] $subParams) {
    if ($subParams -eq "") {
        $service = "backend"
    }
    else {
        $service = $subParams
    }
    Start-Docker "run --rm $service bash"
}

<# Set default parameter as help. #>
if ($args.Length -eq 0) {
    $param = "help"
    $subParams = ""
}
else {
    $param, $subParams = $args
}

if ($param -ne "help") {
    Write-Host -ForegroundColor Cyan -NoNewLine "Environment: "
    Write-Output $env_str
}

<# We use switch instead of alias because there are some constant variables like `start`. #>
switch ($param) {
    "docker" { Start-Docker $subParams }
    "runtests" { Start-Runtests $subParams }
    "shell" { Start-Shell $subParams }
    Default { Get-Help }
}
