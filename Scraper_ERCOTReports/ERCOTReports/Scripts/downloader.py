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

def downloader_archived_files_public_api(default_variables, dct_report_specs:dict, report, report_name:str, report_id:str) -> None:
    import os
    import re
    import json
    import time
    import datetime as dt
    import requests
    import pandas as pd

    from Utils.scrapers import UtilScraper
    import Scraper_ERCOTReports.ERCOTReports.Scripts.helper_functions as hf

    token = hf.get_token_public_api(default_variables)
    dct_headers = {
        'Authorization': f"Bearer {token}",
        'Ocp-Apim-Subscription-Key': default_variables.SUBSCRIPTION_KEY
    }

    get_more_data = True
    str_start_date = '2018-01-01T00:00:00'
    output_folder = default_variables.OUTPUT_FOLDER + report_name
    while get_more_data == True:
        dct_params = {
            'sort': 'postDatetime',
            'postDatetimeFrom': str_start_date
        }

        url = f"{default_variables.API_URL_ARCHIVE}/{dct_report_specs['EMILID']}"
        count = 0
        while count < 3:
            try:
                resp = requests.get(url, headers = dct_headers, params = dct_params)
                df_data = pd.DataFrame(resp.json()['archives'])
                break
                
            except Exception as err:
                print(str(err))
                print(f"Retry: {count}")
                count += 1
                time.sleep(2)

        filename = str_start_date.split('.')[0]
        str_start_date = df_data['postDatetime'].max()
        filename += '_' + str_start_date.split('.')[0]
        df_data.to_csv(f"{output_folder}\\ExtendedHistory\\{re.sub('[:-]', '', filename)}.csv", index = False)

        if resp.json()['_meta']['currentPage'] == resp.json()['_meta']['totalPages']:
            get_more_data = False

    print('Done getting all archived reports')