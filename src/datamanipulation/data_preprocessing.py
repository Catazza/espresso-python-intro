import numpy as np


def identify_quant_cols(df):
    return list(df.select_dtypes(include=[np.number]).columns.values)


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


