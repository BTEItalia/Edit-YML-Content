import yaml
import os

# Path to the folder containing the .yml files
folder_path = 'warps/'

# Function to process each YAML file
def process_yml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Modify the data as needed
    if data.get('world') == 'world':
        data['world'] = 'mondo'
    if 'y' in data:
        data['y'] -= 2016

    # Write the modified data back to the file
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

# Iterate over all the .yml files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.yml'):
        file_path = os.path.join(folder_path, filename)
        process_yml_file(file_path)

print("All YAML files have been processed!")
