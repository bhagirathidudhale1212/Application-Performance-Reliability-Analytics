# Application Performance & Reliability Analytics

## Project Overview

**Application Performance & Reliability Analytics** is an end-to-end data analytics project designed to monitor application performance, identify reliability issues, and analyze service-level behavior.

The project uses **Python, SQL/PostgreSQL, Excel, and Power BI** to transform application log data into meaningful performance insights and interactive dashboards.

## Business Problem

Modern applications generate large volumes of request and performance data. Without proper analysis, it can be difficult to identify:

* High-latency services
* Frequent application errors
* Services with higher error rates
* Regional performance differences
* Production vs. Staging performance
* HTTP status-code patterns
* Application reliability issues

This project analyzes application logs to help monitor these areas and support data-driven performance analysis.

## Objectives

* Analyze application request performance
* Measure service-level latency and error rates
* Identify server-error patterns
* Compare application performance across regions
* Compare Production and Staging environments
* Analyze HTTP status-code distribution
* Identify high-latency services
* Build interactive dashboards for application reliability monitoring

## Technologies Used

| Technology           | Purpose                                  |
| -------------------- | ---------------------------------------- |
|   Python             | Data analysis and visualization          |
|   SQL / PostgreSQL   | Data storage and analytical queries      |
|   Excel              | Data analysis and PivotTables            |
|   Power BI           | Interactive dashboards and KPI reporting |

## Dataset

The project uses an application log dataset containing **3,000 application requests**.

### Key Fields

* Request_ID
* Timestamp
* Service
* Environment
* Region
* HTTP_Method
* Status_Code
* Latency_ms
* CPU_Usage_pct
* Payload_KB

## Python Analysis

Python is used for:

* Data quality validation
* Service performance analysis
* Average latency analysis
* Error-rate calculation
* Server-error analysis
* Regional performance analysis
* Environment comparison
* Performance visualization

### Python Visualizations

* Server Errors by Service
* Average Latency by Service
* Error Rate by Service

## SQL Analysis

SQL is used to perform structured analysis of application logs, including:

* Service performance summary
* Server errors by service
* Regional performance
* HTTP status-code distribution
* 4xx vs. 5xx error analysis
* Slowest services
* Environment performance comparison

## Excel Analysis

Excel is used for:

* Data exploration
* PivotTable analysis
* Request counting
* Service-level analysis
* Performance summarization

## Power BI Dashboard

The Power BI report contains **4 analytical dashboard pages** covering application performance, executive KPIs, reliability, regional performance, and environment analysis.

### Page 1 — Application Performance Overview

Key visuals include:

* Average Latency by Service
* Error Rate by Service
* Regional Performance — Average Latency
* Production vs. Staging — Average Latency
* Requests Over Time
* HTTP Status Code Distribution
* Slowest Services by Average Latency
* Environment Filter
* HTTP Status Code Filter

### Page 2 — Executive KPI Dashboard

Key visuals include:

* Average Latency (ms)
* Error Rate %
* Total Requests
* Server Errors
* Client Errors (4xx)
* Service Performance Summary
* Response Time Trend
* Errors by Service

### Page 3 — Service Reliability & Error Analysis

Key visuals include:

* 4xx vs 5xx Error Analysis
* Error Distribution by Status Code
* Error Trend Over Time
* Service Reliability Comparison
* Highest-Error Services
* Requests by Service & Status Code
* Status Code Filter
* Environment Slicer
* Service Slicer

### Page 4 — Regional & Environment Analysis

The fourth page contains **9 visuals** focused on regional and environment-level performance:

* Error Rate by Region
* Server Errors by Region
* Error Rate by Environment
* Environment Performance Trend
* Requests by Environment
* Average Latency by Region
* Requests by Region
* Production vs Staging Latency
* Region Slicer

## Key Insights

The analysis helps identify:

* Services with comparatively high latency
* Services generating more errors
* Server-error patterns across services
* Regional differences in application performance
* Production vs. Staging performance differences
* HTTP status-code distribution
* Environment-level reliability patterns
* Services requiring closer performance monitoring

## Project Structure
'''text
Application_Performance_Reliability_Analytics
│
├── data
│   └── application_logs.csv
│
├── python
│   ├── analysis.py
│   └── chart.py
│
├── sql
│   └── application_analysis.sql
│
├── excel
│   └── application_performance_data.xlsx
│
├── powerbi
│   └── power bi work.pbix
│
├── visuals
│   ├── server_errors_by_service.png
│   ├── average_latency_by_service.png
│   └── error_rate_by_service.png
│
└── README.md
'''text

## End-to-End Workflow
'''text
Raw Application Logs
        ↓
Data Quality Validation
        ↓
Python Analysis
        ↓
SQL / PostgreSQL Analysis
        ↓
Excel PivotTable Analysis
        ↓
Python Visualizations
        ↓
Power BI Interactive Dashboards
        ↓
Application Performance & Reliability Insights
'''text
## Outcome

This project demonstrates an end-to-end analytics workflow using **Python, SQL, Excel, and Power BI**.

It showcases practical skills in:

* Data Analysis
* SQL
* PostgreSQL
* Python
* Excel
* Power BI
* Data Visualization
* KPI Reporting
* Application Performance Monitoring
* Reliability Analysis
