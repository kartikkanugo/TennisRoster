import pandas as pd
from enum import Enum, unique
from dataclasses import dataclass


@unique
class RoundCheck(Enum):
    SINGLE_ROUND = 1
    ALL_ROUNDS = 2


@dataclass()
class GenData:
    pass


class ResultGenerator:
    def __init__(self, dict_list):
        self.dict_list = dict_list
        self.all_rounds = None
        self.res_name_dict = {
            "Name": None,
            "Num_Matches": None
        }
        self.pres_round = {}
        self.nres_round = {}
        self.pro_names = None
        self.nov_names = None
        self.pro_num_matches = None
        self.nov_num_matches = None
        self.win_loss_score = None
        self.total_score = None

    def generate_result_round(self, round_num):
        self.all_rounds = None
        scores = 'score_' + str(round_num + 1)
        sub_score = 'sub_score_' + str(round_num + 1)
        win_loss_score = 'win_loss_score_' + str(round_num + 1)
        self._generate_result_file(scores, sub_score, win_loss_score, round_num)

    def generate_result_all(self):
        self.all_rounds = 1
        self._generate_result_file()

    def _generate_result_file(self, score_name, sub_score_name, win_loss_score_name, round_num):
        self.pres_round[score_name] = []
        self.pres_round[sub_score_name] = []
        self.pres_round[win_loss_score_name] = []

        self.nres_round[score_name] = []
        self.nres_round[sub_score_name] = []
        self.nres_round[win_loss_score_name] = []

        # if self.allrounds is active check names for individual rounds and then append num matches, and scores in
        # the big list else --- only check in the names and igore
        if self.pro_names is not None or self.nov_names is not None:
            self._check_new_names(round_num)
        else:
            self._load_names(round_num)

        round_list = zip(self.dict_list[round_num]["Teams"], self.dict_list[round_num]["Points"],
                         self.dict_list[round_num]["Sub_pts"], self.dict_list[round_num]["Win_loss"])
        for teams, pts, s_pts, wl in round_list:
            pro_index = self.pro_names.index(teams[0])
            self.res_round[pro_index] = self.pro_num_matches[pro_index] + 1

    def _load_names(self, round_num):
        self.pro_names = []
        self.nov_names = []
        self.pro_num_matches = []
        self.nov_num_matches = []
        for teams in self.dict_list[round_num]["Teams"]:
            self.pro_names.append(teams[0][0])
            self.nov_names.append(teams[0][1])
            self.pro_num_matches.append(1)
            self.nov_num_matches.append(1)

            self.pro_names.append(teams[1][0])
            self.nov_names.append(teams[1][1])
            self.pro_num_matches.append(1)
            self.nov_num_matches.append(1)

    def _check_new_names(self, round_num):
        for teams in self.dict_list[round_num]["Teams"]:
            if teams[0][0] not in self.pro_names:
                self.pro_names.append(teams[0][0])
            if teams[0][1] not in self.nov_names:
                self.nov_names.append(teams[0][1])
            if teams[1][0] not in self.pro_names:
                self.pro_names.append(teams[1][0])
            if teams[1][1] not in self.nov_names:
                self.nov_names.append(teams[1][1])

        for teams in self.dict_list[round_num]["Teams"]:
            pro_index = self.pro_names.index(teams[0][0])
            self.pro_num_matches[pro_index] = self.pro_num_matches[pro_index] + 1
            pro_index = self.pro_names.index(teams[1][0])
            self.pro_num_matches[pro_index] = self.pro_num_matches[pro_index] + 1

            nov_index = self.nov_names.index(teams[0][1])
            self.nov_num_matches[nov_index] = self.nov_num_matches[nov_index] + 1
            nov_index = self.nov_names.index(teams[1][1])
            self.nov_num_matches[nov_index] = self.nov_num_matches[nov_index] + 1
