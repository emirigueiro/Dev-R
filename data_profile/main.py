import pandas as pd
from prettytable import PrettyTable

import id_f as id_f
import email_f as email_f
import primary_f as primary_f


def profile_date (x):

    profile_date =                     pd.DataFrame(columns=['columns'])
    profile_date['columns'] =          pd.Series(primary_f.column_list(x))
    profile_date['count'] =            pd.Series(primary_f.r_count(x))
    profile_date['unique'] =           pd.Series(primary_f.r_count_distinct(x))
    profile_date['unique_%'] =         pd.Series(primary_f.r_count_distinct_percent(x))
    profile_date['id_probabilty'] =    pd.Series(id_f.id_probability(x))
    profile_date['email_probabilty'] = pd.Series(email_f.email_probability(x))
    profile_date['duplicate'] =        profile_date['count'] - profile_date['unique']
    profile_date['numeric'] =          pd.Series(primary_f.is_numeric(x))
    profile_date['letter'] =           pd.Series(primary_f.is_letter(x))
    profile_date['bool'] =             pd.Series(primary_f.is_bool(x))
    profile_date['empty'] =            pd.Series(primary_f.r_empty(x))
    profile_date['empty_%'] =          pd.Series(primary_f.empty_percent(x))
    profile_date['cero'] =             pd.Series(primary_f.r_cero(x))
    profile_date['cero_%'] =           pd.Series(primary_f.r_cero_percent(x))
    profile_date['null'] =             pd.Series(primary_f.is_null(x))
    profile_date['null_%'] =           pd.Series(primary_f.is_null_percent(x))

    x = PrettyTable()
    x.field_names = profile_date.columns.tolist()
    for row in profile_date.itertuples(index=False):
        x.add_row(row)

    return x