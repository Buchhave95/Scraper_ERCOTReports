
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

            '13028': {
                'WindHourlyActualAndForecast': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-732-CD'
                }
            },

            '14787': {
                'WindHourlyActualAndForecastGeoRegional': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-742-CD'
                }
            },

            '13483': {
                'SolarHourlyActualAndForecast': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-737-CD'
                }
            },

            '21809': {
                'WindHourlyActualAndForecastGeoRegional': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-745-CD'
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

            '12331': {
                '15MinRTSettlementLMP': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP4-190-CD'
                }
            },

            '12301': {
                'DAMSettlementLMP': {
                    'FileFormat': 'csv',
                    'DateSlicer': slice(3, 4),
                    'DateFormat': '',
                    'UnZipFiles': True,
                    'ParseData': False,
                    'TableName': False,
                    'FileNamePrefix': slice(3, 5),
                    'DataFileFormat': 'json',
                    'EMILID': 'NP6-905-CD'
                }
            },
        }