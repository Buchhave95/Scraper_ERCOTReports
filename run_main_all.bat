echo off

cd /D "%~dp0"
echo Downloading 13499
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13499

echo Downloading 15933
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 15933

echo Downloading 16554
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 16554

echo Downloading 21812
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 21812

echo Downloading 22912
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 22912

echo Downloading 13103
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13103
exit