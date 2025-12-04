import pandas as pd
def read_json():
    df = pd.read_json('orders_simple.json', orient="records")
    return df

def changes_existing_columns(df):
    df['total_amount'] = df['total_amount'].str.replace('$', '', regex=False)
    df = df.astype({"total_amount": "float","shipping_days": "int64","customer_age": "int64"})
    df["order_date"] = pd.to_datetime(df["order_date"]) 


    df['items_html'] = df['items_html'].str.replace('<[^<]+?>', '', regex=True)

    df['coupon_used'] = df['coupon_used'].replace('','no_coupon').fillna('no_coupon')

    return df


def Creating_new_columns(df):
    df['order_month']=df['order_date'].dt.month
    average_amount = df['total_amount'].mean()
    df['high_value_order'] = df['total_amount'] > average_amount
    df = df.sort_values(by='total_amount', ascending=False)
    df['average_rating']=df.groupby('country')['rating'].transform("mean")
    df['delivery_status'] = df['shipping_days'].apply(lambda x: 'delayed' if x > 7 else 'on_time')
    return df

def filter_rows(df):
    df = df.query("total_amount > 1000 and rating >4.5")
    return df


def saving_to_CSV(df):   
    df.to_csv("clean_orders_[eliezer_yakovson_2].csv", index=False, encoding="utf-8-sig")
    return df