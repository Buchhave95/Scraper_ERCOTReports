def parser(default_variables, dct_report_specs, report, report_name, report_id):
    import os
    import pandas as pd

    # Reading download log
    output_folder = default_variables.OUTPUT_FOLDER + report_name
    download_log_file_path = default_variables.OUTPUT_FOLDER + report_name + '\\downloader.csv'
    df_download_log = pd.read_csv(download_log_file_path, dtype = str)

    # Reading parser log
    parser_log_file_path = default_variables.OUTPUT_FOLDER + report_name + '\\parser.csv'
    if os.path.exists(parser_log_file_path):
        df_parser_log = pd.read_csv(parser_log_file_path)