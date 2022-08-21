from ..context import Context
import pandas as pd
from .. import error


class InputData(Context):
    """ Class will Verify if the context json file matches the input excel file
    If the json file is empty then we load the excel file in the json file"""

    def __init__(self, excel_file, json_file):
        """

        :rtype: object
        """
        df = pd.read_excel(excel_file)
        # check if df already is in the json ctx
        if self._check_ctx(df):
            raise error.InputError("Json file attributes donot match with input excel file")

    @staticmethod
    def _check_ctx(df):
        return False
