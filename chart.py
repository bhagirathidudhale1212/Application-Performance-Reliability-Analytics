 Application Performance & Reliability Analytics
--Python Chart Generation

import pandas as pd
import matplotlib.pyplot as plt

--Load application logs
df = pd.read_csv("application_logs.csv", parse_dates=["Timestamp"])


1. Server Errors by Service
server_errors = (
    df[df["Status_Code"] >= 500]
    .groupby("Service")["Request_ID"]
    .count()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
server_errors.plot(kind="bar")
plt.title("Server Errors by Service")
plt.xlabel("Service")
plt.ylabel("Server Errors")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("server_errors_by_service.png", dpi=300)
plt.show()


 2. Average Latency by Service
avg_latency = (
    df.groupby("Service")["Latency_ms"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
avg_latency.plot(kind="bar")
plt.title("Average Latency by Service")
plt.xlabel("Service")
plt.ylabel("Average Latency (ms)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_latency_by_service.png", dpi=300)
plt.show()


3. Error Rate by Service
error_rate = (
    df.groupby("Service")["Status_Code"]
    .apply(lambda x: (x >= 400).mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
error_rate.plot(kind="bar")
plt.title("Error Rate by Service")
plt.xlabel("Service")
plt.ylabel("Error Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("error_rate_by_service.png", dpi=300)
plt.show()

print("Charts generated successfully.")