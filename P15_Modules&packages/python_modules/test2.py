import importlib

module_name = "string_utils"
string_utils = importlib.import_module(f"utils.{module_name}")

text = 'Python is lovely'

result = string_utils.to_uppercase(text)
print(f"Uppercase: {result}")