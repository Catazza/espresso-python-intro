import os
from sklearn import preprocessing
from src.datamanipulation.data_preprocessing import *
from src.logexception.logframework import *
from src.logexception.exceptionhandler import *

logger = logging.getLogger(__name__)
LoggerInitialiser(conf_method='yaml', conf_path=os.path.join(os.path.dirname(__file__),
                                                             '..', 'logexception', 'config', 'log_config.yaml'))


@func_exec_logger(logger)
@exception_handler(exc_type=(TypeError, ValueError, KeyError), logger=logger, exc_trace=True)
def transform_data(data):
    """
    Function to transform data according to assignment 2.

    :return: None
    """
    # drop column
    data.drop(columns='DAY_OF_WEEK', inplace=True)

    # Rename column
    data.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'}, inplace=True)

    # Split into 4 equal chunks
    list_df = split_df_equal_chunks(data, 4)

    # Concatenate back
    flights_data_conc = pd.concat(list_df, axis=0)

    # Select only for AA
    data_aa = data[data['AIRLINE'] == 'AA']

    # More filtering
    data_filtered = data[(data['DEPARTURE_DELAY'] < 10) & (data['DESTINATION_AIRPORT'] == 'PBI')]

    # Fill blanks with average
    data['AIR_SYSTEM_DELAY'].fillna(data['AIR_SYSTEM_DELAY'].mean(), inplace=True)

    # Has A
    def check_a(element):
        if 'A' in element:
            return 1
        return 0

    data['has_A'] = data['AIRLINE'].apply(check_a)

    # Version with lambda
    # flights_data['has_A'] = flights_data['AIRLINE'].apply(lambda x: 'A' in x)

    # Sample dataframe
    random_sample = sample_dataframe(data, sample_proportion=0.33)

    data['DEPARTURE_DELAY_NORMALISED'] = preprocessing.MinMaxScaler().fit_transform(data[['DEPARTURE_DELAY']])

    return data


if __name__ == "__main__":
    # flights_data = pd.read_csv('./data/flights.csv')
    flights_data = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'flights.csv'))
    transformed = transform_data(flights_data)

