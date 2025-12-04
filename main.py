
from pandas import read_json

from utils import Creating_new_columns, changes_existing_columns, filter_rows, saving_to_CSV


df = read_json()

changes_existing_columns(df)

Creating_new_columns(df)

filter_rows(df)

saving_to_CSV(df)





