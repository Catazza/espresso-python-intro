import pandas as pd
from src.datamanipulation.data_preprocessing import identify_quant_cols


def test_identify_quant_cols():
    dummy_df = pd.DataFrame({
        'col1': [1,2,3],
        'col2': ['as', 3 ,'test'],
        'col3': [4.4, 5.3, 2.0]
    })

    quant_cols = identify_quant_cols(dummy_df)
    assert quant_cols == ['col1', 'col3']