import pandas as pd


class ResultGenerator:
    def __init__(self, dict_list):
        self.dict_list = dict_list
        self.all_rounds = None
        self.res_name_dict = {
            "Name": None,
            "Num_Matches": None
        }
        self.res_round = {}
        self.names = None
        self.num_matches = None
        self.win_loss_score = None
        self.total_score = None

    def generate_result_round(self, round_num):
        self.all_rounds = None
        scores = 'score_' + str(round_num)
        sub_score = 'sub_score_' + str(round_num)
        win_loss_score = 'win_loss_score_' + str(round_num)
        self._generate_result_file(scores, sub_score, win_loss_score, round_num)

    def generate_result_all(self):
        self.all_rounds = 1
        self._generate_result_file()

    def _generate_result_file(self, score_name, sub_score_name, win_loss_score_name, round_num):
        self.res_round[score_name] = None
        self.res_round[sub_score_name] = None
        self.res_round[win_loss_score_name] = None
        # if self.allrounds is active check names for individual rounds and then append num matches, and scores in
        # the big list else --- only check in the names and igore
        if self.names is not None:
            pass # check for new names and append
        else:
            pass

