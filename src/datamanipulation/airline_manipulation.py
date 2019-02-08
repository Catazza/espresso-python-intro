import os
from sklearn import preprocessing
import pandas as pd
from src.logexception.logframework import *
from src.datamanipulation.data_preprocessing import make_col_positive

logger = logging.getLogger(__name__)
LoggerInitialiser(conf_method='yaml', conf_path=os.path.join(os.path.dirname(__file__),
                                                             '..', 'logexception', 'config', 'log_config.yaml'))


def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """
    # drop column
    data.drop(columns='DAY_OF_WEEK', inplace=True)

    # Rename column
    data.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'}, inplace=True)

    # Fill blanks with average
    data['AIR_SYSTEM_DELAY'].fillna(data['AIR_SYSTEM_DELAY'].mean(), inplace=True)

    # Scale values to do more analysis
    data['DEPARTURE_DELAY_NORMALISED'] = preprocessing.MinMaxScaler().fit_transform(data[['DEPARTURE_DELAY']])

    # Make column positive
    data['ARRIVAL_DELAY'] = make_col_positive(data['ARRIVAL_DELAY'], 0.001)

    return data


if __name__ == "__main__":
    flights_data = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'flights.csv'))
    transformed = transform_data(flights_data)

