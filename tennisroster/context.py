import os
from .resources import combinations
from . import error


class Context:
    """ The context class must be initialised with the contexts json file. The context will be used for all the
    functions to check loading data, flowcharts etc.
    """

    def __init__(self, file: str):
        self.matches = None
        self.pairs = None
        self.df = None
        if self._check_compatibility(file):
            self.ctx = file
            # Initialise the json context by writing suitable things
        else:
            self.ctx = None
            raise error.InputError("Json file is not empty or Incompatible. Initialisation failed")

    def load_input_data(self, excel_file, opts):
        """ The function will load the input data from the excel file to the context json file
        If the context is not empty it will generate and error"""

        self.df = combinations.read_excel(excel_file)
        self.pairs = combinations.create_pairs(self.df, opts)
        return self.pairs

    def create_matchups(self):
        self.matches = combinations.create_matchups(self.pairs)
        return self.matches

    def produce_flowchart(self):
        pass

    @staticmethod
    def _check_compatibility(path_of_file):
        # Checking if file exist and it is empty
        if os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0:
            return True
        ## Check the compatibility with the file

        return False
