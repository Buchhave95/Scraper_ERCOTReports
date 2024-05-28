import os

class DefaultVariables():
    def __init__(self, file:str) -> None:
        self.OUTPUT_FOLDER = 'C:\\Users\\cbucj\\Dropbox\\Data\\'
        self.EMIL_URL = 'https://www.ercot.com/mp/data-products/data-product-details?id={}'
        self.BASE_URL = 'https://www.ercot.com/misapp/servlets/IceDocListJsonWS?reportTypeId={}'
        self.DOWNLOAD_URL_DOC_ID = 'https://www.ercot.com/misdownload/servlets/mirDownload?doclookupId={}'

        # Default format for log
        self.DCT_LOG_CONTENT = {
            'DownloadedDateTime': None,
            'FileDate': None,
            'OutputPath': None,
            'Filename': None,
            'DownloadURL': None
        }