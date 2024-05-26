import os

class DefaultVariables():
    def __init__(self, file:str) -> None:
        self.PS_FILEPATH = os.path.dirname(file) + '\\Scripts\\DownloadHTML.ps1'
        self.OUTPUT_FOLDER = ''


        self.BASE_URL = 'https://www.ercot.com/mp/data-products/data-product-details?id={}'

        
