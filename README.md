UAC System Capacity & Care Load Analytics

Data-Driven Healthcare Capacity Monitoring Dashboard

An interactive healthcare analytics system for monitoring Unaccompanied Children (UAC) care load, CBP-HHS operational flow, workload growth, backlog pressure, and system volatility using Python and Streamlit.

---

📌 Project Overview

The UAC System Capacity & Care Load Analytics project analyzes operational data associated with the Unaccompanied Children (UAC) care system.

The system focuses on the operational pipeline:

Intake → CBP Custody → Transfer to HHS → HHS Care → Discharge

The objective is to transform raw operational records into meaningful healthcare capacity indicators and visual insights that can support workload monitoring, capacity planning, and data-driven decision-making.

The project uses historical operational data covering 2023–2025 and provides an interactive Streamlit dashboard for exploring system load and care-load trends.

---

🎯 Objectives

- Analyze UAC operational healthcare data.
- Monitor CBP and HHS care loads.
- Analyze transfers and discharges.
- Measure total system workload.
- Identify periods of increasing workload and accumulation pressure.
- Calculate healthcare-oriented KPIs.
- Analyze care-load growth and volatility.
- Provide an interactive dashboard for operational monitoring.
- Support data-driven capacity and workload planning.

---

📊 Dataset

The project uses daily UAC operational data covering 2023–2025.

The dataset contains information related to:

Feature| Description
"Date"| Reporting date
"Children Apprehended and Placed in CBP Custody"| Daily intake
"Children in CBP Custody"| Active CBP workload
"Children Transferred Out of CBP Custody"| Transfers into HHS
"Children in HHS Care"| Active HHS workload
"Children Discharged from HHS Care"| Daily HHS discharge

The dataset contains 1,170 rows, including blank records, with 720 valid reporting observations used for analysis.

---

🔄 Analytical Pipeline

Raw UAC Operational Data
          ↓
Data Loading
          ↓
Data Validation & Cleaning
          ↓
Time-Series Structuring
          ↓
Exploratory Data Analysis
          ↓
Feature Engineering
          ↓
Healthcare KPI Calculation
          ↓
Trend & Pressure Analysis
          ↓
Interactive Visualization
          ↓
Streamlit Dashboard

---

📈 Key Performance Indicators

1. Total System Load

Measures the combined active workload across CBP and HHS.

Total System Load =
Children in CBP Custody + Children in HHS Care

This provides an overall view of the number of children currently within the active care system.

---

2. Net Daily Intake

Measures the relationship between transfers into HHS and HHS discharges.

Net Daily Intake =
Transfers into HHS − HHS Discharges

A positive value indicates that transfers exceed discharges during the observation period, which may contribute to increasing workload.

---

3. Care Load Growth Rate

Measures the percentage change in system load over time.

Growth Rate (%) =
((Current Load − Previous Load) / Previous Load) × 100

This helps identify periods of increasing or decreasing care workload.

---

4. Backlog Accumulation Rate

Tracks sustained periods in which incoming workload exceeds outgoing workload.

Persistent positive net intake can indicate accumulation pressure within the system.

---

5. Discharge Offset Ratio

Measures how effectively discharge activity offsets transfers.

Discharge Offset Ratio =
Discharges / Transfers

A higher ratio indicates that discharge volume is more closely offsetting incoming transfers.

---

6. Care Load Volatility Index

Measures variation in active system workload over time.

Rolling statistical measures are used to identify periods of relatively stable or highly variable workload.

---

🔍 Exploratory Data Analysis

The project performs exploratory analysis to understand:

- Daily workload trends
- Monthly and yearly patterns
- CBP versus HHS load
- Intake and transfer activity
- Discharge patterns
- Net intake
- Care-load growth
- Workload volatility
- Potential anomalies
- Short- and medium-term trends

Rolling averages are used to smooth short-term fluctuations and identify broader workload patterns.

---

📉 Rolling Analysis

The project uses rolling statistical measures to identify workload trends.

7-Day Rolling Mean

Used to observe short-term changes in system load.

14-Day Rolling Mean

Used to identify medium-term workload trends.

Rolling Standard Deviation

Used to understand workload volatility and stability.

---

🚨 Pressure Analysis

Capacity pressure is treated as an analytical condition, not an official capacity breach.

Potential pressure periods are identified by combining signals such as:

- Positive net intake
- Increasing system load
- Sustained workload growth
- High backlog accumulation
- Increased volatility

The system therefore helps identify periods requiring further operational attention without claiming an official capacity violation.

---

🖥️ Dashboard

The project includes an interactive Streamlit dashboard.

Dashboard Features

