$password1 = Read-Host "Enter password" -AsSecureString
$password1 = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($password1)
$password1 = [Runtime.InteropServices.Marshal]::PtrToStringAuto($password1)

$password2 = Read-Host "Re-enter password" -AsSecureString
$password2 = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($password2)
$password2 = [Runtime.InteropServices.Marshal]::PtrToStringAuto($password2)

if($password1 -eq $password2){
    if($password2.length -lt 6 ){
    Write-Output 1
    }
    else {
        Write-Output $password1
        }

}
else{
    Write-Output 0
}