$error_count=$error.count
$ErrorActionPreference= 'silentlycontinue'
choco -v 
if ($error_count -eq $error.count){
    echo "Skipping chocolatey installation as it was already installed."
    }
else {
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    }