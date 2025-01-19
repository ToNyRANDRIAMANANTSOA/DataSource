import json
import csv

# File paths
json_file_path = "../madagascar-map/liste_fokontany_par_commune_data.json"  # Update with the actual path to your JSON file
csv_file_path = "mg-flat-fokontany.csv"     # Update with the desired path to your CSV file

# Read the JSON file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Skip the first object (i.e., the structure of the data) and start from the real data
regions_data = {key: value for key, value in data.items() if key != "Region"}

# Open the CSV file for writing
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    csv_writer.writerow(["region", "district", "commune", "fokontany"])

    # Iterate through regions and communes to extract data
    for region, communes in regions_data.items():
        print(f"region: {region}")
        for commune_name, commune_data in communes.items():
            print(f"commune_name: {commune_name}")
            for entry in commune_data:
                csv_writer.writerow([
                    entry["region"],
                    entry["district"],
                    entry["commune"],
                    entry["fokontany"]
                ])

print(f"Data has been successfully written to {csv_file_path}")