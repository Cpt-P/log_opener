@echo off
color 0D
echo Disclaimer: This batch script is not affiliated with, endorsed by, or sponsored by SKLauncher or its developers. SKLauncher is a product of skmedix.pl. This batch script is a fan-made mod/launcher that uses SKLauncher as a base/dependency. The author of this batch script is solely responsible for its content and functionality. Any issues, bugs, or feedback related to this batch script should be directed to the author, not to SKLauncher or its developers. Use this batch script at your own risk. The author is not liable for any damages or losses that may result from using this batch script.
echo.
echo ---------------------------------------------
echo        Minecraft Log Opener v0 - Beta
echo ---------------------------------------------
echo.
echo Welcome to the Minecraft log opener by Cpt...
echo.
rem Credits goes to Archon for this code line
set logfile=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%_skl_log_opener.log

echo Please choose one of the following options:
echo Your selection will be copied to your clipboard.
echo.
echo 1. Open the SKlauncher log
echo 2. Open the game log
echo 3. Open the crash report
echo 4. Exit
echo.
set /p choice=Enter your choice: 

echo User choice: %choice% >> %logfile%
echo Date and time: %date% %time% >> %logfile%

if %choice%==1 (
    echo Opening the SKlauncher log >> %logfile%
    clip < %appdata%\.minecraft\sklauncher\sklauncher_logs.txt
    start %appdata%\.minecraft\sklauncher\sklauncher_logs.txt
) else if %choice%==2 (
    echo Opening the game log >> %logfile%
    clip < %appdata%\.minecraft\logs\latest.log
    start %appdata%\.minecraft\logs\latest.log
) else if %choice%==3 (
    for /f "delims=" %%a in ('dir /b /od %appdata%\.minecraft\crash-reports\*.txt') do set latest=%%a
    echo Opening the crash report %latest% >> %logfile%
    clip < %appdata%\.minecraft\crash-reports\%latest%
    start %appdata%\.minecraft\crash-reports\%latest%
) else if %choice%==4 (
    exit
) else (
    echo Invalid choice. Please try again. 
    pause
    goto :EOF
)

color 0E
echo Opening the selected log... 
timeout /t 3

color 0A
echo Task complete... Log file can be found in the same directory of this Batch script.
echo.
echo Feel free to provide your feedback. Thanks for using.
ping localhost -n 2 >\\.\nul 
pause
