$username = Read-Host "Enter username"

if($username.length -lt 6 )
    {
    Write-Output 0
    }
else {
    Write-Output $username
    }
