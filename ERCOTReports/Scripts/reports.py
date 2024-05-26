
class ReportsToDownload():
    def __init__(self) -> None:
        self.Reports = {
            'GEN-55-CD': {
                'HourlyRTLoad': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': False,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5)
                }
            },
            'PG7-200-ER': {
                'GISReport': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': False,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5)
                }
            },
            'NP4-751-CD': {
                'IntraHourWindForecastByGeoRegion': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': False,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5)
                }
            },
            'NP4-752-CD': {
                'IntraHourSolarForecastByGeoRegion': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': False,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5)
                }
            },
        }