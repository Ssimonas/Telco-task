import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

from src.constants import cols_and_types, CATEGORY_TYPE, NUMERIC_TYPE


def fix_values_and_set_types(source_df):
    """ Įveda trūkstamas reikšmes ir nusato kintamųjų tipus pagal iš anksto numatytus.
    """
    df = source_df.copy()
    for col in df.columns:
        if col not in cols_and_types:
            return str(f"Error: column {col} has no described type in src.constants.py cols_and_types")
        col_type = cols_and_types[col]

        df.loc[df[col].isin(['.', '3000.01.01']), col] = pd.NA
        
        if col_type != NUMERIC_TYPE:
            df[col] = df[col].astype(col_type) # Dates, categoricals, strings 
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def calc_categorical_pair_corr(df, threshold):
    """ Apskaičiuoja koreliaciją tarp 2 kategorinių kintamųjų (Cramer's V).
    """
    col0, col1 = df.columns[0], df.columns[1] 

    contingency_table = pd.crosstab(df[col0], df[col1])
    # Perform the Chi-Square Test of Independence
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Calculate Cramer's V
    n = df.shape[0]  # Total number of observations
    min_dim = min(contingency_table.shape) - 1  # Minimum of the two dimensions of the contingency table minus 1
    cramers_v = np.sqrt(chi2 / (n * min_dim))
    if cramers_v > threshold:
        print(f"{col0} - {col1:28} {cramers_v}")


def print_categorical_correlations(df, threshold):
    """ Išspausdina rezultatą, jeigu koreliacija yra aukštesnė nei 0.8
    """
    cat_cols = [key for key,val in cols_and_types.items() if val == CATEGORY_TYPE]
    print("Cramer's V:")
    for col1 in cat_cols:
        for col2 in cat_cols:
            if (col1 not in df.columns or col2 not in df.columns) or (col1 == col2):
                continue
            calc_categorical_pair_corr(df[[col1, col2]], threshold)