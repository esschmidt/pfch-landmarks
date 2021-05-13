### This script loops through a dataset of NYC landmarked buildings to find common characteristics of historic buildings

import csv

borough_count = {}
material_count = {}
decades = []
decades_count = {}
use_type_count = {}

#List of most prominent primary building material types for looping (manually collected by examining the Mat_Prim column in OpenRefine)
material_terms = ["Aluminum", "Ashlar", "Brick", "Bronze", "Brownstone", "Iron", "Clapboard", "Concrete", "Fieldstone", "Glass", "Glass", "Granite", "Limestone", "Marble", "Masonry", "Not determined", "Sandstone", "Schist", "Steel", "Stone", "Stucco", "Terra Cotta", "Wood"]

with open("landmarks_dataset_final.csv", "r") as datafile:
    processed_csv = csv.DictReader(datafile)
    for row in processed_csv:

        #Create a dictionary of the number of landmarked buildings in each borough
        borough = row["Borough"]
        if borough not in borough_count:
            borough_count[borough] = 0
        borough_count[borough] +=1

        #Create a dictionary of the primary building material of each landmarked building (using the list defined above)
        material = row["Mat_Prim"]
        for term in material_terms:
            if term in material:
                if term not in material_count:
                    material_count[term] = 0
                material_count[term] +=1

        #Create of list of the decade built from the year built date, to allow for grouping by decade
        year = row["Date_Low"]
        if not year:
            decade = "Unknown"
        elif year == "0.0":
            decade = "Unknown"
        else:
            # decade = str(year)[0:3] + "0s"
            decade = "".join([str(year)[0:3],"0s"])
        decades.append(decade)

        #Create a dictionary of the number of landmarked buildings built in each decade
        if decade not in decades_count:
            decades_count[decade] = 0
        decades_count[decade] +=1

        #Create a dictionary of building types, accounting for the different formatting in the Use_Orig column
        use_type = row["Use_Orig"]
        if "," not in use_type:
            if uses not in use_type_count:
                use_type_count[uses] = 0
            use_type_count[uses] +=1
        else:
            uses = use_type.split(",", 1)[0]
            if uses not in use_type_count:
                use_type_count[uses] = 0
            use_type_count[uses] +=1

# print(borough_count)
# print(material_count)
# print(decades)
# print(use_type_count)
# print(uses)

#Write out CSVs for each data visualization: materials, types, boroughs, decades
with open("materials_final.csv", "w") as outfile_1:
    writer = csv.writer(outfile_1)
    for key, value in material_count.items():
        writer.writerow([key, value])

with open("types_final.csv", "w") as outfile_2:
    writer = csv.writer(outfile_2)
    for key, value in use_type_count.items():
        if value > 2:
            writer.writerow([key, value])

with open("boroughs_final.csv", "w") as outfile_3:
    writer = csv.writer(outfile_3)
    for key, value in borough_count.items():
        writer.writerow([key, value])

with open("decades_final.csv", "w") as outfile_4:
    writer = csv.writer(outfile_4)
    for key, value in decades_count.items():
        writer.writerow([key, value])