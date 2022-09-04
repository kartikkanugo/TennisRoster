import pandas as pd
from enum import Enum, unique
from dataclasses import dataclass, asdict, field
from datetime import datetime


@unique
class ProNovCheck(Enum):
    PRO = 1
    NOV = 2


@unique
class PtsWinLoss(Enum):
    WIN = 2
    TIE = 1
    LOSS = 0


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
    tot_pts: list[int]


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

    @staticmethod
    def _generate_result_obj(all_data: list[SingleRoundData]) -> AllRoundData:
        name_list = [all_data[0]['names']]

        for single_data in all_data:
            for i in single_data['names']:
                if i not in name_list:
                    name_list.append(i)  # Load names missing in the list along

        num_matches = [0] * len(name_list)
        tot_wl_pts = [0] * len(name_list)
        tot_scores = [0] * len(name_list)

        for i in range(len(name_list)):
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

