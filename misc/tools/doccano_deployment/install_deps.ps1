
$git_installed = cver all -lo | Select-string -Pattern "^git"
if ($git_installed.length -eq 0 ) {
    choco install -y git
    }
else {
    echo "Skipping git installation"
    }
$git_installed = cver all -lo | Select-string -Pattern "^python"
if ($git_installed.length -eq 0 ) {
    choco install -y python --version=3.6.8
    }
else {
    echo "Skipping python installation"
    }
$git_installed = cver all -lo | Select-string -Pattern "^nodejs"
if ($git_installed.length -eq 0 ) {
    choco install -y nodejs
    }
else {
    echo "Skipping node installation"
    }
$git_installed = cver all -lo | Select-string -Pattern "^nssm"
if ($git_installed.length -eq 0 ) {
    choco install -y nssm
    }
else {
    echo "Skipping nssm installation"
   }
