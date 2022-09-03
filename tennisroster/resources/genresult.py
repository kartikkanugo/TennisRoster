import pandas as pd
from enum import Enum, unique
from dataclasses import dataclass, asdict, field
from datetime import datetime


@unique
class ProNovCheck(Enum):
    PRO = 1
    NOV = 2


@dataclass()
class SingleRoundData:
    names: list[str]
    scores: list[float]
    sub_scores: list[float]
    win_loss: list[str]
    round_num: int


@dataclass()
class AllRoundData:
    names: list[str]
    num_matches: list[int]


def create_result_file_single(single_obj, pro_nov_chk, round_num):
    df = pd.DataFrame(asdict(single_obj))
    if pro_nov_chk == ProNovCheck.PRO:
        datatype = '_Pro'
    else:
        datatype = '_Nov'
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M")
    result_data = dt_string + "_Result_" + str(round_num + 1) + datatype + ".xlsx"
    df.to_excel(result_data, merge_cells=False, index=False)


class ResultGenerator:
    def __init__(self, dict_list):
        self.dict_list = dict_list

    def generate_result_file(self, round_num=None):
        if round_num is not None:
            [pro_obj, nov_obj] = self._generate_result_obj_single(round_num)
            create_result_file_single(pro_obj, ProNovCheck.PRO, round_num)
            create_result_file_single(nov_obj, ProNovCheck.NOV, round_num)
        else:
            all_pro_data: list[SingleRoundData] = []
            all_nov_data: list[SingleRoundData] = []
            total_rounds = len(self.dict_list)
            for i in range(total_rounds + 1):
                [pro_obj, nov_obj] = self._generate_result_obj_single(i)
                all_pro_data.append(pro_obj)
                all_nov_data.append(nov_obj)

            all_pro_obj = self._generate_result_obj(all_pro_data)
            all_nov_obj = self._generate_result_obj(all_nov_data)
            # todo

    def _generate_result_obj(self, all_pro_data) -> AllRoundData:
        pass

    def _generate_result_obj_single(self, round_num) -> list[SingleRoundData]:
        [pro_names, pro_scores, pro_sub_scores, pro_win_loss] = self._get_data_lists(self.dict_list[round_num]["Teams"],
                                                                                     self.dict_list[round_num][
                                                                                         "Points"],
                                                                                     self.dict_list[round_num][
                                                                                         "Sub_pts"],
                                                                                     self.dict_list[round_num][
                                                                                         "Win_loss"],
                                                                                     ProNovCheck.PRO)
        [nov_names, nov_scores, nov_sub_scores, nov_win_loss] = self._get_data_lists(self.dict_list[round_num]["Teams"],
                                                                                     self.dict_list[round_num][
                                                                                         "Points"],
                                                                                     self.dict_list[round_num][
                                                                                         "Sub_pts"],
                                                                                     self.dict_list[round_num][
                                                                                         "Win_loss"],
                                                                                     ProNovCheck.NOV)

        pro_obj = SingleRoundData(pro_names, pro_scores, pro_sub_scores, pro_win_loss, round_num)
        nov_obj = SingleRoundData(nov_names, nov_scores, nov_sub_scores, nov_win_loss, round_num)

        return [pro_obj, nov_obj]

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

    @staticmethod
    def _get_data_lists(names_list, pts_list, sub_pts_list, win_loss_list, pro_nov_chk) -> list:
        res_names = []
        res_pts = []
        res_sub_pts = []
        res_win_loss = []
        if pro_nov_chk == ProNovCheck.PRO:
            idx = 0
        else:
            idx = 1

        for teams, pts, sub_pts, win_loss in zip(names_list, pts_list, sub_pts_list, win_loss_list):
            res_names.append(teams[0][idx])
            res_pts.append(pts[0])
            res_sub_pts.append(sub_pts[0])
            res_win_loss.append(win_loss[0])

            res_names.append(teams[1][idx])
            res_pts.append(pts[1])
            res_sub_pts.append(sub_pts[1])
            res_win_loss.append(win_loss[1])

        return [res_names, res_pts, res_sub_pts, res_win_loss]

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
