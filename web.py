# app.py - Complete Multi-Domain Intelligence Platform (Single File Version)
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import io
import random

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== LOAD COMPLETE CSV FILES ======================
# COMPLETE datasets_metadata.csv
datasets_metadata_content = """dataset_id,name,rows,columns,uploaded_by,upload_date
1,Customer_Churn,5000,15,data_scientist,2024-01-15
2,Financial_Fraud,150000,22,cyber_admin,2024-03-01
3,Server_Logs,800000,10,data_scientist,2024-05-10
4,Image_Classification,1000,5,data_scientist,2024-08-20
5,HR_Salary,3000,12,it_admin,2024-09-01"""

datasets_df = pd.read_csv(io.StringIO(datasets_metadata_content))

# COMPLETE it_tickets.csv
it_tickets_content = """ticket_id,priority,description,status,assigned_to,created_at,resolution_time_hours
2000,High,Ticket 0 problem description,Resolved,IT_Support_A,2024-01-27 05:00:00,24
2001,Medium,Ticket 1 problem description,Resolved,IT_Support_C,2024-08-06 07:00:00,37
2002,High,Ticket 2 problem description,Open,IT_Support_C,2024-04-07 11:00:00,40
2003,Medium,Ticket 3 problem description,Resolved,IT_Support_A,2024-08-24 20:00:00,6
2004,Critical,Ticket 4 problem description,Resolved,IT_Support_B,2024-06-21 16:00:00,19
2005,High,Ticket 5 problem description,Open,IT_Support_C,2024-07-08 13:00:00,80
2006,Medium,Ticket 6 problem description,Resolved,IT_Support_A,2024-03-04 01:00:00,7
2007,Medium,Ticket 7 problem description,Resolved,IT_Support_A,2024-07-11 18:00:00,10
2008,High,Ticket 8 problem description,Resolved,IT_Support_A,2024-06-29 03:00:00,41
2009,High,Ticket 9 problem description,Resolved,IT_Support_A,2024-10-08 20:00:00,32
2010,High,Ticket 10 problem description,Resolved,IT_Support_C,2024-09-23 07:00:00,70
2011,Low,Ticket 11 problem description,In Progress,IT_Support_C,2024-01-11 03:00:00,46
2012,Medium,Ticket 12 problem description,Open,IT_Support_A,2024-04-22 06:00:00,15
2013,Medium,Ticket 13 problem description,Resolved,IT_Support_A,2024-08-19 02:00:00,30
2014,Low,Ticket 14 problem description,Resolved,IT_Support_A,2024-04-07 22:00:00,37
2015,High,Ticket 15 problem description,Resolved,IT_Support_A,2024-04-20 23:00:00,29
2016,Low,Ticket 16 problem description,Waiting for User,IT_Support_C,2024-09-02 21:00:00,75
2017,Medium,Ticket 17 problem description,Resolved,IT_Support_A,2024-03-09 23:00:00,4
2018,High,Ticket 18 problem description,Resolved,IT_Support_A,2024-10-15 03:00:00,20
2019,Medium,Ticket 19 problem description,Resolved,IT_Support_A,2024-08-26 19:00:00,32
2020,Low,Ticket 20 problem description,Resolved,IT_Support_B,2024-08-14 19:00:00,36
2021,Medium,Ticket 21 problem description,In Progress,IT_Support_A,2024-07-19 01:00:00,4
2022,Low,Ticket 22 problem description,Resolved,IT_Support_C,2024-03-13 08:00:00,61
2023,Medium,Ticket 23 problem description,In Progress,IT_Support_A,2024-10-22 16:00:00,17
2024,Low,Ticket 24 problem description,Resolved,IT_Support_C,2024-05-08 10:00:00,83
2025,Medium,Ticket 25 problem description,In Progress,IT_Support_B,2024-04-13 09:00:00,22
2026,Low,Ticket 26 problem description,Resolved,IT_Support_A,2024-01-25 06:00:00,17
2027,Medium,Ticket 27 problem description,Resolved,IT_Support_B,2024-10-17 02:00:00,10
2028,High,Ticket 28 problem description,Open,IT_Support_C,2024-08-16 11:00:00,49
2029,Critical,Ticket 29 problem description,Waiting for User,IT_Support_C,2024-06-20 18:00:00,62
2030,High,Ticket 30 problem description,In Progress,IT_Support_B,2024-04-11 01:00:00,26
2031,Critical,Ticket 31 problem description,Resolved,IT_Support_B,2024-01-12 18:00:00,18
2032,High,Ticket 32 problem description,Waiting for User,IT_Support_C,2024-04-10 11:00:00,69
2033,Medium,Ticket 33 problem description,Resolved,IT_Support_B,2024-01-17 09:00:00,47
2034,Medium,Ticket 34 problem description,Waiting for User,IT_Support_A,2024-02-26 22:00:00,29
2035,Low,Ticket 35 problem description,Resolved,IT_Support_C,2024-01-12 15:00:00,61
2036,Low,Ticket 36 problem description,Open,IT_Support_A,2024-08-03 18:00:00,36
2037,Medium,Ticket 37 problem description,In Progress,IT_Support_B,2024-09-20 20:00:00,35
2038,Low,Ticket 38 problem description,Open,IT_Support_A,2024-03-21 22:00:00,12
2039,Low,Ticket 39 problem description,Resolved,IT_Support_A,2024-07-16 07:00:00,7
2040,Medium,Ticket 40 problem description,Resolved,IT_Support_A,2024-01-25 17:00:00,29
2041,High,Ticket 41 problem description,In Progress,IT_Support_C,2024-03-29 11:00:00,31
2042,High,Ticket 42 problem description,Resolved,IT_Support_A,2024-05-22 08:00:00,33
2043,High,Ticket 43 problem description,Waiting for User,IT_Support_A,2024-01-26 14:00:00,6
2044,High,Ticket 44 problem description,Open,IT_Support_A,2024-10-14 09:00:00,47
2045,High,Ticket 45 problem description,Resolved,IT_Support_B,2024-01-16 06:00:00,15
2046,Low,Ticket 46 problem description,Open,IT_Support_C,2024-10-08 20:00:00,62
2047,Low,Ticket 47 problem description,Resolved,IT_Support_B,2024-03-26 06:00:00,11
2048,Critical,Ticket 48 problem description,Open,IT_Support_B,2024-09-26 14:00:00,23
2049,High,Ticket 49 problem description,In Progress,IT_Support_C,2024-04-26 06:00:00,59
2050,Critical,Ticket 50 problem description,Resolved,IT_Support_B,2024-05-16 18:00:00,34
2051,Medium,Ticket 51 problem description,Resolved,IT_Support_A,2024-06-24 07:00:00,46
2052,Medium,Ticket 52 problem description,Waiting for User,IT_Support_A,2024-08-02 17:00:00,34
2053,Low,Ticket 53 problem description,Resolved,IT_Support_A,2024-08-10 19:00:00,29
2054,Medium,Ticket 54 problem description,Resolved,IT_Support_A,2024-04-12 16:00:00,4
2055,Low,Ticket 55 problem description,Resolved,IT_Support_B,2024-01-14 23:00:00,17
2056,Low,Ticket 56 problem description,Resolved,IT_Support_C,2024-04-17 12:00:00,62
2057,High,Ticket 57 problem description,Resolved,IT_Support_A,2024-04-07 02:00:00,13
2058,Low,Ticket 58 problem description,Resolved,IT_Support_B,2024-10-19 10:00:00,41
2059,Medium,Ticket 59 problem description,Resolved,IT_Support_B,2024-07-01 22:00:00,39
2060,Medium,Ticket 60 problem description,Open,IT_Support_A,2024-02-08 14:00:00,15
2061,Medium,Ticket 61 problem description,Resolved,IT_Support_C,2024-01-04 21:00:00,55
2062,Low,Ticket 62 problem description,Resolved,IT_Support_B,2024-07-28 00:00:00,29
2063,Medium,Ticket 63 problem description,Resolved,IT_Support_A,2024-01-16 12:00:00,11
2064,Low,Ticket 64 problem description,Resolved,IT_Support_C,2024-04-17 01:00:00,51
2065,Low,Ticket 65 problem description,Resolved,IT_Support_B,2024-08-14 09:00:00,2
2066,Medium,Ticket 66 problem description,Open,IT_Support_B,2024-02-03 22:00:00,47
2067,Low,Ticket 67 problem description,In Progress,IT_Support_B,2024-09-25 12:00:00,14
2068,Medium,Ticket 68 problem description,Resolved,IT_Support_B,2024-09-30 02:00:00,20
2069,Medium,Ticket 69 problem description,In Progress,IT_Support_C,2024-02-08 13:00:00,95
2070,Medium,Ticket 70 problem description,Open,IT_Support_A,2024-01-29 16:00:00,11
2071,High,Ticket 71 problem description,Resolved,IT_Support_A,2024-09-01 11:00:00,27
2072,Low,Ticket 72 problem description,Waiting for User,IT_Support_A,2024-07-03 15:00:00,3
2073,Medium,Ticket 73 problem description,Waiting for User,IT_Support_C,2024-08-23 14:00:00,67
2074,Medium,Ticket 74 problem description,Resolved,IT_Support_A,2024-09-22 06:00:00,44
2075,Low,Ticket 75 problem description,Resolved,IT_Support_C,2024-03-05 16:00:00,75
2076,High,Ticket 76 problem description,Waiting for User,IT_Support_B,2024-01-03 12:00:00,29
2077,Medium,Ticket 77 problem description,Open,IT_Support_C,2024-05-21 23:00:00,44
2078,Medium,Ticket 78 problem description,Resolved,IT_Support_C,2024-06-06 17:00:00,73
2079,Low,Ticket 79 problem description,In Progress,IT_Support_C,2024-05-25 04:00:00,78
2080,Medium,Ticket 80 problem description,In Progress,IT_Support_C,2024-06-01 15:00:00,90
2081,Low,Ticket 81 problem description,In Progress,IT_Support_B,2024-07-11 20:00:00,20
2082,Low,Ticket 82 problem description,In Progress,IT_Support_B,2024-03-13 14:00:00,6
2083,High,Ticket 83 problem description,In Progress,IT_Support_A,2024-05-19 04:00:00,19
2084,Critical,Ticket 84 problem description,Resolved,IT_Support_A,2024-03-01 04:00:00,5
2085,Medium,Ticket 85 problem description,Resolved,IT_Support_B,2024-07-16 06:00:00,3
2086,Medium,Ticket 86 problem description,Open,IT_Support_B,2024-01-11 12:00:00,1
2087,High,Ticket 87 problem description,Waiting for User,IT_Support_A,2024-08-13 06:00:00,38
2088,Medium,Ticket 88 problem description,Resolved,IT_Support_B,2024-02-21 03:00:00,15
2089,Medium,Ticket 89 problem description,Resolved,IT_Support_C,2024-02-28 07:00:00,35
2090,Medium,Ticket 90 problem description,Open,IT_Support_B,2024-05-27 21:00:00,35
2091,Medium,Ticket 91 problem description,Resolved,IT_Support_C,2024-08-30 12:00:00,38
2092,Medium,Ticket 92 problem description,Open,IT_Support_C,2024-04-16 01:00:00,35
2093,Medium,Ticket 93 problem description,In Progress,IT_Support_C,2024-08-05 08:00:00,61
2094,Medium,Ticket 94 problem description,Open,IT_Support_B,2024-08-28 02:00:00,18
2095,High,Ticket 95 problem description,Resolved,IT_Support_C,2024-09-18 04:00:00,70
2096,Medium,Ticket 96 problem description,Resolved,IT_Support_C,2024-09-17 21:00:00,37
2097,Medium,Ticket 97 problem description,Resolved,IT_Support_C,2024-02-16 22:00:00,79
2098,Low,Ticket 98 problem description,Resolved,IT_Support_A,2024-06-25 08:00:00,27
2099,Medium,Ticket 99 problem description,Resolved,IT_Support_B,2024-04-08 19:00:00,8
2100,Low,Ticket 100 problem description,Resolved,IT_Support_A,2024-08-28 09:00:00,46
2101,Medium,Ticket 101 problem description,Resolved,IT_Support_A,2024-06-26 17:00:00,25
2102,High,Ticket 102 problem description,Resolved,IT_Support_B,2024-03-02 16:00:00,17
2103,Low,Ticket 103 problem description,Resolved,IT_Support_C,2024-08-03 02:00:00,91
2104,Medium,Ticket 104 problem description,Resolved,IT_Support_C,2024-06-08 02:00:00,91
2105,Medium,Ticket 105 problem description,Resolved,IT_Support_A,2024-09-25 23:00:00,15
2106,Critical,Ticket 106 problem description,Open,IT_Support_C,2024-03-29 08:00:00,36
2107,Medium,Ticket 107 problem description,Open,IT_Support_B,2024-03-08 13:00:00,46
2108,Medium,Ticket 108 problem description,Resolved,IT_Support_C,2024-04-07 10:00:00,33
2109,Medium,Ticket 109 problem description,In Progress,IT_Support_C,2024-04-14 23:00:00,35
2110,Low,Ticket 110 problem description,Resolved,IT_Support_B,2024-05-02 08:00:00,29
2111,High,Ticket 111 problem description,Open,IT_Support_A,2024-07-13 01:00:00,44
2112,Medium,Ticket 112 problem description,Resolved,IT_Support_C,2024-06-18 08:00:00,87
2113,Medium,Ticket 113 problem description,Waiting for User,IT_Support_A,2024-02-09 04:00:00,3
2114,High,Ticket 114 problem description,In Progress,IT_Support_A,2024-08-13 23:00:00,20
2115,Medium,Ticket 115 problem description,Open,IT_Support_C,2024-05-03 14:00:00,51
2116,Medium,Ticket 116 problem description,In Progress,IT_Support_A,2024-02-07 07:00:00,15
2117,Medium,Ticket 117 problem description,Resolved,IT_Support_C,2024-09-07 04:00:00,55
2118,High,Ticket 118 problem description,Resolved,IT_Support_A,2024-06-24 17:00:00,30
2119,Medium,Ticket 119 problem description,Open,IT_Support_C,2024-02-06 15:00:00,32
2120,Critical,Ticket 120 problem description,Resolved,IT_Support_A,2024-10-10 04:00:00,7
2121,Low,Ticket 121 problem description,In Progress,IT_Support_C,2024-03-21 17:00:00,70
2122,High,Ticket 122 problem description,Resolved,IT_Support_C,2024-02-09 12:00:00,89
2123,Medium,Ticket 123 problem description,Resolved,IT_Support_A,2024-08-11 18:00:00,20
2124,Low,Ticket 124 problem description,Resolved,IT_Support_B,2024-07-04 02:00:00,36
2125,Medium,Ticket 125 problem description,Resolved,IT_Support_C,2024-02-25 07:00:00,43
2126,Low,Ticket 126 problem description,Open,IT_Support_B,2024-02-09 12:00:00,38
2127,High,Ticket 127 problem description,Resolved,IT_Support_A,2024-08-24 00:00:00,22
2128,Low,Ticket 128 problem description,Resolved,IT_Support_B,2024-09-18 23:00:00,2
2129,Medium,Ticket 129 problem description,Resolved,IT_Support_B,2024-05-26 15:00:00,24
2130,Low,Ticket 130 problem description,Resolved,IT_Support_C,2024-06-16 00:00:00,41
2131,High,Ticket 131 problem description,In Progress,IT_Support_B,2024-02-28 15:00:00,11
2132,High,Ticket 132 problem description,Resolved,IT_Support_B,2024-06-17 12:00:00,13
2133,High,Ticket 133 problem description,Resolved,IT_Support_A,2024-02-14 20:00:00,17
2134,Medium,Ticket 134 problem description,Resolved,IT_Support_B,2024-06-18 03:00:00,8
2135,Low,Ticket 135 problem description,Open,IT_Support_B,2024-07-09 05:00:00,21
2136,Low,Ticket 136 problem description,Resolved,IT_Support_A,2024-07-06 06:00:00,18
2137,Critical,Ticket 137 problem description,In Progress,IT_Support_C,2024-05-12 10:00:00,41
2138,Low,Ticket 138 problem description,Waiting for User,IT_Support_B,2024-02-14 18:00:00,18
2139,Medium,Ticket 139 problem description,Resolved,IT_Support_B,2024-01-31 22:00:00,46
2140,Medium,Ticket 140 problem description,Resolved,IT_Support_C,2024-06-08 10:00:00,42
2141,High,Ticket 141 problem description,Resolved,IT_Support_B,2024-06-06 06:00:00,31
2142,Low,Ticket 142 problem description,Resolved,IT_Support_C,2024-03-22 03:00:00,54
2143,High,Ticket 143 problem description,Open,IT_Support_B,2024-09-14 13:00:00,32
2144,Medium,Ticket 144 problem description,Waiting for User,IT_Support_A,2024-03-17 11:00:00,11
2145,Low,Ticket 145 problem description,Resolved,IT_Support_B,2024-10-21 01:00:00,45
2146,High,Ticket 146 problem description,Resolved,IT_Support_B,2024-08-11 12:00:00,25
2147,Medium,Ticket 147 problem description,Resolved,IT_Support_C,2024-02-15 16:00:00,74
2148,High,Ticket 148 problem description,Open,IT_Support_A,2024-08-20 16:00:00,38
2149,Medium,Ticket 149 problem description,Resolved,IT_Support_A,2024-08-10 01:00:00,41"""

