import pandas as pd

# List of input files
input_files = ['Sol_pan_comp.csv', 'EF_comp.csv']
# List of sensitive columns to remove
columns_to_remove = ['Project number', 'Granted support', 'Home address', 'Energy audit number']

def anonymize_column_values(df, column_name, label_prefix):
    """
    Anonymize a column by replacing its unique values with sequential anonymized labels.
    """
    if column_name in df.columns:
        unique_values = df[column_name].dropna().unique()
        mapping = {value: f"{label_prefix}{i+1}" for i, value in enumerate(unique_values)}
        df[column_name] = df[column_name].map(mapping).fillna(df[column_name])

def remove_sensitive_data_from_files(input_files):
    for file in input_files:
        try:
            # Load the CSV file into a DataFrame
            print(f"Processing file: {file}")
            df = pd.read_csv(file)

            # Remove sensitive columns if they exist
            df_cleaned = df.drop(columns=[col for col in columns_to_remove if col in df.columns])

            # Check if "The date" column exists and modify its values to only include the year
            if 'The date' in df_cleaned.columns:
                print('The date column exists')
                df_cleaned['The date'] = df_cleaned['The date'].str.extract(r'(\d{4})', expand=False)
            
            if 'The data' in df_cleaned.columns:
                print('The data column exists')
                df_cleaned['The data'] = df_cleaned['The data'].str.extract(r'(\d{4})', expand=False)

             # Anonymize "The town/village" and "County/City" columns
            anonymize_column_values(df_cleaned, 'The town/village', 'town')
            anonymize_column_values(df_cleaned, 'County/City', 'county')

            print(f'{file}_columns: {df_cleaned.head(1)}')


            # Save the cleaned file with a '_redacted.csv' suffix
            output_file = file.replace('.csv', '_redacted.csv')
            df_cleaned.to_csv(output_file, index=False)

            print(f"Sensitive data removed. Cleaned file saved as: {output_file}")
        except Exception as e:
            print(f"An error occurred while processing {file}: {e}")

# Run the function
remove_sensitive_data_from_files(input_files)
# rename_country_town_labels()
