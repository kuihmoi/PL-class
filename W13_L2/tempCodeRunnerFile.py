from datetime import date, datetime
import os
import json
SAMPLE_SALES = [
    {"date": "2024-01-05", "product": "Laptop",
     "region": "North", "units": 3, "price": 999},
     {"date": "2024-01-08", "product": "Phone",
     "region": "South", "units": 10, "price": 499},
     {"date": "2024-01-12", "product": "Tablet",
     "region": "East", "units": 5, "price": 329},
     {"date": "2024-01-15", "product": "Monitor",
     "region": "West", "units": 7, "price": 249},
     {"date": "2024-02-03", "product": "Laptop",
     "region": "East", "units": 4, "price": 999},
     {"date": "2024-02-07", "product": "Phone",
     "region": "North", "units": 12, "price": 499},
]

# 1) JSON DATA TYPES MAPPING
sample_config ={
    "app_name": "SalesTracker",
    "version": 2,
    "discount": 0.15,
    "active": True,
    "owner": None,
    "tags": ["sales", "demo"],
    "settings": {"theme": "dark"},
}

print("Python dict:")
for key, value in sample_config.items():
    print(f"{key:<12} -> {type(value).__name__:<8} value: {value!r}")

##########################################################################################
# 2_ Encoding: Python -> JSON string (json.dumps)
# 'dumps' = "dump to string"

# 2.1) Compact form (default) - smalles size, good for network transfer
compact_json = json.dumps(sample_config)
print("\nCompact JSON:")
print(" ", compact_json)

# 2.2) Pretty-printed - indented, human-readable
pretty_json = json.dumps(sample_config, indent=4)
print("\nPretty-printed JSON:")
print(pretty_json)

# 2.3) Sort keys alphabetically, useful for reproducible output or diffs
sorted_json = json.dumps(sample_config, indent=2, sort_keys=True)
print("\nSorted-keys JSON:")
print(sorted_json)

# 2.4) Compact separators, removes all optional whitespace
tiny_json = json.dumps(sample_config, separators=(",", ":"))
print("\nTiny (minimal separators):", tiny_json[:80], "...")

print(
    f"\nCompact size: {len(compact_json)} chars | Pretty size: {len(pretty_json)} chars"
)

##########################################################################################
# 3) Decoding: JSON string -> Python (json.loads)
# 'loads' = "load from string"

raw_json_string = '{"product": "Laptop", "price": 999, "in-stock": true, "tags": ["new", "sale"]}'

parsed = json.loads(raw_json_string)
print("\nOriginal JSON string:")
print(" ", raw_json_string)
print("\nAfter json.loads():")
print(f"  Type     : {type(parsed)}")
print(f"  product     : {parsed['product']!r}   (type: {type(parsed['product']).__name__})")
print(f"  price       : {parsed['price']!r}   (type: {type(parsed['price']).__name__})")
print(f"  in_stock    : {parsed['in-stock']!r}   (type: {type(parsed['in-stock']).__name__})")
print(f"  tags        : {parsed['tags']!r}   (type: {type(parsed['tags']).__name__})")

# Accessing nested values just like a normal dict / list
print(f"\n First tag: {parsed['tags'][0]}")

##########################################################################################
# 4) Saving JSON to a File (json.dump)
# 'dump' writes directly to an open file object

os.makedirs("output", exist_ok=True)

SALES_JSON_PATH = "output/sales.json"

with open(SALES_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(SAMPLE_SALES, f, indent=4)

print(f"\nSave {len(SAMPLE_SALES)} sales records to '{SALES_JSON_PATH}'")
file_size = os.path.getsize(SALES_JSON_PATH)
print(f"File size: {file_size} bytes")

# Read the raw text back to show what the file looks like
with open(SALES_JSON_PATH, "r", encoding="utf-8") as f:
    file_contents = f.read()
print("\nFile preview (first 300 chars):")
print(file_contents[:300])

##########################################################################################
# 5) Loading JSON from a file (json.load)
# 'load' reads from an open file object.

with open(SALES_JSON_PATH, "r", encoding="utf-8") as f:
    loaded_sales = json.load(f)

print(f"\nLoaded {len(loaded_sales)} records from '{SALES_JSON_PATH}'")
print(f"Type of result   : {type(loaded_sales)}")
print(f"Type of one row  : {type(loaded_sales[0])}")

print("\nLoaded records:")
print(f"  {'Date':<12} {'Product':10} {'Region':<8} {'Units':>5} {'Price':>7}")
print("  " + "-" * 48)
for row in loaded_sales:
    print(f"  {row['date']:<12} {row['product']:10} {row['region']:<8}"
          f" {row['units']:>5} ${row['price']:>6,}")
    
##########################################################################################
# 6) Nested JSON (Objects inside Objects)

company = {
    "name": "TechCorp",
    "headquarters": {
        "city": "Toronto",
        "country": "Canada",
        "coordinates": {"lat":43.65, "lon": -79.38},
    },
    "departments": [
        {"id": 1, "name": "Sales",      "headcount": 42},
        {"id": 2, "name": "Marketing",  "headcount": 18},
        {"id": 3, "name": "IT",         "headcount": 27},
    ],
    "active": True,
}

print("\nNested dict as JSON:")
print(json.dumps(company, indent=4))

# Accessing deeply nested values
city = company["headquarters"]["city"]
print(f"  City                 : {city}")

latitude = company["headquarters"]["coordinates"]["lat"]
print(f"  Latitude             : {latitude}")

first_dept = company["departments"][0]["name"]
print(f"  First department     : {first_dept}")

total_staff = sum(d["headcount"] for d in company["departments"])
print(f"  Total headcount      : {total_staff}")


##########################################################################################
# 7) Updating JSON Data

CONFIG_PATH = "output/config.json"

# Create an initial config file
default_config = {"theme": "light", "language": "en", "notifications": True}
with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    json.dump(default_config, f, indent=4)
print("Default config written:", default_config)

# Load, modify, and save back
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)
config["theme"] = "dark"          # update existing key
config["font_size"] = 14          # add new key
config.pop("notifications", None)     # remove a key safely

with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("Updated config saved  :", config)

##########################################################################################
# 8) Error Handling (json.JSONDecodeError)
# Invalid JSON raises json.JSONDecodeError, a sublcass of ValueError

