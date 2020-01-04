@echo off
SETLOCAL
set name=Banana
set a=%name%.git
CALL :stringConcat %a%
EXIT /B

:stringConcat %a%
    echo this is the output %~1
    echo function call is working
EXIT /B 0