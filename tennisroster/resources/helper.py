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


def _check_win_loss_list(win_loss_list, sub_pts_list):
    wl_check = {'D', 'L', 'W'}
    sub_check = {0, 15, 30, 40}
    for i, ii in win_loss_list, sub_pts_list:
        for j, jj in i, ii:
            if j not in wl_check or jj not in sub_check:
                return False
    return True


def _check_if_win_matches_pts(points_list, sub_pts_list, win_loss_list):
    for i, ii, iii in win_loss_list, points_list, sub_pts_list:
        if i[0] == 'W':
            if not (ii[0] > ii[1] or (ii[0] == i[1] and iii[0] > iii[1])):
                return False
        elif i[0] == 'L':
            if not (ii[0] < ii[1] or (ii[0] == i[1] and iii[0] < iii[1])):
                return False
        else:
            if not (ii[0] == ii[1] and iii[0] == iii[1]):
                return False
    return True


def add_dict_to_json(path_to_file, match_list, points_list, sub_pts_list, win_loss_list, round_num=-1):
    if len(match_list) != len(points_list) != len(sub_pts_list) != len(win_loss_list):
        raise error.InputError("Lengths of the match list, points list ,sub_pts_list and win_loss_list are not equal")

    if not _check_win_loss_list(win_loss_list, sub_pts_list):
        raise error.InputError("Win loss list or sub_pts_list consists of other than (D L W) or (0 15 30 40)")

    if not _check_if_win_matches_pts(points_list, sub_pts_list, win_loss_list):
        raise error.InputError("Win or loss condition does not match the points list")

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
