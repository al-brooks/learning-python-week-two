import json

# Adding JSON read logic to test:

with open("pool_tables_activity.json") as file:
    pool_tables = json.load(file)

for table in pool_tables:
    print(table)