import pandas as pd
import requests

# Target URL (Using SIH 2025 screening batch 1 as an example)
url = "https://www.sih.gov.in/sih2025/screeningresult-batch1"

# Mimic a real browser to prevent the server from blocking the script
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Fetching data from the SIH portal...")
response = requests.get(url, headers=headers)

# pd.read_html searches the HTML string for  tags
print("Extracting tables...")
tables = pd.read_html(response.text)

# The main data is usually the first table on the page (index 0)
df = tables[0]

# Save the dataframe locally as a clean CSV file
df.to_csv("SIH_2025_Ideas.csv", index=False)
print(f"Success! {len(df)} rows saved to SIH_2025_Ideas.csv.")