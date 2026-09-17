 Application Performance & Reliability Analytics
--Python Analysis

import pandas as pd

1. Load application logs
df = pd.read_csv("application_logs.csv", parse_dates=["Timestamp"])

2. Data quality checks
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

3. Service performance analysis
service_summary = df.groupby("Service").agg(
    Requests=("Request_ID", "count"),
    Avg_Latency_ms=("Latency_ms", "mean"),
    Error_Rate_pct=("Status_Code", lambda x: (x >= 400).mean() * 100)
).round(2)

print("\nService Performance Summary:")
print(service_summary)

 4. HTTP status code distribution
status_summary = df["Status_Code"].value_counts().sort_index()

print("\nHTTP Status Code Distribution:")
print(status_summary)

 5. Server errors by service
server_errors = (
    df[df["Status_Code"] >= 500]
    .groupby("Service")
    .agg(
        Server_Errors=("Request_ID", "count"),
        Avg_Latency_ms=("Latency_ms", "mean")
    )
    .round(2)
    .sort_values("Server_Errors", ascending=False)
)

print("\nServer Errors by Service:")
print(server_errors)

 6. Regional performance
region_summary = df.groupby("Region").agg(
    Requests=("Request_ID", "count"),
    Avg_Latency_ms=("Latency_ms", "mean")
).round(2)

print("\nRegional Performance:")
print(region_summary)

 7. Slowest services
slowest_services = (
    df.groupby("Service")["Latency_ms"]
    .max()
    .sort_values(ascending=False)
)

print("\nMaximum Latency by Service:")
print(slowest_services)

 8. Environment comparison
environment_summary = df.groupby("Environment").agg(
    Requests=("Request_ID", "count"),
    Avg_Latency_ms=("Latency_ms", "mean"),
    Error_Rate_pct=("Status_Code", lambda x: (x >= 400).mean() * 100)
).round(2)

print("\nEnvironment Performance:")
print(environment_summary)