- KPI summary cards
- Total system load visualization
- CBP vs HHS comparison
- Care-load growth analysis
- Net intake analysis
- Backlog monitoring
- Rolling trend analysis
- Date filtering
- Year/month filtering
- Daily/weekly/monthly analysis
- Interactive charts

---

🛠️ Technologies Used

Technology| Purpose
Python| Core programming
Pandas| Data processing
NumPy| Numerical analysis
Matplotlib| Visualization
Seaborn| Exploratory visualization
Plotly| Interactive charts
Statsmodels| Statistical analysis
Streamlit| Dashboard development
GitHub| Version control

---

📁 Project Structure

UAC-System-Capacity-Care-Load-Analytics/
│
├── data/
│   └── uac_operational_data.csv
│
├── app.py
│
├── analysis/
│   └── data_analysis.ipynb
│
├── requirements.txt
│
├── README.md
│
└── documentation/
    └── project_report.pdf

«Update the filenames above if your actual repository uses different names.»

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/Deasmita21/health-care.git
cd health-care

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

---

▶️ Run the Dashboard

Run the Streamlit application using:

streamlit run app.py

The dashboard will open in your browser at the local Streamlit address.

---

📦 Main Python Libraries

Example "requirements.txt":

pandas
numpy
matplotlib
seaborn
plotly
streamlit
statsmodels

---

📊 Key Analytical Findings

Analysis of the available dataset shows substantial variation in UAC system workload across the 2023–2025 period.

Key observations include:

- 720 valid reporting observations were available for analysis.
- Mean Total System Load was approximately 6,233 children.
- Maximum observed Total System Load was 11,762 children on December 20, 2023.
- Minimum observed Total System Load was approximately 2,002 children on August 24, 2025.
- Mean Net Daily Intake was approximately −44.7 children.
- The highest positive Net Daily Intake was 206 children on February 12, 2024.
- Total recorded HHS discharges exceeded total transfers across the complete set of valid observations.

These findings demonstrate significant changes in workload across the analyzed period.

---

🔮 Future Scope

The project can be extended through:

Predictive Forecasting

Machine-learning and time-series models can be used to forecast future care load, transfers, discharges, and pressure periods.

Real-Time Monitoring

The dashboard can be connected to continuously updated operational data.

Automated Alerts

Alerts can be introduced when backlog, workload growth, or volatility exceeds predefined thresholds.

Capacity-Aware Forecasting

Validated facility-capacity information could be incorporated to estimate actual capacity risk.

Cloud Deployment

The dashboard can be deployed on cloud platforms such as AWS or GCP for authorized stakeholder access.

Advanced Decision Support

Future versions could simulate how changes in transfers and discharge rates affect system workload.

---

⚠️ Limitations

- The analysis depends on the quality and completeness of the operational dataset.
- The dataset does not provide an explicit facility-capacity denominator.
- Therefore, the system identifies analytical pressure, not official capacity breaches.
- Historical trends alone cannot establish the causes of workload changes.
- Anomalies require domain review before correction or removal.
- The dashboard is a decision-support tool and does not replace official operational, medical, legal, or child-welfare procedures.

---

👩‍💻 Author

Debasmita Jana

B.Tech – Computer Science & Engineering
Specialization: Artificial Intelligence & Machine Learning

Role: Machine Learning Intern

---

📚 References

1. H. Vornhagen et al., “Design Practices for Data Dashboards in Health Care: Scoping Review,” Journal of Medical Internet Research, 2026.

2. G. van Hulzen et al., “Supporting Capacity Management Decisions in Healthcare Using Data-Driven Process Simulation,” Journal of Biomedical Informatics, vol. 129, 2022.

3. D. A. Martinez et al., “An Electronic Dashboard to Monitor Patient Flow at the Johns Hopkins Hospital,” Journal of Medical Systems, vol. 42, 2018.

4. S. S. Khairat et al., “The Impact of Visualization Dashboards on Quality of Care and Clinician Satisfaction,” JMIR Human Factors, 2018.

5. U.S. Department of Health and Human Services, Administration for Children and Families, Unaccompanied Children Program, Office of Refugee Resettlement.

6. W. McKinney, Python for Data Analysis, 3rd ed., O'Reilly Media, 2022.

7. G. James, D. Witten, T. Hastie, and R. Tibshirani, An Introduction to Statistical Learning, 2nd ed., Springer, 2021.

---

📄 Project Documentation

The complete research documentation contains detailed information about the dataset, methodology, KPI development, statistical analysis, results, limitations, and future scope.

---

⭐ Project Highlights

Healthcare Analytics • UAC Capacity Monitoring • Time-Series Analysis • KPI Development • Streamlit Dashboard • Data Visualization • Operational Decision Support