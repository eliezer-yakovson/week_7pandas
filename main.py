

from utils import read_json,Creating_new_columns, changes_existing_columns, filter_rows, saving_to_CSV


df = read_json()

df = changes_existing_columns(df)

df = Creating_new_columns(df)

df = filter_rows(df)
df = saving_to_CSV(df)




