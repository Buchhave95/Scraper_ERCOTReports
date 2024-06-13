import Scraper_ERCOTReports.ERCOTReports.Scripts.helper_functions as hf
from Scraper_ERCOTReports.ERCOTReports.Scripts import defaults
from Scraper_ERCOTReports.ERCOTReports.Scripts import reports_to_download
from Scraper_ERCOTReports.ERCOTReports.Scripts import downloader
from Scraper_ERCOTReports.ERCOTReports.Scripts import parser


def run_app(report_id:str):
    default_variables = defaults.DefaultVariables(__file__)
    reports_mapping = reports_to_download.ReportsToDownload()
    report = reports_mapping.Reports[report_id]

    for report_name, dct_report_specs in report.items():
        try:
            # downloader.downloader_archived_files_public_api(default_variables, dct_report_specs, report, report_name, report_id)
            downloader.downloader(default_variables, dct_report_specs, report, report_name, report_id)
        except Exception as err:
            print(str(err))

        if dct_report_specs['ParseData']:
            try:
                parser.parser(default_variables, dct_report_specs, report, report_name, report_id)
            except Exception as err:
                print(str(err))