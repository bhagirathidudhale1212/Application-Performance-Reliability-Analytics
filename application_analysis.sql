Application Performance & Reliability Analytics
-- SQL Analysis

 1. Create database
CREATE DATABASE ApplicationReliability;


2. Create application logs table
CREATE TABLE ApplicationLogs (
    Request_ID VARCHAR(20) PRIMARY KEY,
    Timestamp TIMESTAMP,
    Service VARCHAR(100),
    Environment VARCHAR(30),
    Region VARCHAR(50),
    HTTP_Method VARCHAR(10),
    Status_Code INT,
    Latency_ms DECIMAL(10,1),
    CPU_Usage_pct DECIMAL(5,2),
    Payload_KB INT
);


 3. Service performance summary
SELECT
    Service,
    COUNT(*) AS Total_Requests,
    AVG(Latency_ms) AS Avg_Latency_ms,
    SUM(CASE WHEN Status_Code >= 400 THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*) AS Error_Rate_pct
FROM ApplicationLogs
GROUP BY Service
ORDER BY Avg_Latency_ms DESC;


 4. Server errors by service
SELECT
    Service,
    COUNT(*) AS Server_Errors,
    AVG(Latency_ms) AS Avg_Latency_ms
FROM ApplicationLogs
WHERE Status_Code >= 500
GROUP BY Service
ORDER BY Server_Errors DESC;


5. Performance by region
SELECT
    Region,
    COUNT(*) AS Total_Requests,
    AVG(Latency_ms) AS Avg_Latency_ms
FROM ApplicationLogs
GROUP BY Region
ORDER BY Avg_Latency_ms DESC;


 6. HTTP status code distribution
SELECT
    Status_Code,
    COUNT(*) AS Request_Count
FROM ApplicationLogs
GROUP BY Status_Code
ORDER BY Status_Code;


 7. 4xx and 5xx error analysis
SELECT
    CASE
        WHEN Status_Code BETWEEN 400 AND 499 THEN '4xx Client Error'
        WHEN Status_Code BETWEEN 500 AND 599 THEN '5xx Server Error'
        ELSE 'Other'
    END AS Error_Category,
    COUNT(*) AS Error_Count
FROM ApplicationLogs
GROUP BY Error_Category
ORDER BY Error_Count DESC;

 8. Slowest services
SELECT
    Service,
    MAX(Latency_ms) AS Max_Latency_ms,
    AVG(Latency_ms) AS Avg_Latency_ms
FROM ApplicationLogs
GROUP BY Service
ORDER BY Max_Latency_ms DESC;


 9. Environment performance comparison
SELECT
    Environment,
    COUNT(*) AS Total_Requests,
    AVG(Latency_ms) AS Avg_Latency_ms,
    SUM(CASE WHEN Status_Code >= 400 THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*) AS Error_Rate_pct
FROM ApplicationLogs
GROUP BY Environment
ORDER BY Avg_Latency_ms DESC;