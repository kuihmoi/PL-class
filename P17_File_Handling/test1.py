# with open('output_venv1.txt', 'r') as file:
#     content = file.read()
#     print("Content from venv2:")
#     print(content)

# import pandas as pd
# data = {
#     'A': [1, 2, 3, 4],
#     'B': [5, 6, 7, 8],
#     'C': [9, 10, 11, 12]
# }

# df = pd.DataFrame(data)
# df.to_csv('output.csv', index=False)
# print("CSV file created in venv1 with pandas")

#-------------------------------------------------------

# import csv

# with open('output.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     print("CSV read in venv2 with csv module")
#     for i in reader:
#         print(i)

#-------------------------------------------------------

# input_file = 'python.png'

# output_file = 'python_copy.png'

# try:
#     with open(input_file, 'rb') as source:
#         content = source.read()
#     with open(output_file, 'wb') as destination:
#         destination.write(content)
#         print('Binary file copied successfully.')
# except FileNotFoundError as e:
#     print(f'Error: {input_file} not found.')
# except PermissionError:
#     print('Error: Permission denied.')

#-------------------------------------------------------

# from PIL import Image
# import os

# img_path = 'python.png'

# image = Image.open(img_path)
# width, height = image.size

# f_s = os.path.getsize(img_path)
# print(f'image size: {f_s} bytes')

# f_s_k = f_s / 1024
# print(f'image size: {f_s_k: .2f} KB')

# width, height = image.size
# new_size = (int(width / 2), int(height / 2))
# resize_image = image.resize(new_size)
# resize_image.save('python_resized.png')

# print(f'Original size: {width} x {height}')
# print(f'Resized size: {new_size[0]} x {new_size[1]}')

# # i had to install pillow using
# # python -m pip install pillow (since im downloading in virtual environment)

# print(f'image size: {f_s_k: .2f} KB')
# print(f'resized image size: {os.path.getsize('python_resized.png') / 1024:.2f} KB')

#-------------------------------------------------------

# from datetime import datetime

# try:
#     with open('output_venv1.txt', 'a') as file:
#         file.write(f'\nAppended from venv2 on {datetime.now()}!\n')
#     print('Line appended in venv2.')
# except FileNotFoundError:
#     print('Error:" output_venv1.txt not found.')
# except IOError as e:
#     print(f'IOError: An I/O error occured {e}')

#-------------------------------------------------------

#JSON - used for storing and exchanging data (encode and decode JSON data)

import json
from datetime import datetime

def save_json(data, output_file='results.json'):
    try:
        import pandas as pd
        df = pd.DataFrame(data)
        summary = {
            'row_count': len(df),
            'columns': list(df.columns),
            'mean_age': df['Age'].mean() if 'Age' in df.columns else None,
            'pandas_version': pd.__version__,
            'datetime': datetime.now().isoformat()
        }
    except ImportError:
        summary = {
            'row_count': len(data),
            'columns': list(data.keys()),
            'mean_age': None,
            'pandas_version': 'N/A',
            'datetime': datetime.now().isoformat()
        }
    
    try:
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=4)
        print(f'Project results save to {output_file}')
    except Exception as e:
        print(f'Error saving project results: {e}')
        raise

data = {
    'Name': ['Alice', 'Bob', 'Charlies'],
    'Age' : [20, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

save_json(data, 'output.json')