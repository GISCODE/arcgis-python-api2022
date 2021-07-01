
# $git_installed = cver all -lo | Select-string -Pattern "^git"
# if ($git_installed.length -eq 0 ) {
#    choco install -y git.install
#     }
# else {
#     echo "Skipping git installation"
#     }
$python_installed = cver all -lo | Select-string -Pattern "python3 3.9.4"
if ($python_installed.length -eq 0 ) {
    choco install -y python3 --version=3.9.4
    }
else {
    echo "Skipping python installation"
    }
# $node_installed = cver all -lo | Select-string -Pattern "^nodejs"
# if ($node_installed.length -eq 0 ) {
#     choco install -y nodejs --version=13.11.0
#     }
# else {
#     echo "Skipping node installation"
#     }
$nssm_installed = cver all -lo | Select-string -Pattern "^nssm"
if ($nssm_installed.length -eq 0 ) {
    choco install -y nssm
    }
else {
        echo "Skipping nssm installation"
    }