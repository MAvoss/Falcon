import pandas as pd
from selenium import webdriver

# Create an empty dataframe
df = pd.DataFrame()

# Define the Google Sheets document ID and sheet name
SHEET_ID = 'YOUR SHEET ID HERE'
SHEET_NAME = 'YOUR SHEET NAME HERE'

# Construct the URL to access the Google Sheets document as a CSV
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

# Load the CSV data into the dataframe
df = pd.read_csv(url)

# Clean up the column names by capitalizing them, replacing spaces with underscores, and removing special characters
df.columns = map(str.title, df.columns)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('[^a-zA-Z_]', '', regex=True)

# Clean up the data by replacing non-alphanumeric characters with spaces
df = df.replace('[^0-9a-zA-Z,_-]+', ' ', regex=True)

# Display the cleaned data
display(df)

# Set the path to your user profile directory
USER_PROFILE_DIR = r'YOUR USER PROFILE DIRECTORY HERE'

# Set Chrome options to use the current user profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-data-dir={USER_PROFILE_DIR}')

# Open a new Chrome browser window using the current user profile
driver = webdriver.Chrome(options=chrome_options)

# Loop through each row of the dataframe
for index, row in df.iterrows():
    # Get the search term from the first column of the row
    search_term = row[0]

    # Navigate to Google and enter the search term
    driver.get('https://www.google.com/')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(search_term)
    search_box.submit()

    # Extract the search results
    search_results = driver.find_elements_by_css_selector('div.g')

    # Print the search results
    print(f"Search results for '{search_term}':")
    for result in search_results:
        print(result.text)
    print()

# Close the browser window
driver.quit()

# Note: This code is for educational purposes only and may violate Google's terms of service. Scraping search results from Google may be prohibited by Google, and could result in legal consequences. Please use caution and ensure that your use of this code is legal and ethical.
