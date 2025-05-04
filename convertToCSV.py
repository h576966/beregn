import pandas as pd

# Load the Excel file
df = pd.read_excel("Matvaretabellen 2024.xlsx", sheet_name="Matvarer", engine="openpyxl")

# Save to CSV
df.to_csv("Matvaretabellen.csv", index=False)