tickets_df = pd.read_csv(io.StringIO(it_tickets_content))

# COMPLETE cyber_incidents.csv
cyber_incidents_content = """incident_id,timestamp,severity,category,status,description
1000,2024-04-12 19:00:00.000000,Low,Malware,Closed,Incident 0 description
1001,2024-09-27 10:00:00.000000,Medium,Malware,Resolved,Incident 1 description
1002,2024-03-12 20:00:00.000000,Critical,Misconfiguration,Resolved,Incident 2 description
1003,2024-04-12 18:00:00.000000,Medium,Phishing,Open,Incident 3 description
1004,2024-08-02 10:00:00.000000,Medium,Phishing,In Progress,Incident 4 description
1005,2024-03-28 20:00:00.000000,Medium,Phishing,In Progress,Incident 5 description
1006,2024-04-09 07:00:00.000000,Medium,Phishing,In Progress,Incident 6 description
1007,2024-05-31 02:00:00.000000,Medium,Malware,In Progress,Incident 7 description
1008,2024-05-29 20:00:00.000000,Medium,Malware,Open,Incident 8 description
1009,2024-09-14 23:00:00.000000,Medium,Malware,Open,Incident 9 description
1010,2024-10-20 01:00:00.000000,Critical,Unauthorized Access,Closed,Incident 10 description
1011,2024-07-10 20:00:00.000000,Medium,Misconfiguration,In Progress,Incident 11 description
1012,2024-06-09 11:00:00.000000,High,Phishing,Closed,Incident 12 description
1013,2024-01-22 11:00:00.000000,Low,Phishing,In Progress,Incident 13 description
1014,2024-02-18 09:00:00.000000,Medium,DDoS,In Progress,Incident 14 description
1015,2024-07-06 15:00:00.000000,Low,Malware,Resolved,Incident 15 description
1016,2024-09-27 14:00:00.000000,Medium,Phishing,Closed,Incident 16 description
1017,2024-02-20 11:00:00.000000,Low,Phishing,Closed,Incident 17 description
1018,2024-02-24 19:00:00.000000,Low,Phishing,In Progress,Incident 18 description
1019,2024-05-10 04:00:00.000000,High,Unauthorized Access,Closed,Incident 19 description
1020,2024-05-14 20:00:00.000000,Medium,Phishing,In Progress,Incident 20 description
1021,2024-06-15 17:00:00.000000,Medium,DDoS,Resolved,Incident 21 description
1022,2024-03-29 13:00:00.000000,Low,Malware,Resolved,Incident 22 description
1023,2024-08-29 08:00:00.000000,Medium,Phishing,Resolved,Incident 23 description
1024,2024-02-22 01:00:00.000000,High,Malware,Resolved,Incident 24 description
1025,2024-04-01 14:00:00.000000,Low,Phishing,Resolved,Incident 25 description
1026,2024-09-20 14:00:00.000000,Low,DDoS,In Progress,Incident 26 description
1027,2024-02-04 13:00:00.000000,Medium,Phishing,Resolved,Incident 27 description
1028,2024-03-21 03:00:00.000000,Critical,Phishing,In Progress,Incident 28 description
1029,2024-02-19 07:00:00.000000,Low,DDoS,Resolved,Incident 29 description
1030,2024-01-02 05:00:00.000000,Medium,Phishing,In Progress,Incident 30 description
1031,2024-02-23 09:00:00.000000,Medium,Phishing,Resolved,Incident 31 description
1032,2024-09-16 21:00:00.000000,Low,Malware,Resolved,Incident 32 description
1033,2024-07-09 17:00:00.000000,Medium,Phishing,Resolved,Incident 33 description
1034,2024-08-05 11:00:00.000000,Low,Unauthorized Access,In Progress,Incident 34 description
1035,2024-06-10 09:00:00.000000,High,Phishing,Resolved,Incident 35 description
1036,2024-09-26 15:00:00.000000,Medium,Malware,Open,Incident 36 description
1037,2024-09-27 07:00:00.000000,Medium,Malware,Resolved,Incident 37 description
1038,2024-08-02 07:00:00.000000,High,DDoS,Resolved,Incident 38 description
1039,2024-07-31 15:00:00.000000,High,Phishing,Open,Incident 39 description
1040,2024-08-24 17:00:00.000000,Low,Phishing,In Progress,Incident 40 description
1041,2024-02-22 23:00:00.000000,Medium,Misconfiguration,Resolved,Incident 41 description
1042,2024-08-04 12:00:00.000000,High,Unauthorized Access,In Progress,Incident 42 description
1043,2024-02-10 14:00:00.000000,Low,Unauthorized Access,In Progress,Incident 43 description
1044,2024-03-05 06:00:00.000000,Low,Phishing,Closed,Incident 44 description
1045,2024-01-09 23:00:00.000000,Medium,Phishing,Resolved,Incident 45 description
1046,2024-05-08 11:00:00.000000,Low,Phishing,Resolved,Incident 46 description
1047,2024-05-15 23:00:00.000000,High,Malware,In Progress,Incident 47 description
1048,2024-03-03 10:00:00.000000,High,Phishing,Closed,Incident 48 description
1049,2024-03-21 07:00:00.000000,Low,Unauthorized Access,In Progress,Incident 49 description
1050,2024-06-11 02:00:00.000000,Low,Phishing,Resolved,Incident 50 description
1051,2024-10-15 04:00:00.000000,Low,Misconfiguration,In Progress,Incident 51 description
1052,2024-08-18 08:00:00.000000,Medium,Malware,Closed,Incident 52 description
1053,2024-01-28 06:00:00.000000,Low,Unauthorized Access,Resolved,Incident 53 description
1054,2024-07-19 07:00:00.000000,Low,Phishing,Resolved,Incident 54 description
1055,2024-09-24 01:00:00.000000,Low,Malware,In Progress,Incident 55 description
1056,2024-02-02 15:00:00.000000,Low,DDoS,Resolved,Incident 56 description
1057,2024-03-02 23:00:00.000000,Medium,Phishing,Resolved,Incident 57 description
1058,2024-10-19 02:00:00.000000,Medium,Phishing,Resolved,Incident 58 description
1059,2024-06-20 07:00:00.000000,Medium,Misconfiguration,Resolved,Incident 59 description
1060,2024-08-01 02:00:00.000000,Low,DDoS,Resolved,Incident 60 description
1061,2024-08-14 04:00:00.000000,Low,Phishing,Open,Incident 61 description
1062,2024-05-10 00:00:00.000000,High,Malware,Closed,Incident 62 description
1063,2024-01-05 22:00:00.000000,Medium,Malware,Resolved,Incident 63 description
1064,2024-09-11 13:00:00.000000,Medium,DDoS,Open,Incident 64 description
1065,2024-10-09 08:00:00.000000,Medium,Phishing,In Progress,Incident 65 description
1066,2024-07-25 14:00:00.000000,Low,Phishing,Resolved,Incident 66 description
1067,2024-02-11 12:00:00.000000,High,Phishing,Resolved,Incident 67 description
1068,2024-06-27 06:00:00.000000,Critical,Malware,Resolved,Incident 68 description
1069,2024-08-28 19:00:00.000000,Medium,DDoS,Resolved,Incident 69 description
1070,2024-04-05 03:00:00.000000,High,Phishing,In Progress,Incident 70 description
1071,2024-08-09 04:00:00.000000,Medium,Misconfiguration,In Progress,Incident 71 description
1072,2024-08-18 12:00:00.000000,Low,Malware,Resolved,Incident 72 description
1073,2024-05-22 10:00:00.000000,Low,Phishing,Open,Incident 73 description
1074,2024-01-29 03:00:00.000000,Medium,Phishing,Closed,Incident 74 description
1075,2024-01-13 06:00:00.000000,Medium,Phishing,Resolved,Incident 75 description
1076,2024-07-05 18:00:00.000000,Medium,Misconfiguration,Open,Incident 76 description
1077,2024-03-26 01:00:00.000000,Medium,DDoS,Open,Incident 77 description
1078,2024-06-18 12:00:00.000000,High,Malware,Open,Incident 78 description
1079,2024-03-02 20:00:00.000000,Medium,DDoS,Resolved,Incident 79 description
1080,2024-05-13 11:00:00.000000,Low,Malware,Closed,Incident 80 description
1081,2024-02-13 19:00:00.000000,Medium,DDoS,In Progress,Incident 81 description
1082,2024-10-12 10:00:00.000000,Low,Phishing,Closed,Incident 82 description
1083,2024-05-07 22:00:00.000000,Medium,Malware,Open,Incident 83 description
1084,2024-08-18 00:00:00.000000,Medium,Phishing,In Progress,Incident 84 description
1085,2024-10-09 19:00:00.000000,Medium,Phishing,Closed,Incident 85 description
1086,2024-08-20 02:00:00.000000,Medium,Phishing,Closed,Incident 86 description
1087,2024-07-16 07:00:00.000000,Low,Phishing,Closed,Incident 87 description
1088,2024-05-16 04:00:00.000000,High,Phishing,Resolved,Incident 88 description
1089,2024-08-12 18:00:00.000000,Medium,Phishing,Resolved,Incident 89 description
1090,2024-08-21 11:00:00.000000,Medium,Misconfiguration,Resolved,Incident 90 description
1091,2024-05-31 14:00:00.000000,Low,Phishing,Closed,Incident 91 description
1092,2024-06-08 23:00:00.000000,Critical,Phishing,Resolved,Incident 92 description
1093,2024-08-20 19:00:00.000000,Low,Unauthorized Access,In Progress,Incident 93 description
1094,2024-04-22 16:00:00.000000,Medium,Unauthorized Access,Resolved,Incident 94 description
1095,2024-02-21 11:00:00.000000,High,Phishing,In Progress,Incident 95 description
1096,2024-10-21 01:00:00.000000,Low,Malware,Closed,Incident 96 description
1097,2024-04-22 04:00:00.000000,Low,DDoS,Closed,Incident 97 description
1098,2024-04-22 23:00:00.000000,Low,Phishing,Resolved,Incident 98 description
1099,2024-03-21 16:00:00.000000,Medium,Misconfiguration,Open,Incident 99 description
1100,2025-10-16 09:23:45.891480,High,Phishing,Open,Recent Phishing Attempt 0
1101,2025-10-25 07:23:45.891520,High,Phishing,In Progress,Recent Phishing Attempt 1
1102,2025-09-30 18:23:45.891532,High,Phishing,In Progress,Recent Phishing Attempt 2
1103,2025-09-30 01:23:45.891543,Medium,Phishing,Open,Recent Phishing Attempt 3
1104,2025-10-07 06:23:45.891554,Medium,Phishing,In Progress,Recent Phishing Attempt 4
1105,2025-10-02 03:23:45.891561,High,Phishing,In Progress,Recent Phishing Attempt 5
1106,2025-10-02 18:23:45.891568,High,Phishing,In Progress,Recent Phishing Attempt 6
1107,2025-10-22 10:23:45.891575,High,Phishing,Open,Recent Phishing Attempt 7
1108,2025-10-16 00:23:45.891584,Medium,Phishing,Open,Recent Phishing Attempt 8
1109,2025-10-10 17:23:45.891591,Medium,Phishing,Open,Recent Phishing Attempt 9
1110,2025-10-01 05:23:45.891597,High,Phishing,Open,Recent Phishing Attempt 10
1111,2025-09-30 04:23:45.891604,High,Phishing,Open,Recent Phishing Attempt 11
1112,2025-10-22 12:23:45.891611,High,Phishing,In Progress,Recent Phishing Attempt 12
1113,2025-10-26 00:23:45.891618,High,Phishing,Open,Recent Phishing Attempt 13
1114,2025-09-30 20:23:45.891624,High,Phishing,Open,Recent Phishing Attempt 14"""

