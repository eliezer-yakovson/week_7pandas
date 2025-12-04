
import pandas as pd
def read_json():
    df = pd.read_json('orders_simple.json', orient="records")
    return df
    
def clean(df):
    df['total_amount'] = df['total_amount'].replace('$', '')
    df = df.astype({"total_amount": "float","shipping_days": "int64","customer_age": "int64"})
    df["order_date"] = pd.to_datetime(df["order_date"]) 
    df['items_html'] =df['items_html'].str.replace('<b>', ' ')
    df['items_html'] =df['items_html'].str.replace('</b>', ' ')

df['coupon_used'] = df['coupon_used'].replace('','no_coupon')

df['order_month']=df['order_date'].dt.month

otal = int(df['total_amount'].mean())

df['high_value_order'] = df['total_amount'].apply(lambda x: True if x > total else False)


df['average_rating']=df.groupby('country')['rating'].transform("mean")
df.head()

filtered = df.query("total_amount > 1000 and rating >4.5")

filtered['delivery_status'] = df['shipping_days'].apply(lambda x: 'delayed' if x > 7 else 'on_time')

filtered.to_csv("clean_orders_[ID_NUMBER].csv", index=False, encoding="utf-8-sig")
