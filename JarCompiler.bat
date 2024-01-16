@echo off
dir /b *.java
setlocal enabledelayedexpansion
set i=0
for %%f in (*.java) do (
  set /a i+=1
  set file[!i!]=%%f
)
echo Choose a java file to compile:
for /l %%i in (1,1,%i%) do echo %%i. !file[%%i]!
set /p choice=Enter the number of the java file to compile: 
set filename=!file[%choice%]!
set filename=%filename:~0,-5%
if not exist build mkdir build
javac %filename%.java
jar cvfe build\%filename%.jar %filename% %filename%.class -c
del %filename%.class
echo The jar file has been created in the build folder.
pause
