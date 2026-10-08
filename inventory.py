import csv
def load_inventroy():
    items=[]
    with open ("inventory.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["reorder_threshold"] = int(row["reorder_threshold"])
            row["reorder_amount"] = int(row["reorder_amount"])
            items.append(row)
    return items

items=load_inventroy()
for item in items:
    print(item)

    