import json
from . import resources


class Context:
    def __init__(self, file):
        self._ctx = file

    def load_input_data(self, excel_file):
        """ The function will load the input data from the excel file to the context json file
        If the context is not empty it will generate and error"""
        resources.inputdata.InputData(excel_file)



