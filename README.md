# AngelOne-Portfolio-Dashboard-Powerbi

This is a **Portfolio Analysis Dashboard** created in Power BI.  
It shows insights into stock performance, asset allocation, and portfolio growth.

**Worksheet 1- Portfolio Insights**
## 🚀 Key Performance Indicators (Metrics)
- Portfolio Performance Metrics
- Investment KPIs
- Portfolio Valuation Metrics
- Stocks in Gain/Loss (% and value wise)
- Asset allocation breakdown - Sector/Industry wise
- Scatter plot- Avg Trading Price Vs Current Closing Price
- Slicer to filter the data by Capital Value of the Company- Small Cap, Mid Cap, Large Cap

**Worksheet 2- Trends**
## Shows the performance of invested shares over the specified period.
- Filter by Market Cap and Sector
Provide insights about each stock and establish correlation in stock price movement.

## 📂 Files
- 'Portfolio Analyzer AngelOne.pbix' - Power BI file
- 'Portfolio Analyzer AngelOne.pdf' - Exported pdf 
- 'PreProcessing_1.py' - Pre processing Python file
- 'Companies_with_tickers.csv' - Sample input file to Preprocessing_1.py
- 'nse_closing_prices.csv' - Ouput file from Preprocessing_1.py - Input to Power BI
- 'Holdings.csv'- Report file downloaded and edited to use in Power BI

## 📊 Data Handling and Preprocessing
**Step-1** **Prepare Holdings File*
1. Download Compiled final report from AngelOne app or website.
2. Create a new CSV and paste the data from Equity tab from Equity Holding Details onwards.
4. Add the Ticker column and add Ticker name of each Script and save the file as **Holdings.csv*.
5. The new csv should look like this:
   
<img width="1724" height="208" alt="image" src="https://github.com/user-attachments/assets/65d01ae1-2197-456f-abb6-b0cd944a95b0" />


**Step-2** **Prepare nse closing price history data*
Prerequisite- Prepare |Company|Ticker| csv file containing each company present in the Portfolio and it's respective Ticker value.

<img width="846" height="773" alt="image" src="https://github.com/user-attachments/assets/6dff72b7-ce1a-4b57-bd7e-958df646d405" />


1. Keep the python script **PreProcessing.py* in the same folder as csv file and run the script.
2. The history data of closing price can be customized according to user input. By default, it is 5 years. 
3. This generates a csv file named- **nse_closing_prices.csv* which is Input to Power BI.
   
Output csv file:
<img width="359" height="503" alt="image" src="https://github.com/user-attachments/assets/2321ac1b-6ef6-4191-b70d-372dc3faa6b2" />


**Step-2**
Now, we have 2 csv files prepared to load into Power BI.
Open .pbix file and load the data into the dashboard.

----------------------------------------------------------------------------------------------------------------
## Schema

<img width="940" height="749" alt="image" src="https://github.com/user-attachments/assets/05b83eea-270d-46fb-8c02-d4a4558d7806" />



## 📷 Preview


**Worksheet 1- Portfolio Insights**

<img width="1541" height="872" alt="image" src="https://github.com/user-attachments/assets/b7423e84-041b-4592-8fe8-a51e783ccfc9" />




**Worksheet 2- Trends**

<img width="1245" height="706" alt="image" src="https://github.com/user-attachments/assets/0d4a7060-2cf7-4cbd-b68c-bced5ee30e79" />



 













