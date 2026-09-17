import pandas as pd
df=pd.read_csv('application_logs.csv',parse_dates=['Timestamp'])
print(df.groupby('Service').agg(Requests=('Request_ID','count'),
Avg_Latency_ms=('Latency_ms','mean'),
Error_Rate_pct=('Status_Code',lambda x:(x>=500).mean()*100)).round(2))
