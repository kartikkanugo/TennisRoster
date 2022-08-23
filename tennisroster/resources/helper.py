import json
from .. import error

INITIALISE_DICT = {"TennisRoster": []
                   }


def check_file_compatibility(path_to_file):
    f = open(path_to_file, 'r+')
    file_data = json.load(f)
    f.close()
    if "TennisRoster" in file_data:
        return True
    return False


def initialise_json(path_to_file):
    f = open(path_to_file, 'r+')
    json.dump(INITIALISE_DICT, f, indent=4)
    f.close()


def add_dict_to_json(path_to_file, match_list, points_list, sub_pts_list, win_loss_list, round_num=-1):
    if len(match_list) != len(points_list) != len(sub_pts_list):
        raise error.InputError("Lengths of the match list, points list and sub_pts_list are not equal")
    round_dict = {"Teams": match_list,
                  "Points": points_list,
                  "Sub_pts": sub_pts_list,
                  "Win_loss": win_loss_list
                  }
    f = open(path_to_file, 'r+')
    file_data = json.load(f)
    if round_num == -1:
        file_data["TennisRoster"].append(round_dict)
    else:
        file_data["TennisRoster"][round_num] = round_dict

    f.seek(0)
    json.dump(file_data, f, indent=4)
    f.close()


def get_match_list(path_to_file, round_num):
    f = open(path_to_file, 'r+')
    file_data = json.load(f)
    f.close()
    if len(file_data["TennisRoster"]) > round_num >= 0:
        match_list = file_data["TennisRoster"][round_num]["Teams"]
    else:
        error.InputError("Round number is invalid")

    return match_list
