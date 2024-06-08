def downloader(default_variables, dct_report_specs:dict, report, report_name:str, report_id:str) -> None:
    import os
    import json
    import datetime as dt
    import pandas as pd

    from Utils.scrapers import UtilScraper
    import Scraper_ERCOTReports.ERCOTReports.Scripts.helper_functions as hf

    # Setting paths
    output_folder = default_variables.OUTPUT_FOLDER + report_name
    log_file_path = default_variables.OUTPUT_FOLDER + report_name + '\\downloader.csv'
    print('Downloading ' + report_name)

    # Creating folder\file paths
    if not os.path.exists(output_folder): os.mkdir(output_folder)
    if not os.path.exists(log_file_path): pd.DataFrame(default_variables.DCT_LOG_CONTENT, index = [0]).to_csv(log_file_path, index = False)

    # Scraping files
    report_url = default_variables.BASE_URL.format(report_id)
    util_scraper = UtilScraper()
    util_scraper.py_get_html_to_file_requests(report_url, f"{output_folder}\\{report_name}.{dct_report_specs['DataFileFormat']}")

    if dct_report_specs['DataFileFormat'].lower() == 'json':
        hf.download_file_json_format(log_file_path, output_folder, report_name, dct_report_specs, default_variables, util_scraper)