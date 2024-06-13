import os
import json
import time
import requests
import datetime as dt
import pandas as pd
from zipfile import ZipFile

from Utils.logging import Logging


def download_file_json_format(log_file_path:str, output_folder:str, report_name:str, dct_report_specs:dict, default_variables, util_scraper) -> None:
    logging = Logging()

    # Reading json data file
    with open(f"{output_folder}\\{report_name}.{dct_report_specs['DataFileFormat']}") as raw_data:
        data = json.load(raw_data)
        raw_data.close()
    df_data = pd.json_normalize(data['ListDocsByRptTypeRes']['DocumentList'])

    for idx, row in df_data[(df_data['Document.FriendlyName'].str.contains(dct_report_specs['FileFormat'])) | \
                            (df_data['Document.Extension'].str.contains(dct_report_specs['FileFormat']))].iterrows():
        
        df_log = pd.read_csv(log_file_path)

        # Checking for already downloaded file
        download_url = default_variables.DOWNLOAD_URL_DOC_ID.format(row['Document.DocID'])
        if not df_log[df_log['DownloadURL'] == download_url].empty:
            continue

        # Setting input variables
        dt_file_date = pd.to_datetime(row['Document.PublishDate'], utc = True)
        file_date = dt_file_date.strftime('%d-%m-%Y %H:%M:%S.%f%z')
        output_folder_sub_folder = output_folder + '\\' + str(dt_file_date.year)
        if not os.path.exists(output_folder_sub_folder): os.mkdir(output_folder_sub_folder)
        raw_filename = row['Document.ConstructedName']
        filename = raw_filename

        # Downloading file
        print(f"Downloading {raw_filename}")
        util_scraper.py_get_file_from_url(download_url, f"{output_folder_sub_folder}\\{raw_filename}")

        # Unziping 
        if dct_report_specs['UnZipFiles']:
            with ZipFile(f"{output_folder_sub_folder}\\{raw_filename}", 'r') as obj:
                obj.extractall(output_folder_sub_folder)
                time.sleep(2)
                filename = obj.filelist[0].filename
            obj.close()

        # Writing to log
        df_log = pd.DataFrame({
            'DownloadedDateTime': dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'FileDate': file_date,
            'OutputPath': output_folder_sub_folder,
            'Filename': filename,
            'DownloadURL': download_url
        }, index = [0])
        logging.write_log_from_dataframe_csv(log_file_path, df_log, 3)

def get_token_public_api(default_variables) -> str:
    # Get new token id
    dct_params = {
        'username': 'cbucjensen@gmail.com',
        'password': 'tPkz73d6kX3QkNx',
        'grant_type': 'password',
        'scope': "openid+fec253ea-0d06-4272-a5e6-b478baeecd70+offline_access",
        'client_id': "fec253ea-0d06-4272-a5e6-b478baeecd70",
        'response_type': 'id_token'
    }
    
    url_token = default_variables.TOKEN_URL + '?'
    for k in dct_params.keys():
        url_token += f"{k}={dct_params[k]}&"
    url_token = url_token[:-1]

    resp = requests.post(url_token)
    token = resp.json()['id_token']

    return token