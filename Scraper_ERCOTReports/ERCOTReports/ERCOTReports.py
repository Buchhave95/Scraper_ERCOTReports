import os
import json
import datetime as dt
import pandas as pd

import Scraper_ERCOTReports.ERCOTReports.Scripts.helper_functions as hf
from Scraper_ERCOTReports.ERCOTReports.Scripts import defaults
from Scraper_ERCOTReports.ERCOTReports.Scripts import reports_to_download
from Utils.scrapers import UtilScraper

def run_app(report_id:str):
    default_variables = defaults.DefaultVariables(__file__)
    reports_mapping = reports_to_download.ReportsToDownload()

    report = reports_mapping.Reports[report_id]
    report_url = default_variables.BASE_URL.format(report_id)

    for report_name, dct_report_specs in report.items():
        # Setting paths
        output_folder = default_variables.OUTPUT_FOLDER + report_name
        log_file_path = default_variables.OUTPUT_FOLDER + report_name + '\\downloader.csv'

        # Creating folder\file paths
        if not os.path.exists(output_folder): os.mkdir(output_folder)
        if not os.path.exists(log_file_path): pd.DataFrame(default_variables.DCT_LOG_CONTENT, index = [0]).to_csv(log_file_path, index = False)

        # Scraping files
        util_scraper = UtilScraper()
        util_scraper.py_get_html_to_file_requests(report_url, f"{output_folder}\\{report_name}.{dct_report_specs['DataFileFormat']}")

        if dct_report_specs['DataFileFormat'].lower() == 'json':
            hf.download_file_json_format(log_file_path, output_folder, report_name, dct_report_specs, default_variables, util_scraper)