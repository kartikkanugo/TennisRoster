import os
from .resources import combinations
from . import error
from .resources import helper


class Context:
    """ The context class must be initialised with the contexts json file. The context will be used for all the
    functions to check loading data, flowcharts etc.
    """

    def __init__(self, file: str):
        self.matches = None
        self.pairs = None
        self.df = None
        self.ctx = None
        if self._check_compatibility(file):
            self.ctx = file
        else:
            raise error.InputError("Json file is not empty or Incompatible. Initialisation failed")

    def load_input_data(self, excel_file, opts):
        """ The function will load the input data from the excel file to the context json file
        If the context is not empty it will generate and error"""

        self.df = combinations.read_excel(excel_file)
        self.pairs = combinations.create_pairs(self.df, opts)
        return self.pairs

    def create_matchups(self):
        self.matches = combinations.create_matchups(self.pairs)
        helper.add_dict_to_json(self.ctx, self.matches, [(-1, -1)] * len(self.matches), [(-1, -1)] * len(self.matches))
        return self.matches

    def produce_flowchart(self):
        pass

    def get_match_list(self, round_num):
        return helper.get_match_list(self.ctx, round_num - 1)

    def update_scores(self, round_num, points_list, sub_pts_list):
        helper.add_dict_to_json(self.ctx, self.get_match_list(round_num), points_list, sub_pts_list, round_num - 1)
        pass

    @staticmethod
    def _check_compatibility(path_of_file):
        # Checking if file exist and it is empty
        if os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0:
            helper.initialise_json(path_of_file)
            return True
        if helper.check_file_compatibility(path_of_file):
            return True

        return False
