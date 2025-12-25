# Retail Daily Customer Count Analysis

## 📌 Project Overview
This project is a **Retail Analytics Web Application** built using Python. It allows shop owners or managers to upload their daily transaction data (CSV format) and instantly generates a comprehensive report.

The app uses **Data Science** techniques to clean the data, calculate key statistics (like average daily visitors and peak hours), and visualize trends using interactive charts.

## 🚀 Features
* **Automated Data Cleaning:** Automatically processes date formats and sorts data.
* **Statistical Analysis:** Calculates Mean, Median, Mode, and identifies the Peak Busy Day.
* **Gender Analysis:** Break down of customer demographics (Male vs. Female) and their spending habits.
* **Visualizations:** Generates 6 different types of charts:
    1.  Daily Customer Trend (Line Plot)
    2.  Monthly Footfall (Bar Plot)
    3.  Weekly Traffic Analysis (Bar Plot)
    4.  Gender Ratio (Pie Chart)
    5.  Sales by Gender (Bar Plot)
    6.  Product Category Preferences (Grouped Bar Chart)
* **User-Friendly Interface:** Built with **Gradio** for a simple drag-and-drop web experience.

## 🛠️ Technologies Used
* **Python:** Core programming language.
* **Pandas:** For data manipulation and analysis.
* **Matplotlib & Seaborn:** For creating static data visualizations.
* **Gradio:** For creating the web interface and frontend.

## ⚙️ Installation & Setup

### Prerequisites
Make sure you have Python installed on your system. You will need to install the required libraries before running the app.

### Step 1: Install Libraries
Open your terminal or command prompt and run:
```bash
pip install pandas matplotlib seaborn gradio
python app.py
Column Name,Data Type,Description
Date,Date (YYYY-MM-DD),The date of the transaction.
Gender,Text (Male/Female),The gender of the customer.
Total Amount,Number,The total money spent in that transaction.
Product Category,Text,"The type of item bought (e.g., Clothing, Electronics)."
Date,Gender,Total Amount,Product Category
2024-01-01,Female,1500,Clothing
2024-01-01,Male,500,Electronics
2024-01-02,Female,300,Home Decor
2024-01-02,Male,1200,Clothing
