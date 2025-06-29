import os
import pandas as pd

base_dir = r"cards"
columns_to_drop = ['_airbyte_ab_id', '_airbyte_emitted_at', 'source_file_path', '_airbyte_additional_properties']

print("Script started.")
print(" Base directory:", base_dir)

if not os.path.exists(base_dir):
    print(" ERROR: Base directory does not exist!")
    exit()

any_file_found = False

for file in os.listdir(base_dir):
    if file.lower().endswith(".xlsx"):
        any_file_found = True
        file_path = os.path.join(base_dir, file)
        print(f" Processing: {file_path}")
        try:
            df = pd.read_excel(file_path)
            cols_before = df.columns.tolist()
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)
            df.to_excel(file_path, index=False)
            cols_after = df.columns.tolist()
            print(f" Cleaned: {file_path}")
            print(f"   Removed columns: {set(cols_before) - set(cols_after)}")
        except Exception as e:
            print(f" Error: {file_path} — {e}")

if not any_file_found:
    print("No .xlsx files found in the base directory.")
