:Git_Code %projectName%
    SET a=%~1
    SET b=%a%.git
    git remote add origin https://github.com/TriniKiskadee/%b%
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
EXIT /B 0