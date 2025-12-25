## ⚙️ How to Run
1. **Clone:** `git clone https://github.com/iAbdullah/bootcamp_data.git`
2. **Setup:** `pip install pandas numpy plotly nbformat`
3. **Open:** `jupyter notebook notebooks/eda.ipynb`
# E-commerce Data Analysis Project 🚀

This repository contains a comprehensive **Exploratory Data Analysis (EDA)** of e-commerce order data, focusing on regional performance and statistical significance.

## 📊 Key Highlights
* **Data Cleaning:** Processed over 5,000 orders, including date formatting and outlier management (Winsorization).
* **Revenue Insights:** Identified UAE and Kuwait as the primary revenue drivers.
* **Trend Analysis:** Analyzed monthly seasonality to understand peak sales periods.
* **Statistical Testing:** Performed **Bootstrap comparison** to analyze refund rate differences between Saudi Arabia and UAE.

## 📁 Project Structure
* `notebooks/eda.ipynb`: The main analysis notebook with code and visualizations.
* `reports/figures/`: Exported charts (Bar charts, Histograms, Line trends).
* `data/`: Processed datasets used for the analysis.

## 🛠️ Tech Stack
* **Python** (Pandas, NumPy)
* **Plotly** (Interactive Visualizations)
* **Git/GitHub** (Version Control)

---
*Created as part of the AI Pros Bootcamp.*
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)


We compare the total revenue, number of orders, and Average Order Value (AOV) across different countries to identify the top-performing markets.


<img width="1371" height="570" alt="image" src="https://github.com/user-attachments/assets/26eb0655-70e8-4964-b4b2-f9465994a8f6" />


After auditing the data (5,250 rows) and performing exploratory data analysis (EDA), we found the following:

1. **Market Leadership:** The **UAE (AE)** and **Kuwait (KW)** are our strongest markets, contributing the highest total revenue.
2. **Growth Trends:** The monthly revenue analysis shows a steady trend with specific peaks, suggesting that our promotional periods are effective.
3. **Customer Behavior:** Most orders are within a consistent "typical" range as shown in the distribution, allowing for predictable inventory planning.
4. **Data Reliability:** By using **Winsorization**, we have ensured that our insights are not distorted by extreme outliers, providing a more realistic view of the business performance.

**Next Steps:**
* Investigate the factors driving high AOV in specific countries.
* Align marketing campaigns with the peak months identified in the trend analysis.


### Questions (Rule 2)
1. **Total Revenue by Country:** Which country generates the highest total revenue (using amount_winsor)?
2. **Order Volume over Time:** What is the monthly trend of order counts, and are there specific peak months?
3. **Average Order Value Comparison:** Is there a significant difference in the average transaction amount between the top two countries?


<img width="1365" height="560" alt="image" src="https://github.com/user-attachments/assets/db345927-6726-45fb-a6e5-f8c54f92f721" />


canclogn## Conclusion: Key Business Insights

Based on the Exploratory Data Analysis (EDA) of the orders data, we conclude the following:

* **Market Leadership:** The **UAE (AE)** is our primary revenue driver, followed by **Kuwait (KW)**. Marketing efforts should prioritize maintaining this lead while investigating growth opportunities in other GCC markets.
* **Temporal Trends:** Monthly revenue shows clear **seasonality**. The peaks identified in the trend line suggest that current promotional strategies are effective during those periods.
* **Order Consistency:** The distribution of order amounts is **right-skewed**, indicating that the majority of our revenue comes from a high volume of smaller "typical" orders rather than a few massive transactions.
* **Data Reliability:** By using **Winsorization**, we have ensured that our insights are robust and not skewed by extreme outliers, providing a realistic view for decision-making.

**Final Recommendation:** Maintain focus on the UAE market while exploring why certain months show lower performance to stabilize revenue year-round.



### Question 3: Distribution of Order Amounts (Rule )
In this section, we analyze the distribution of transaction values using a histogram to understand what a "typical" order look like and identify any remaining skewness.
<img width="1368" height="560" alt="image" src="https://github.com/user-attachments/assets/2e83318a-fcad-4f14-9b9e-62d3f5d4cf71" />

### Interpretation: Amount Distribution
* **Typical Order:** Most orders fall within the range of 50 to 150 (depending on your data), which represents the core customer segment.
* **Skewness:** The distribution remains **right-skewed**, indicating that while we have many small orders, there is a long tail of higher-value transactions.
* **Outlier Management:** By using the winsorized amount, we have successfully managed extreme values, making the chart easier to read and more representative of the business.



###  Total Revenue by Country 
In this section, we analyze which countries generate the most revenue using the winsorized amount to ensure outliers do not distort the rankings.

<img width="1362" height="564" alt="image" src="https://github.com/user-attachments/assets/ca2343fe-bbde-47f2-b684-592f1bde688f" />

### Interpretation: Revenue by Country
* **Market Leader:** The UAE (AE) stands out as the highest revenue-generating market, significantly leading other regions.
* **Secondary Markets:** Kuwait (KW) and Saudi Arabia (SA) show strong performance, while Qatar (QA) remains a growing market.
* **Revenue Stability:** Since we used `amount_winsor`, these results are reliable and not driven by single massive "whale" orders.

**Caveat:** This analysis only looks at total revenue; it does not account for the operational costs or marketing spend in each country.




### What does this mean?
* **The Result:** The difference is about **2%**.
* **Is it real?** No, because the interval **includes zero** (it goes from -0.017 to 0.059).
* **Final Word:** This means the difference between SA and AE is just a matter of luck/chance. Practically, they have the same refund rates.
  

  ## Final Summary
1. **Best Markets:** UAE and Kuwait are our "Big Players" in revenue.
2. **Sales Timing:** Sales go up and down depending on the month (Seasonality).
3. **Typical Order:** Most customers spend a similar amount, we don't have many crazy high or low orders.
4. **Refunds:** No real difference in refunds between Saudi and UAE.

**Conclusion:** The business is doing great in the UAE. We should keep doing what we're doing but keep an eye on the busy months!



## ⚙️ How to Run
Follow these steps to run the analysis on your local machine:

1. **Clone the repository:**
   `git clone https://github.com/iAbdullah/bootcamp_data.git`

2. **Navigate to the project folder:**
   `cd bootcamp_data`

3. **Install dependencies:**
   `pip install pandas numpy plotly nbformat`

4. **Run the Notebook:**
   `jupyter notebook notebooks/eda.ipynb`

# E-commerce Data Analysis Project 🚀

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

## 📊 Key Highlights
* **Data Cleaning:** Processed over 5,000 orders.
* **Statistical Testing:** Performed `Bootstrap comparison` for refund rates.








