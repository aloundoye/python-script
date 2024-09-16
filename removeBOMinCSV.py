import os

# Function to remove BOM from a CSV file
def remove_bom_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove BOM if it exists
    cleaned_content = content.replace('\ufeff', '')
    
    # Overwrite the file with the cleaned content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# Function to loop through all CSV files in a directory and clean BOM
def remove_bom_from_csvs_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"Cleaning BOM from: {file_path}")
                remove_bom_from_file(file_path)

# Replace 'your_directory_path' with the path to your folder containing the CSV files
directory_path = '/Users/alassanendoye/Documents/Workspace/config-gandaki/cht-config/csv'  # Example: '/path/to/csv/folder'
remove_bom_from_csvs_in_directory(directory_path)