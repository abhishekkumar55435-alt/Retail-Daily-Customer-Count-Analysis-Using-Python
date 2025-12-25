import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

def simple_analysis(file_obj):
    # Step 1: Load the Data
    # We try to read the uploaded CSV file
    try:
        data = pd.read_csv(file_obj.name)
    except:
        return "Error: Could not read the file.", None

    # Step 2: Clean the Data
    # We need to make sure the 'Date' column is treated as actual dates, not text
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        # Sort the data from oldest to newest
        data = data.sort_values(by='Date')
    else:
        return "Error: Your CSV must have a 'Date' column.", None

    # Step 3: Count Customers Per Day
    # We group the data by Date and count the rows to see daily footfall
    daily_data = data.groupby('Date').size().reset_index(name='Count')

    # Step 4: Calculate Basic Statistics (The Math Part)
    
    # Calculate Mean (Average)
    avg_visitors = daily_data['Count'].mean()
    
    # Calculate Median (The middle number)
    median_visitors = daily_data['Count'].median()
    
    # Calculate Mode (The most common number)
    mode_visitors = daily_data['Count'].mode()[0]
    
    # Find the Busiest Day (Peak)
    max_visitors = daily_data['Count'].max()
    # Find the row where the count equals the max visitors
    peak_row = daily_data[daily_data['Count'] == max_visitors].iloc[0]
    peak_date = peak_row['Date'].date()

    # Step 5: Gender Analysis
    # Count how many Females vs Males
    gender_counts = data['Gender'].value_counts()
    
    # Calculate Total Sales by Gender (Summing up the money)
    gender_sales = data.groupby('Gender')['Total Amount'].sum()

    # Step 6: Create the Text Report
    # We use 'f-strings' to put our calculated numbers into the text
    report = f"""
    --- BASIC STATISTICS ---
    Average Daily Visitors: {avg_visitors:.2f}
    Median Daily Visitors: {median_visitors}
    Most Common Visitor Count (Mode): {mode_visitors}

    --- PEAK BUSY DAY ---
    Date: {peak_date}
    Total Customers: {max_visitors}

    --- GENDER INFO ---
    Female Customers: {gender_counts.get('Female', 0)}
    Male Customers: {gender_counts.get('Male', 0)}

    --- SALES BY GENDER (Rupees) ---
    Female Sales: ₹ {gender_sales.get('Female', 0)}
    Male Sales: ₹ {gender_sales.get('Male', 0)}
    """

    # Step 7: Create the Charts
    # We make a figure with 6 rows of charts
    figure, axes = plt.subplots(6, 1, figsize=(10, 30))

    # Chart 1: Line Plot (Daily Trend)
    sns.lineplot(data=daily_data, x='Date', y='Count', ax=axes[0], marker='o', color='blue')
    axes[0].set_title("1. Daily Customer Trend")
    axes[0].grid(True)

    # Chart 2: Bar Plot (Monthly Trend)
    # Extract month name from date
    data['Month'] = data['Date'].dt.month_name()
    # Define correct order of months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    monthly_data = data.groupby('Month').size().reindex(months_order)
    
    sns.barplot(x=monthly_data.index, y=monthly_data.values, ax=axes[1], palette='magma')
    axes[1].set_title("2. Customers by Month")

    # Chart 3: Bar Plot (Weekly Trend)
    daily_data['DayName'] = daily_data['Date'].dt.day_name()
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekly_avg = daily_data.groupby('DayName')['Count'].mean().reindex(days_order)

    sns.barplot(x=weekly_avg.index, y=weekly_avg.values, ax=axes[2], palette='viridis')
    axes[2].set_title("3. Average Customers by Day of Week")

    # Chart 4: Pie Chart (Gender Split)
    axes[3].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['pink', 'skyblue'])
    axes[3].set_title("4. Male vs Female Ratio")

    # Chart 5: Bar Plot (Sales by Gender in Rupees)
    sns.barplot(x=gender_sales.index, y=gender_sales.values, ax=axes[4])
    axes[4].set_title("5. Total Sales by Gender (Rupees)")
    axes[4].set_ylabel("Amount in ₹")

    # Chart 6: Bar Plot (What do they buy?)
    if 'Product Category' in data.columns:
        # Create a cross-table of Category vs Gender
        cat_gender_table = pd.crosstab(data['Product Category'], data['Gender'])
        cat_gender_table.plot(kind='bar', ax=axes[5])
        axes[5].set_title("6. Product Categories by Gender")
        axes[5].tick_params(axis='x', rotation=0)
    else:
        axes[5].text(0.5, 0.5, "No Category Data")

    # Make sure plots don't overlap
    plt.tight_layout()

    return report, figure

# Step 8: Build the App Interface
# This creates the web page for upload
my_app = gr.Interface(
    fn=simple_analysis,
    inputs=gr.File(label="Upload CSV File Here"),
    outputs=[
        gr.Textbox(label="Analysis Report", lines=15),
        gr.Plot(label="Charts")
    ],
    title="My Retail Analysis Project",
    description="Upload a store CSV file to see statistics and charts.",
    theme="soft"
)

# Run the App
if __name__ == "__main__":
    my_app.launch()