incidents_df = pd.read_csv(io.StringIO(cyber_incidents_content))

# Process datetime columns
tickets_df['created_at'] = pd.to_datetime(tickets_df['created_at'])
incidents_df['timestamp'] = pd.to_datetime(incidents_df['timestamp'])

# ====================== SESSION STATE INIT ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "users" not in st.session_state:
    st.session_state.users = {}  # In-memory users (replace with DB later)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Add sample users on first run
if not st.session_state.users:
    st.session_state.users = {
        "admin": "admin123",
        "analyst": "analyst123",
        "operator": "operator123"
    }


# ====================== AI ASSISTANT CLASS ======================
class AIAssistant:
    """Enhanced AI Assistant for multi-domain intelligence"""

    def __init__(self):
        self.name = "Guardian AI"
        self.version = "2.0"
        self.expertise = ["Cybersecurity", "Data Science", "IT Operations", "Business Intelligence"]

    def analyze_threat(self, incident_data):
        """Analyze cybersecurity threats"""
        severity = incident_data.get('severity', 'Medium')
        category = incident_data.get('category', 'Unknown')

        analysis_templates = {
            "Critical": {
                "Phishing": "🚨 CRITICAL PHISHING ALERT! Immediate action required. Isolate affected systems, reset credentials, and notify security team.",
                "Malware": "🚨 CRITICAL MALWARE DETECTED! Contain infected systems, activate incident response, and conduct forensic analysis.",
                "DDoS": "🚨 CRITICAL DDoS ATTACK! Activate mitigation services, implement rate limiting, and monitor traffic patterns.",
                "default": "🚨 CRITICAL THREAT DETECTED! Activate emergency protocols and notify CISO immediately."
            },
            "High": {
                "Phishing": "🔴 HIGH RISK PHISHING: Investigate email headers, update spam filters, and conduct user awareness training.",
                "Malware": "🔴 HIGH RISK MALWARE: Scan systems, update antivirus, and review security logs.",
                "Unauthorized Access": "🔴 UNAUTHORIZED ACCESS ATTEMPT: Review access logs, strengthen authentication, and monitor suspicious activity.",
                "default": "🔴 HIGH SEVERITY THREAT: Investigate thoroughly and implement countermeasures within 4 hours."
            },
            "Medium": {
                "Phishing": "🟡 MEDIUM PHISHING RISK: Update email security rules and monitor for similar attacks.",
                "Malware": "🟡 SUSPICIOUS ACTIVITY: Run full system scan and review recent downloads.",
                "default": "🟡 MODERATE THREAT: Investigate within 24 hours and update security policies."
            },
            "Low": {
                "default": "🟢 LOW RISK INCIDENT: Monitor and document for future reference."
            }
        }

        severity_dict = analysis_templates.get(severity, analysis_templates["Medium"])
        analysis = severity_dict.get(category, severity_dict["default"])

        # Add recommendations
        recommendations = self._get_threat_recommendations(severity, category)
        return f"{analysis}\n\n🤖 **AI Recommendations:**\n" + "\n".join([f"• {rec}" for rec in recommendations])

    def _get_threat_recommendations(self, severity, category):
        """Get specific threat recommendations"""
        recommendations = []

        if severity in ["Critical", "High"]:
            recommendations.append("Activate incident response team")
            recommendations.append("Isolate affected systems immediately")
            recommendations.append("Notify senior management")

        if category == "Phishing":
            recommendations.append("Implement DMARC/DKIM/SPF email authentication")
            recommendations.append("Conduct phishing simulation training")
            recommendations.append("Update email filtering rules")
        elif category == "Malware":
            recommendations.append("Run antivirus scans on all endpoints")
            recommendations.append("Review system logs for IOCs")
            recommendations.append("Update all security patches")
        elif category == "DDoS":
            recommendations.append("Contact ISP for traffic filtering")
            recommendations.append("Activate cloud DDoS protection")
            recommendations.append("Implement rate limiting")

        return recommendations

    def analyze_dataset(self, dataset_data):
        """Provide insights for datasets"""
        rows = dataset_data.get('rows', 0)
        columns = dataset_data.get('columns', 0)
        name = dataset_data.get('name', 'Dataset')

        insights = []

        # Size-based insights
        if rows > 1000000:
            insights.append("📊 **Very Large Dataset** - Consider distributed processing with Spark or Dask")
        elif rows > 100000:
            insights.append("📊 **Large Dataset** - May require optimized processing and memory management")
        else:
            insights.append("📊 **Moderate Dataset** - Suitable for standard analytical tools")

        # Analysis recommendations
        if columns > 20:
            insights.append("🎯 **High Dimensionality** - Consider dimensionality reduction (PCA/t-SNE)")

        # Domain-specific recommendations
        if "customer" in name.lower() or "churn" in name.lower():
            insights.append("👥 **Customer Analysis** - Apply RFM analysis and customer segmentation")
            insights.append("📈 **Churn Prediction** - Use XGBoost or Random Forest for prediction")
        elif "fraud" in name.lower():
            insights.append("🕵️ **Fraud Detection** - Implement anomaly detection algorithms")
            insights.append("⚖️ **Class Imbalance** - Use SMOTE or weighted loss functions")
        elif "log" in name.lower():
            insights.append("🔍 **Log Analysis** - Apply time series analysis and pattern recognition")
            insights.append("🚨 **Anomaly Detection** - Use isolation forests or autoencoders")

        # General recommendations
        insights.append("🔧 **Preprocessing** - Check for missing values and outliers")
        insights.append("📐 **Feature Engineering** - Create domain-specific features")
        insights.append("🤖 **Model Selection** - Start with baseline models before complex ones")

        return "🤖 **AI Dataset Analysis:**\n\n" + "\n".join([f"• {insight}" for insight in insights])

    def analyze_ticket(self, ticket_data):
        """Analyze IT tickets for optimization"""
        priority = ticket_data.get('priority', 'Medium')
        status = ticket_data.get('status', 'Open')
        resolution_time = ticket_data.get('resolution_time_hours', 0)

        analysis = []

        # Priority-based analysis
        if priority == "Critical":
            analysis.append("🚨 **CRITICAL TICKET** - Immediate attention required. Escalate to senior staff.")
        elif priority == "High":
            analysis.append("🔴 **HIGH PRIORITY** - Address within 4 hours. System impact likely.")
        elif priority == "Medium":
            analysis.append("🟡 **MEDIUM PRIORITY** - Address within 24 hours. Business process affected.")
        else:
            analysis.append("🟢 **LOW PRIORITY** - Address within 72 hours. Minor inconvenience.")

        # Resolution time insights
        if resolution_time > 72:
            analysis.append("⏰ **SLA BREACH RISK** - Resolution time exceeds 72 hours. Review process.")
        elif resolution_time > 24:
            analysis.append("⚠️ **LONG RESOLUTION** - Consider process optimization or automation.")

        # Status-based recommendations
        if status == "Open":
            analysis.append("📋 **ACTION NEEDED** - Assign to available technician immediately.")
        elif status == "In Progress":
            analysis.append("⚙️ **IN PROGRESS** - Monitor closely and provide updates to requester.")
        elif status == "Waiting for User":
            analysis.append("⏳ **WAITING FOR USER** - Send reminder and follow up promptly.")

        # Optimization suggestions
        analysis.append("🤖 **AI Optimization Tips:**")
        analysis.append("• Automate common ticket resolutions")
        analysis.append("• Implement knowledge base for self-service")
        analysis.append("• Use predictive assignment based on technician expertise")
        analysis.append("• Monitor ticket aging and escalate proactively")

        return "\n".join(analysis)

    def get_cross_domain_insights(self, incidents_df, datasets_df, tickets_df):
        """Provide cross-domain intelligence insights"""
        insights = []

        if not incidents_df.empty:
            # Security insights
            critical_incidents = len(incidents_df[incidents_df['severity'] == 'Critical'])
            phishing_count = len(incidents_df[incidents_df['category'] == 'Phishing'])

            if critical_incidents > 0:
                insights.append(f"🛡️ **Security Alert:** {critical_incidents} critical incidents detected")
            if phishing_count > 5:
                insights.append(f"📧 **Phishing Spike:** {phishing_count} phishing incidents - review email security")

        if not datasets_df.empty:
            # Data insights
            total_rows = datasets_df['rows'].sum()
            recent_datasets = len(datasets_df[datasets_df['upload_date'] > '2024-08-01'])

            insights.append(f"📊 **Data Volume:** {total_rows:,} total rows across all datasets")
            if recent_datasets > 0:
                insights.append(f"🆕 **Recent Data:** {recent_datasets} datasets uploaded in last 3 months")

        if not tickets_df.empty:
            # IT insights
            open_tickets = len(tickets_df[tickets_df['status'] == 'Open'])
            avg_resolution = tickets_df[tickets_df['status'] == 'Resolved']['resolution_time_hours'].mean()

            insights.append(f"⚙️ **IT Operations:** {open_tickets} open tickets")
            if not pd.isna(avg_resolution):
                insights.append(f"⏱️ **Performance:** Average resolution time: {avg_resolution:.1f} hours")

        if not insights:
            insights.append("📈 **System Status:** All domains operating normally")

        return "🌐 **Cross-Domain Intelligence:**\n\n" + "\n".join([f"• {insight}" for insight in insights])

    def chat_response(self, user_message):
        """Generate chat response based on user query"""
        user_message_lower = user_message.lower()

        # Domain detection
        if any(word in user_message_lower for word in ["security", "threat", "attack", "malware", "phishing"]):
            response = self._security_chat_response(user_message)
        elif any(word in user_message_lower for word in ["data", "dataset", "analysis", "model", "ml"]):
            response = self._data_science_chat_response(user_message)
        elif any(word in user_message_lower for word in ["ticket", "it", "support", "sla", "service"]):
            response = self._it_chat_response(user_message)
        else:
            response = self._general_chat_response(user_message)

        return response

    def _security_chat_response(self, query):
        """Generate security-focused response"""
        responses = [
            "Based on current threat intelligence, I recommend reviewing your email security policies. Phishing attacks have increased by 40% this quarter.",
            "For enhanced security, consider implementing multi-factor authentication across all systems and conducting regular security awareness training.",
            "I detect potential vulnerabilities in your network. Recommend running a vulnerability scan and updating all security patches.",
            "Based on industry trends, ransomware attacks are targeting organizations like yours. Ensure backups are current and test recovery procedures."
        ]
        return f"🛡️ **Security Analysis:** {random.choice(responses)}"

    def _data_science_chat_response(self, query):
        """Generate data science-focused response"""
        responses = [
            "For optimal model performance, consider feature engineering and hyperparameter tuning. Ensemble methods often outperform single models.",
            "I recommend implementing automated data quality checks to ensure dataset integrity before analysis.",
            "Consider using time series analysis for temporal data. ARIMA or LSTM models work well for forecasting tasks.",
            "For imbalanced datasets, try SMOTE oversampling or weighted loss functions to improve minority class prediction."
        ]
        return f"📊 **Data Science Insight:** {random.choice(responses)}"

    def _it_chat_response(self, query):
        """Generate IT operations-focused response"""
        responses = [
            "To improve ticket resolution times, consider implementing a knowledge base and automated ticket routing.",
            "System monitoring should include CPU, memory, disk I/O, and network latency metrics for comprehensive oversight.",
            "Recommend implementing ITIL framework for better service management and incident tracking.",
            "For critical systems, ensure redundancy and failover mechanisms are in place and regularly tested."
        ]
        return f"⚙️ **IT Operations Advice:** {random.choice(responses)}"

    def _general_chat_response(self, query):
        """Generate general response"""
        responses = [
            "I'm here to help with cybersecurity, data science, and IT operations. How can I assist you today?",
            "As your multi-domain AI assistant, I can analyze threats, provide data insights, and optimize operations.",
            "For comprehensive intelligence, I integrate insights across security, data, and IT domains.",
            "Tell me about your specific challenge, and I'll provide targeted recommendations."
        ]
        return f"🤖 **AI Assistant:** {random.choice(responses)}"


