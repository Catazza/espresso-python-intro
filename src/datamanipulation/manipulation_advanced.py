import pandas as pd
import numpy as np
import src.datamanipulation.data_preprocessing as dproc

# Read the dataset in pandas
flight_data = pd.read_csv('../../data/flights.csv')

# Create the route attribute
flight_data['route'] = flight_data['ORIGIN_AIRPORT'] + ' - ' + flight_data['DESTINATION_AIRPORT']

# Exclude outliers column 'departure_delay'
flight_data_outl = dproc.drop_outlier_std(flight_data, 'any', cols_to_consider=['DEPARTURE_DELAY'])

# All quant cols remove outliers - any
flight_data_outl_2 = dproc.drop_outlier_std(flight_data, 'any', cols_to_consider=dproc.identify_quant_cols(flight_data))

# Log transform
log_transformed = dproc.log_transform(flight_data[dproc.identify_quant_cols(flight_data)])

# Merge the datasets
airport_data = pd.read_csv('../../data/airports.csv')
tot_data = flight_data.merge(airport_data, left_on='ORIGIN_AIRPORT', right_on='IATA_CODE')

# Mean delay for each airline
delay_airline = tot_data[['AIRLINE', 'DEPARTURE_DELAY']].groupby('AIRLINE').mean()


# Calculate the number of flights before 12pm
tot_data['is_before_12'] = tot_data['SCHEDULED_DEPARTURE'].apply(lambda x: int(x < 1200))
flights_morning = tot_data[['AIRLINE', 'is_before_12']].groupby('AIRLINE').sum()
flights_day = tot_data[['AIRLINE', 'SCHEDULED_DEPARTURE']].groupby('AIRLINE').count()

merged = flights_morning.merge(flights_day, left_index=True, right_index=True)
merged['proportion_morning'] = merged['is_before_12'] / merged['SCHEDULED_DEPARTURE']


# Pivot table - use pandas pivot_table function, and add a line to calculate percentages row-wise.

print('done')



