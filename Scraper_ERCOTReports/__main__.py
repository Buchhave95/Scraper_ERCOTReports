import sys
import argparse
from Scraper_ERCOTReports.ERCOTReports.ERCOTReports import run_app
from Scraper_ERCOTReports.ERCOTReports.Scripts import defaults
from Scraper_ERCOTReports.ERCOTReports.Scripts import reports_to_download

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-id', '--reportid', type = str, default = False, required = True)

#     if len(sys.argv) > 1:
#         args = parser.parse_args()
#         report_id = args.reportid
#     else:
#         report_id = '13028'

#     run_app(report_id)

if __name__ == '__main__':
    default_variables = defaults.DefaultVariables(__file__)
    reports_mapping = reports_to_download.ReportsToDownload()

    for report_id in reports_mapping.Reports.keys():
        run_app(report_id)
