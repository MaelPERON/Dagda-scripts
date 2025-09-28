@echo off
cd %project%
set first=%1
set second=%2
if "%first%"=="" (
    echo First argument is missing.
    exit /b 1
)

if "%second%"=="" (
    echo Second argument is missing.
    exit /b 1
)

set third=%3
if /I "%third%"=="true" (
    echo Third argument is true.
) else (
    echo Third argument is false or not provided.
)

echo Comparing %first% to %second%

if /I "%third%"=="true" (
    git log --oneline %first%..%second% > diff.txt
) else (
    git diff %first%..%second% > diff.txt
)
echo Diff saved to diff.txt