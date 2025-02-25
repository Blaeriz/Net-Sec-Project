import pandas as pd


df = pd.read_csv("processed_ssh_logs.csv")

first = df.iloc[:,0]

first.to_csv("first_column.csv",index=False,header=True)

print("[+] Timestamp Column has been saved")