# Initialize AI Assistant
ai_assistant = AIAssistant()

# ====================== LOGIN / REGISTER PAGE ======================
if not st.session_state.logged_in:
    st.title("Multi-Domain Intelligence Platform")
    st.markdown("### Secure Login Required")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_btn = st.form_submit_button("Log In", type="primary")

            if login_btn:
                if (username in st.session_state.users and
                        st.session_state.users[username] == password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"Welcome back, {username}!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    with tab2:
        with st.form("register_form"):
            new_user = st.text_input("Choose Username")
            new_pass = st.text_input("Choose Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")
            reg_btn = st.form_submit_button("Create Account")

            if reg_btn:
                if not new_user or not new_pass:
                    st.warning("Please fill all fields")
                elif new_pass != confirm:
                    st.error("Passwords do not match")
                elif new_user in st.session_state.users:
                    st.error("Username already exists")
                else:
                    st.session_state.users[new_user] = new_pass
                    st.success("Account created! Now log in.")
                    st.balloons()

# ====================== MAIN DASHBOARD (Protected) ======================
else:
    st.sidebar.title(f"User: {st.session_state.username}")
    page = st.sidebar.radio("Navigation", [
        "Dashboard Overview",
        "Cybersecurity",
        "IT Operations",
        "Data Science",
        "AI Assistant",
        "Settings"
    ])

    if st.sidebar.button("Logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.chat_history = []
        st.rerun()

    st.title("Multi-Domain Intelligence Platform")

    if page == "Dashboard Overview":
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            # Active threats (incidents not resolved or closed)
            active_incidents = len(incidents_df[
                                       ~incidents_df['status'].isin(['Resolved', 'Closed'])
                                   ])
            st.metric("Active Threats", active_incidents)

        with col2:
            # Open tickets
            open_tickets = len(tickets_df[
                                   tickets_df['status'] == 'Open'
                                   ])
            st.metric("Open Tickets", open_tickets)

        with col3:
            # Total datasets
            total_datasets = len(datasets_df)
            st.metric("Datasets", total_datasets)

        with col4:
            # Average resolution time
            resolved_tickets = tickets_df[tickets_df['status'] == 'Resolved']
            avg_resolution = resolved_tickets['resolution_time_hours'].mean() if not resolved_tickets.empty else 0
            st.metric("Avg Resolution Time", f"{avg_resolution:.1f}h")

        st.divider()

        # Row 2: Charts
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Threat Severity Distribution")
            if not incidents_df.empty:
                fig = px.pie(
                    incidents_df,
                    names="severity",
                    title="Cyber Incidents by Severity",
                    color_discrete_sequence=px.colors.sequential.Reds
                )
                st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Ticket Priority Distribution")
            if not tickets_df.empty:
                fig2 = px.pie(
                    tickets_df,
                    names="priority",
                    title="IT Tickets by Priority",
                    color_discrete_map={
                        'Critical': 'darkred',
                        'High': 'red',
                        'Medium': 'orange',
                        'Low': 'green'
                    }
                )
                st.plotly_chart(fig2, use_container_width=True)

        # AI Cross-Domain Insights
        st.divider()
        st.subheader("🤖 AI Cross-Domain Insights")

        cross_domain_insights = ai_assistant.get_cross_domain_insights(incidents_df, datasets_df, tickets_df)
        st.info(cross_domain_insights)

        # Recent Activity
        st.divider()
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Recent Cyber Incidents")
            recent_incidents = incidents_df.sort_values('timestamp', ascending=False).head(5)
            st.dataframe(recent_incidents[['timestamp', 'severity', 'category', 'status']],
                         use_container_width=True)

            # AI Analysis for top incident
            if not recent_incidents.empty:
                top_incident = recent_incidents.iloc[0]
                analysis = ai_assistant.analyze_threat({
                    'severity': top_incident['severity'],
                    'category': top_incident['category']
                })
                with st.expander(f"AI Analysis for {top_incident['incident_id']}"):
                    st.markdown(analysis)

        with col2:
            st.subheader("Recent IT Tickets")
            recent_tickets = tickets_df.sort_values('created_at', ascending=False).head(5)
            st.dataframe(recent_tickets[['created_at', 'priority', 'status', 'assigned_to']],
                         use_container_width=True)

            # AI Analysis for top ticket
            if not recent_tickets.empty:
                top_ticket = recent_tickets.iloc[0]
                analysis = ai_assistant.analyze_ticket({
                    'priority': top_ticket['priority'],
                    'status': top_ticket['status'],
                    'resolution_time_hours': top_ticket.get('resolution_time_hours', 0)
                })
                with st.expander(f"AI Analysis for {top_ticket['ticket_id']}"):
                    st.markdown(analysis)

    elif page == "Cybersecurity":
        st.header("Cybersecurity Monitoring")

        # AI Analysis Section
        with st.expander("🤖 AI Threat Analysis", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                test_severity = st.selectbox("Test Severity", ["Low", "Medium", "High", "Critical"], key="ai_severity")
                test_category = st.selectbox("Test Category",
                                             ["Phishing", "Malware", "DDoS", "Unauthorized Access", "Data Breach"],
                                             key="ai_category")

            if st.button("Generate AI Analysis", key="gen_ai_analysis"):
                analysis = ai_assistant.analyze_threat({
                    'severity': test_severity,
                    'category': test_category
                })
                st.markdown(analysis)

        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_incidents = len(incidents_df)
            st.metric("Total Incidents", total_incidents)
        with col2:
            phishing_count = len(incidents_df[incidents_df['category'] == 'Phishing'])
            st.metric("Phishing Attacks", phishing_count)
        with col3:
            open_incidents = len(incidents_df[incidents_df['status'] == 'Open'])
            st.metric("Open Incidents", open_incidents)
        with col4:
            critical_count = len(incidents_df[incidents_df['severity'] == 'Critical'])
            st.metric("Critical Threats", critical_count)

        # Visualizations
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Incidents by Category")
            category_counts = incidents_df['category'].value_counts()
            fig = px.bar(
                x=category_counts.index,
                y=category_counts.values,
                title="Incident Categories",
                labels={'x': 'Category', 'y': 'Count'}
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Incidents by Status")
            status_counts = incidents_df['status'].value_counts()
            fig = px.pie(
                values=status_counts.values,
                names=status_counts.index,
                title="Incident Status Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Incident reporting
        with st.expander("Report New Incident", expanded=False):
            with st.form("new_incident"):
                title = st.text_input("Incident Title")
                severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
                category = st.selectbox("Category",
                                        ["Phishing", "Malware", "DDoS", "Unauthorized Access", "Misconfiguration",
                                         "Other"])
                status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
                description = st.text_area("Description")
                submitted = st.form_submit_button("Add Incident")

                if submitted and title:
                    new_id = incidents_df['incident_id'].max() + 1 if not incidents_df.empty else 1000
                    new_row = pd.DataFrame([{
                        "incident_id": new_id,
                        "timestamp": datetime.now(),
                        "severity": severity,
                        "category": category,
                        "status": status,
                        "description": description
                    }])
                    incidents_df = pd.concat([incidents_df, new_row], ignore_index=True)

                    # AI Analysis of new incident
                    analysis = ai_assistant.analyze_threat({
                        'severity': severity,
                        'category': category,
                        'description': description
                    })

                    st.success("Incident added!")
                    st.info("🤖 **AI Analysis:**")
                    st.markdown(analysis)
                    st.rerun()

        # Data table with AI insights
        st.subheader("All Cyber Incidents")

        if not incidents_df.empty:
            # Add AI insights column
            display_df = incidents_df.copy()

            # Show incidents with AI button
            for idx, row in display_df.iterrows():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{row['incident_id']}** - {row['severity']} {row['category']}")
                    st.write(f"Status: {row['status']} | {row['timestamp']}")
                    st.write(f"{row['description'][:100]}..." if len(row['description']) > 100 else row['description'])
                with col2:
                    if st.button("🤖 Analyze", key=f"ai_btn_{idx}"):
                        analysis = ai_assistant.analyze_threat({
                            'severity': row['severity'],
                            'category': row['category'],
                            'description': row['description']
                        })
                        st.info(analysis)
                st.divider()
        else:
            st.info("No incidents found in database.")

    elif page == "IT Operations":
        st.header("IT Operations & Support")

        # AI Optimization Section
        with st.expander("🤖 AI Operations Optimization", expanded=False):
            st.markdown("### AI-Powered Ticket Analysis")

            if not tickets_df.empty:
                # Analyze ticket patterns
                high_priority = len(tickets_df[tickets_df['priority'].isin(['High', 'Critical'])])
                overdue = len(tickets_df[tickets_df['resolution_time_hours'] > 72])

                insights = []
                if high_priority > 5:
                    insights.append(
                        f"🔴 **High Workload:** {high_priority} high/critical tickets - consider resource allocation")
                if overdue > 0:
                    insights.append(f"⏰ **SLA Risks:** {overdue} tickets exceed 72-hour resolution - review processes")

                if insights:
                    for insight in insights:
                        st.warning(insight)
                else:
                    st.success("✅ Operations within optimal parameters")

            # AI Recommendations
            st.markdown("### AI Recommendations")
            rec_col1, rec_col2 = st.columns(2)
            with rec_col1:
                st.info("""
                **Automation Opportunities:**
                • Automate password resets
                • Implement chatbot for L1 support
                • Auto-assign tickets by category
                """)
            with rec_col2:
                st.info("""
                **Process Improvements:**
                • Standardize resolution procedures
                • Implement knowledge base
                • Regular SLA reviews
                """)

        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_tickets = len(tickets_df)
            st.metric("Total Tickets", total_tickets)
        with col2:
            avg_resolution = tickets_df[tickets_df['status'] == 'Resolved']['resolution_time_hours'].mean()
            st.metric("Avg Resolution Time", f"{avg_resolution:.1f}h")
        with col3:
            open_tickets = len(tickets_df[tickets_df['status'] == 'Open'])
            st.metric("Open Tickets", open_tickets)
        with col4:
            critical_tickets = len(tickets_df[tickets_df['priority'] == 'Critical'])
            st.metric("Critical Tickets", critical_tickets)

        # Visualizations
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Tickets by Priority")
            priority_counts = tickets_df['priority'].value_counts()
            fig = px.bar(
                x=priority_counts.index,
                y=priority_counts.values,
                title="Ticket Priority Distribution",
                color=priority_counts.index,
                color_discrete_map={
                    'Critical': 'darkred',
                    'High': 'red',
                    'Medium': 'orange',
                    'Low': 'green'
                }
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Resolution Time by Priority")
            resolution_stats = tickets_df.groupby('priority')['resolution_time_hours'].mean().reset_index()
            fig = px.bar(
                resolution_stats,
                x='priority',
                y='resolution_time_hours',
                title="Average Resolution Time by Priority",
                color='priority',
                color_discrete_map={
                    'Critical': 'darkred',
                    'High': 'red',
                    'Medium': 'orange',
                    'Low': 'green'
                }
            )
            st.plotly_chart(fig, use_container_width=True)

        # Support team performance with AI insights
        st.subheader("Support Team Performance")
        team_stats = tickets_df.groupby('assigned_to').agg({
            'ticket_id': 'count',
            'resolution_time_hours': 'mean'
        }).reset_index()
        team_stats.columns = ['Support Agent', 'Tickets Handled', 'Avg Resolution Time (hours)']

        col1, col2 = st.columns([2, 1])
        with col1:
            st.dataframe(team_stats, use_container_width=True)

            # AI insights on team performance
            if not team_stats.empty:
                best_agent = team_stats.loc[team_stats['Tickets Handled'].idxmax()]
                fastest_agent = team_stats.loc[team_stats['Avg Resolution Time (hours)'].idxmin()]

                st.info(f"🤖 **AI Insights:**")
                st.write(
                    f"• **Top Performer:** {best_agent['Support Agent']} handled {best_agent['Tickets Handled']} tickets")
                st.write(
                    f"• **Fastest Resolver:** {fastest_agent['Support Agent']} averages {fastest_agent['Avg Resolution Time (hours)']:.1f} hours")

        with col2:
            st.subheader("AI Quick Analysis")
            selected_agent = st.selectbox("Select Agent", team_stats['Support Agent'].unique())
            if selected_agent:
                agent_data = team_stats[team_stats['Support Agent'] == selected_agent].iloc[0]
                analysis = ai_assistant.analyze_ticket({
                    'priority': 'Medium',  # Default for analysis
                    'status': 'Resolved',
                    'resolution_time_hours': agent_data['Avg Resolution Time (hours)']
                })
                st.markdown(analysis)

        # Data table
        st.subheader("All IT Tickets")
        st.dataframe(tickets_df, use_container_width=True)

    elif page == "Data Science":
        st.header("Data Science & Analytics")

        # AI Analysis Section
        with st.expander("🤖 AI Dataset Analysis", expanded=False):
            selected_dataset = st.selectbox("Select Dataset for AI Analysis", datasets_df['name'].unique())
            if selected_dataset:
                dataset_info = datasets_df[datasets_df['name'] == selected_dataset].iloc[0]
                analysis = ai_assistant.analyze_dataset({
                    'name': dataset_info['name'],
                    'rows': dataset_info['rows'],
                    'columns': dataset_info['columns']
                })
                st.markdown(analysis)

        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_rows = datasets_df['rows'].sum()
            st.metric("Total Rows", f"{total_rows:,}")
        with col2:
            avg_columns = datasets_df['columns'].mean()
            st.metric("Avg Columns", f"{avg_columns:.1f}")
        with col3:
            total_datasets = len(datasets_df)
            st.metric("Datasets", total_datasets)
        with col4:
            recent_uploads = len(datasets_df[datasets_df['upload_date'] > '2024-08-01'])
            st.metric("Recent Uploads", recent_uploads)

        # Dataset analysis
        st.subheader("Dataset Overview")
        col1, col2 = st.columns(2)

        with col1:
            # Dataset size visualization
            fig = px.bar(
                datasets_df,
                x='name',
                y='rows',
                title="Dataset Size (Rows)",
                color='rows',
                color_continuous_scale='viridis'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Upload trend
            datasets_df['upload_date'] = pd.to_datetime(datasets_df['upload_date'])
            upload_counts = datasets_df.groupby(datasets_df['upload_date'].dt.to_period('M')).size()
            upload_counts.index = upload_counts.index.astype(str)

            fig = px.line(
                x=upload_counts.index,
                y=upload_counts.values,
                title="Dataset Upload Trend",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        # Uploader analysis with AI insights
        st.subheader("Uploader Analysis")
        uploader_stats = datasets_df.groupby('uploaded_by').agg({
            'dataset_id': 'count',
            'rows': 'sum',
            'columns': 'mean'
        }).reset_index()
        uploader_stats.columns = ['Uploader', 'Datasets Uploaded', 'Total Rows', 'Avg Columns']

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(uploader_stats, use_container_width=True)

            # AI insights
            if not uploader_stats.empty:
                top_uploader = uploader_stats.loc[uploader_stats['Datasets Uploaded'].idxmax()]
                st.info(
                    f"🤖 **AI Insight:** {top_uploader['Uploader']} is the most active uploader with {top_uploader['Datasets Uploaded']} datasets")

        with col2:
            fig = px.pie(
                uploader_stats,
                values='Datasets Uploaded',
                names='Uploader',
                title="Datasets by Uploader"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Data table with expanded view
        st.subheader("All Datasets")

        with st.expander("Dataset Details", expanded=True):
            # Add some calculated fields for better insights
            display_df = datasets_df.copy()
            display_df['size_mb'] = (display_df['rows'] * display_df['columns'] * 8) / (1024 * 1024)  # Approximate size
            display_df['size_mb'] = display_df['size_mb'].round(2)
            display_df['upload_date'] = pd.to_datetime(display_df['upload_date']).dt.strftime('%Y-%m-%d')

            st.dataframe(display_df, use_container_width=True)

            # Summary statistics with AI recommendations
            st.subheader("Dataset Statistics & AI Recommendations")
            col1, col2, col3 = st.columns(3)
            with col1:
                total_size = display_df['size_mb'].sum()
                st.metric("Total Size", f"{total_size:.1f} MB")
                if total_size > 1000:
                    st.info("🤖 Consider data archiving strategy")

            with col2:
                largest_dataset = display_df['rows'].max()
                st.metric("Largest Dataset", f"{largest_dataset:,} rows")
                if largest_dataset > 1000000:
                    st.info("🤖 Optimize with distributed processing")

            with col3:
                most_features = display_df['columns'].max()
                st.metric("Most Features", f"{most_features} columns")
                if most_features > 50:
                    st.info("🤖 Apply dimensionality reduction")

    elif page == "AI Assistant":
        st.header("🤖 AI Assistant")

        # Introduction
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("""
            ### Welcome to your AI Assistant!

            I'm here to help you with:
            - **Cybersecurity Threat Analysis** 🛡️
            - **Data Science Insights** 📊
            - **IT Operations Optimization** ⚙️
            - **Cross-Domain Intelligence** 🔄

            Ask me anything about your data and operations!
            """)

        with col2:
            st.metric("AI Version", "2.0")
            st.metric("Domains", "3")
            st.metric("Response Time", "<1s")

        # Chat Interface
        st.markdown("---")
        st.subheader("💬 Chat with AI Assistant")

        # Display chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(
                    f'<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin: 5px 0;">'
                    f'<strong>🤖 AI:</strong> {message["content"]}</div>',
                    unsafe_allow_html=True)

        # Chat input
        col1, col2 = st.columns([4, 1])
        with col1:
            user_input = st.text_input("Type your message:", placeholder="Ask me about threats, data, or operations...",
                                       key="chat_input")
        with col2:
            send_button = st.button("Send", type="primary", use_container_width=True)

        if send_button and user_input:
            # Add user message to history
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Generate AI response
            response = ai_assistant.chat_response(user_input)

            # Add AI response to history
            st.session_state.chat_history.append({"role": "ai", "content": response})

            # Clear input and rerun
            st.rerun()

        # Quick Analysis Buttons
        st.markdown("---")
        st.subheader("⚡ Quick Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Analyze Security Threats", use_container_width=True):
                analysis = ai_assistant.get_cross_domain_insights(incidents_df, datasets_df, tickets_df)
                st.session_state.chat_history.append({"role": "ai", "content": analysis})
                st.rerun()

        with col2:
            if st.button("Optimize IT Operations", use_container_width=True):
                if not tickets_df.empty:
                    insights = []
                    high_priority = len(tickets_df[tickets_df['priority'].isin(['High', 'Critical'])])
                    avg_resolution = tickets_df[tickets_df['status'] == 'Resolved']['resolution_time_hours'].mean()

                    insights.append(f"**IT Operations Analysis:**")
                    insights.append(f"• {high_priority} high/critical tickets")
                    insights.append(f"• Average resolution: {avg_resolution:.1f} hours")
                    insights.append(f"• Recommendations: Automate L1 support, implement knowledge base")

                    response = "\n".join(insights)
                    st.session_state.chat_history.append({"role": "ai", "content": response})
                    st.rerun()

        with col3:
            if st.button("Data Insights", use_container_width=True):
                if not datasets_df.empty:
                    total_rows = datasets_df['rows'].sum()
                    largest = datasets_df['rows'].max()
                    response = f"**Data Insights:**\n• {len(datasets_df)} datasets\n• {total_rows:,} total rows\n• Largest dataset: {largest:,} rows\n• Recommendations: Implement data quality monitoring"
                    st.session_state.chat_history.append({"role": "ai", "content": response})
                    st.rerun()

        # Domain-Specific Analysis
        st.markdown("---")
        st.subheader("🎯 Domain-Specific Analysis")

        tab1, tab2, tab3 = st.tabs(["Security", "Data", "Operations"])

        with tab1:
            st.markdown("### Security Threat Analysis")
            severity = st.select_slider("Threat Severity", ["Low", "Medium", "High", "Critical"], value="Medium")
            category = st.selectbox("Threat Category", ["Phishing", "Malware", "DDoS", "Unauthorized Access"])

            if st.button("Generate Security Analysis", key="security_ai"):
                analysis = ai_assistant.analyze_threat({
                    'severity': severity,
                    'category': category
                })
                st.info(analysis)

        with tab2:
            st.markdown("### Dataset Analysis")
            selected_ds = st.selectbox("Select Dataset", datasets_df['name'].unique())
            if selected_ds:
                ds_info = datasets_df[datasets_df['name'] == selected_ds].iloc[0]

                if st.button("Analyze Dataset", key="data_ai"):
                    analysis = ai_assistant.analyze_dataset({
                        'name': ds_info['name'],
                        'rows': ds_info['rows'],
                        'columns': ds_info['columns']
                    })
                    st.info(analysis)

        with tab3:
            st.markdown("### Ticket Analysis")
            priority = st.selectbox("Ticket Priority", ["Low", "Medium", "High", "Critical"])
            status = st.selectbox("Ticket Status", ["Open", "In Progress", "Resolved", "Closed"])

            if st.button("Analyze Ticket", key="ticket_ai"):
                analysis = ai_assistant.analyze_ticket({
                    'priority': priority,
                    'status': status
                })
                st.info(analysis)

        # Clear Chat Button
        st.markdown("---")
        if st.button("Clear Chat History", type="secondary"):
            st.session_state.chat_history = []
            st.rerun()

    elif page == "Settings":
        st.header("Settings & Profile")
        st.write(f"Logged in as: **{st.session_state.username}**")

        # AI Settings
        with st.expander("AI Assistant Settings", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                ai_detail_level = st.select_slider(
                    "AI Detail Level",
                    options=["Basic", "Detailed", "Advanced"],
                    value="Detailed"
                )
                ai_response_speed = st.select_slider(
                    "AI Response Speed",
                    options=["Fast", "Balanced", "Thorough"],
                    value="Balanced"
                )

            with col2:
                enable_security_ai = st.checkbox("Enable Security AI", value=True)
                enable_data_ai = st.checkbox("Enable Data Science AI", value=True)
                enable_it_ai = st.checkbox("Enable IT Operations AI", value=True)

            if st.button("Save AI Settings", type="primary"):
                st.success("AI settings saved successfully!")

        st.info("This is a demo app. In production, passwords would be hashed and stored in a database.")

        # AI Capabilities Info
        st.markdown("---")
        st.subheader("AI Assistant Capabilities")

        capabilities = {
            "Cybersecurity": ["Threat analysis", "Risk assessment", "Incident response recommendations",
                              "Security policy suggestions"],
            "Data Science": ["Dataset analysis", "ML model recommendations", "Data quality assessment",
                             "Feature engineering suggestions"],
            "IT Operations": ["Ticket prioritization", "SLA analysis", "Process optimization",
                              "Automation recommendations"]
        }

        for domain, caps in capabilities.items():
            with st.expander(f"{domain} AI Capabilities"):
                for cap in caps:
                    st.write(f"• {cap}")

    # Footer
    st.divider()
    st.caption(
        "CST1510 Coursework 2 • Intelligence Platform • DESIGNED BY • Ano_Kay • M01037211")

