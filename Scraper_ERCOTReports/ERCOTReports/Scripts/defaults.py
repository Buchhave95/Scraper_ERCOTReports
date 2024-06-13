import os

class DefaultVariables():
    def __init__(self, file:str) -> None:
        self.OUTPUT_FOLDER = 'C:\\Users\\cbucj\\Dropbox\\Data\\'
        self.EMIL_URL = 'https://www.ercot.com/mp/data-products/data-product-details?id={}'
        self.BASE_URL = 'https://www.ercot.com/misapp/servlets/IceDocListJsonWS?reportTypeId={}'
        self.DOWNLOAD_URL_DOC_ID = 'https://www.ercot.com/misdownload/servlets/mirDownload?doclookupId={}'
        
        # URLs related to public API for both latest and archive
        self.TOKEN_URL = 'https://ercotb2c.b2clogin.com/ercotb2c.onmicrosoft.com/B2C_1_PUBAPI-ROPC-FLOW/oauth2/v2.0/token'
        self.API_URL = 'https://api.ercot.com/api/public-reports'
        self.API_URL_ARCHIVE = 'https://api.ercot.com/api/public-reports/archive/'
        self.SUBSCRIPTION_KEY = 'b64da907580e4c77b19435d2c6b37a3c'

        # Default format for log
        self.DCT_LOG_CONTENT = {
            'DownloadedDateTime': None,
            'FileDate': None,
            'OutputPath': None,
            'Filename': None,
            'DownloadURL': None
        }