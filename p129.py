import pandas as pd
import csv 
df = pd.read_csv("dwarf_stars.csv")

rows = []
with open("dwarf_stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(planet_data_rows)

planet_mass = []
planet_radius = []

for planet_data in planet_data_rows:
  planet_mass = planet_data[2]
 # planet_radius = planet_data[3]
  #print(planet_radius)
 # print(type(planet_radius))

planet_mass = float(planet_mass) * 0.000954588
try:
   planet_data[3] = float(planet_radius) * 0.102763 
except:
    pass
with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data_rows)

dataset_1 = []
dataset_2 = []
with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)
with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = dataset_1[0] + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])
with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)