
class ReportsToDownload():
    def __init__(self) -> None:
        self.Reports = {
            '13499': {
                'HourlyRTLoad': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'GEN-55-CD'
                }
            },
            '15933': {
                'GISReport': {
                    'FileFormat': 'xlsx',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': False,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'PG7-200-ER'
                }
            },
            '16554': {
                'IntraHourWindForecastByGeoRegion': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-751-CD'
                }
            },
            '21812': {
                'IntraHourSolarForecastByGeoRegion': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-752-CD'
                }
            },
            '22912': {
                'UnplannedResourceOutagesReport': {
                    'FileFormat': 'zip',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP1-346-ER'
                }
            },
            '13103': {
                'HourlyResourceOutageCapacity': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP3-233-CD'
                }
            },
        }