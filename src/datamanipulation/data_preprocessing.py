import math
import numpy as np
import pandas as pd
from functools import partial
import copy
from scipy.stats.mstats import winsorize
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


def identify_quant_cols(df):
    return list(df.select_dtypes(include=[np.number]).columns.values)


def identify_outliers_std_any(data_to_treat, threshold=3, cols_to_consider=None):
    return identify_outliers_std(data_to_treat, threshold, cols_to_consider).any(axis=1)


def identify_outliers_std_all(data_to_treat, threshold=3, cols_to_consider=None):
    return identify_outliers_std(data_to_treat, threshold, cols_to_consider).all(axis=1)


def identify_outliers_std(data_to_treat, threshold=3, cols_to_consider=None):
    if cols_to_consider is None:
        cols_to_consider = data_to_treat.columns.tolist()
    return data_to_treat[cols_to_consider].apply(lambda x: np.abs(x - x.mean()) / x.std() > threshold)


def drop_outlier_std(data_to_treat, method, threshold=3, cols_to_consider=None):
    if method == 'any':
        mask_exclude = identify_outliers_std_any(data_to_treat, threshold, cols_to_consider)
    elif method == 'all':
        mask_exclude = identify_outliers_std_all(data_to_treat, threshold, cols_to_consider)
    else:
        raise ValueError('Must provide a valid outlier removal method. You provided: {}'.format(str(method)))
    mask_include = ~mask_exclude
    return data_to_treat[mask_include]


def log_transform(data, min_positive_value=0.0001):
    positive_data = make_positive(data=data, min_positive_value=min_positive_value)
    return np.log(positive_data)


def make_positive(data, min_positive_value):
    return data.apply(lambda col: make_col_positive(col, min_positive_value), axis=0)


def make_col_positive(col, min_positive_value):
    min_value = min(col)
    if min_value <= 0:
        return col - min_value + min_positive_value
    else:
        return col


