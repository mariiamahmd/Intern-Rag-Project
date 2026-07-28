import pandas as pd

def clean_data():
  df=pd.read_csv("./dataset/Inter_dataset_PII_masked.csv")

  df.columns = df.columns.str.replace('"', '', regex=False) #remove quotes from column names


  df = df.drop("sub_sub_group_category", axis=1) # empty column (no need for it)


  df["approve_date"]=pd.to_datetime(df["approve_date"])
  df["creation_date"]=pd.to_datetime(df["creation_date"])
  df["closed_date"]=pd.to_datetime(df["closed_date"])

  

  df.fillna({
    "item_number": "Unknown",
    "inventory_type": "Unknown",
    "main_category": "Unknown",
    "group_category": "Unknown",
    "sub_group_category": "Unknown",
    "vendor_no" : "Unknown",
    "vendor_name":"Unknown",
    "payment_term":"Unknown",
    "vendor_site_code":"Unknown" }, inplace=True)

  return df