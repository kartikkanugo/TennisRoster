import pandas as pd
from .. import error
from itertools import zip_longest, tee
import random


def read_excel(excel_file):
    """

    :rtype: dataframe
    """
    try:
        df = pd.read_excel(excel_file)
    except:
        error.InputError("The input file is not correct excel format")
    return df


def create_matchups(pairs):
    length = len(pairs)
    if length % 2 != 0:
        pairs.append(pairs[0])

    list_pair = list()
    match_list = list()
    for i in pairs:
        list_pair.append(i)
        if len(list_pair) == 2:
            match_list.append(list_pair)
            list_pair = list()

    return match_list


def create_pairs(df, opts):
    list_pro = list(df['Pros'])
    list_nov = list(df['Novice'])
    if pd.isnull(list_nov).any():
        list_without_nan = [x for x in list_nov if pd.isnull(x) == False]
        if opts == 1:
            random.shuffle(list_without_nan)
            random.shuffle(list_pro)

        for i in range(len(list_pro) - len(list_without_nan)):
            list_without_nan.append(list_without_nan[i])

        list_nov = list_without_nan
    else:
        list_without_nan = [x for x in list_pro if pd.isnull(x) == False]
        if opts == 1:
            random.shuffle(list_without_nan)
            random.shuffle(list_nov)

        for i in range(len(list_nov) - len(list_without_nan)):
            list_without_nan.append(list_without_nan[i])

        list_pro = list_without_nan

    allpairs = list(zip_longest(list_pro, list_nov, fillvalue='-'))

    return allpairs
