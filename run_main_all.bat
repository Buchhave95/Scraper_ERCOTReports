echo off

cd /D "%~dp0"
echo Downloading 13499
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13499

echo Downloading 15933
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 15933

echo Downloading 13028
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13028

echo Downloading 14787
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 14787

echo Downloading 13483
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13483

echo Downloading 21809
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 21809

echo Downloading 22912
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 22912

echo Downloading 13103
py -3.12 -m poetry run .\.venv\Scripts\python.exe Scraper_ERCOTReports\__main__.py -id 13103
exit