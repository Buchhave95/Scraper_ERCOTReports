echo off

set reportid="%1"
cd /D "%~dp0"
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id %reportid%
pause