from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
import streamlit as st
import pandas as pd
import gspread
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials

# Define Google Sheets API auth
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Load the Google Spreadsheet Data into a DataFrame
sheet = client.open("Test").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Calculate the 3 month moving average
df['Moving_Average_Spend'] = df['Average Spend'].rolling(window=3).mean()
df['Moving_Average_Transactions'] = df['Transactions'].rolling(window=3).mean()
df['Moving_Average_Guests'] = df['Guests'].rolling(window=3).mean()

# Streamlit App Layout
st.title('Marketing Data Dashboard')

st.header('Average Spend')
# Plot average spend
plt.figure(figsize=(10,5))
plt.plot(df.index, df['Average Spend'], marker='', color='green', linewidth=2, label="Average Spend")
plt.title('Average Spend Over Time')
plt.xlabel('Months')
plt.ylabel('Average Spend')
st.pyplot()

# Display the 3 month moving averages
st.header('3 Month Moving Averages')
st.markdown('**Average Spend:** ${}'.format(df['Moving_Average_Spend'].iloc[-1]))
st.markdown('**Transactions:** {}'.format(df['Moving_Average_Transactions'].iloc[-1]))
st.markdown('**Guests:** {}'.format(df['Moving_Average_Guests'].iloc[-1]))

# Add more sections as needed for other metrics (Transactions, Guests, etc.)
# ...
