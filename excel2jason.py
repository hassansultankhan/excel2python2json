import pandas as pd
import json

# Load the Excel file
excel_file = 'data.xlsx'  # Name of the Excel file
df = pd.read_excel(excel_file)

# Convert the DataFrame to a list of dictionaries
data_dict = df.to_dict(orient='records')

# Write the list of dictionaries to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data has been successfully written to output.json")
