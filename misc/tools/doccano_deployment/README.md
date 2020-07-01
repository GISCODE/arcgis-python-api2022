
# Script for automated deployment of doccano.
 
## This process will automatically install the following deployment related requirements:
- Node.js, nssm, Git, Chocolatey & Windows build tools. (all of these to the, latest release)
- Python (ver. 3.7.2) 
- Python virtual environment, with all the necessary dependencies.
- The deployment will take around 30-60 minutes, _depending on the internet speed & pre-installed requirements, if any._ 

## Make sure to place the deployment folder on C drive.
## Run 'Install.bat' as _admin._ to initiate the script.
## Please note that the vs_build_tools installation will take a long time and it will seem like it is stuck with a message 
## "Python 2.7 is successfuly installed", let the setup run as it is installing build tools in the background at that point.
## At the final stage, it will ask the user to setup 'username' & 'password'.
## Incase install package crashes, restart your system and run 'Install.bat' as _admin._ again.
## Post deployment, docanno can be accessed from http://127.0.0.1:8000/ or  http://localhost:8000/ .
### *For uninstalling doccano, run 'uninstall.bat' as _admin._*
### *More info on doccano at: https://github.com/doccano/doccano*

