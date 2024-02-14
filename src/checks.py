import pandas as pd

def print_limit_raw_values(df):
    """ Išrikiavus reikšmes kaip strings, išspausdinamos kraštutinės jų reikšmės.
        Taip tikimasi pagauti 'kreivas' reikšmes kraštuose.
    """
    for col in df.columns:
        str_col = set(df[col].astype(str))
        sorted_list = sorted(str_col)

        if len(sorted_list) >= 4:
            print(f"{col:18}\t{sorted_list[:2]} - {sorted_list[-2:]}")
        else:
            print(f"{col:18}\t{sorted_list}")


def check_missing_values(df):
    """ Suskaičiuojamos trūkstamos reikšmės.
    """
    missing_res_df = pd.DataFrame(columns=['column', 'num_missing', 'perc_missing', 'num_unknown', 'perc_unknown'])
    for col in df.columns:
        num_na = df[col].isna().sum()
        num_unknown = len(df[df[col].astype(str).str.lower() == 'unknown'])
        if num_na > 0 or num_unknown > 0:
            missing_res_df.loc[len(missing_res_df)] = [col,num_na,round(num_na/len(df),4),num_unknown,round(num_unknown/len(df),4)]
    return missing_res_df