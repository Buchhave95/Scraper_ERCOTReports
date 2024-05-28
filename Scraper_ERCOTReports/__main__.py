import sys
import argparse
from ERCOTReports.ERCOTReports import run_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--reportid', type = str, default = False, required = True)

    if len(sys.argv) > 1:
        args = parser.parse_args()
        report_id = args.reportid
    else:
        report_id = None

    run_app(report_id)