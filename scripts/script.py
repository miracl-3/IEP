import pandas as pd

# Load file
df = pd.read_excel("customer_data.xlsx")

# Convert timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Create complete timeline
full_range = pd.date_range(
    start='2024-01-01 00:00',
    end='2024-12-31 23:30',
    freq='30min'
)

full_df = pd.DataFrame({'Timestamp': full_range})

# Merge
merged = full_df.merge(df, on='Timestamp', how='left')

# Detect missing rows
missing = merged[merged['GROSS Consumption (kWh)'].isna()]

print("Missing rows:")
print(missing)

# Optional interpolation
merged['GROSS Consumption (kWh)'] = (
    merged['GROSS Consumption (kWh)']
    .interpolate()
)

# Save
merged.to_excel("cleaned_data.xlsx", index=False)