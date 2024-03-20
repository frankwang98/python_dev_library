@echo off
echo delay 1:  %time%
ping /n 3 127.0.0.1 > null
echo delay 2:  %time%
del null

echo ----------
ping 127.0.0.1 >nul /n 1 & set /p=<nul
for /L %%i in (1 1 39) do set /p a= < nul & ping /n 1 127.0.0.1 > nul
echo 100%%
echo ----------

pause