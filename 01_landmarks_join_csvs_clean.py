### This script joins and cleans two datasets from the NYC Landmarks Preservation Commission:
### https://data.cityofnewyork.us/Housing-Development/Individual-Landmark-Sites/ts56-fkf5
### https://data.cityofnewyork.us/Housing-Development/LPC-Individual-Landmark-and-Historic-District-Buil/7mgd-s57w


import pandas as pd
import csv
import sys

#To get around system error message
csv.field_size_limit(sys.maxsize)

#Open the historic building file and filter for just the buildings identified as Individual Landmarks
df = pd.read_csv("LPC_Historic_Building_Database.csv")
df = df.loc[df["Hist_Dist"] == "Individual Landmarks"]

#Delete as many duplicate as possible (duplicate rows often have extremely small differences so aren't identical) and create a new CSV
df = df.reset_index().drop_duplicates(subset=["Des_Addres","Date_High","Mat_Prim","Mat_Sec","Use_Orig"],keep="first").set_index("index")
df.to_csv("LPC_Historic_Building_Database_subset.csv")

file1 = pd.read_csv("LPC_Individual_Landmarks.csv")
file2 = pd.read_csv("LPC_Historic_Building_Database_subset.csv")

#Join the new historic building file to the individual landmark file, using multiple fields since there is no one common column between the two files
landmarks_join = file1.merge(file2, how="left", on=["BBL","Borough","Block","Lot"])
landmarks_join.to_csv("landmarks_joined_files.csv", sep = ",", index=False)

#Joining on mulitple fields means lots of duplicate records that need to be deleted
lookup = {}
biggest_value = {}

with open("landmarks_joined_files.csv", "r") as joined_csv:
    reader = csv.reader(joined_csv)
    for row in reader:

        #Convert each row to a string
        all_rows = "".join(row)
        # print(all_rows)

        #The Shape_Leng column is the only one with a unique value for each item, so use that for the lookup
        join_value = row[16]

        #Compare all rows with the same join_value to one another
        if join_value in lookup:

            #If true, the current row is bigger than the saved row
            if lookup[join_value] > len(all_rows):

                #Replace the stored version
                lookup[join_value] = len(all_rows)
                biggest_value[join_value] = row

        #If not true, the address hasn't been found yet
        #Saving both the length and the row data
        else:
            lookup[join_value] = len(all_rows)
            biggest_value[join_value] = row

#Write out to a new CSV
with open("landmarks_cleaned_file.csv", "w") as values:
    writer = csv.writer(values)
    for join_value in biggest_value:
        writer.writerow(biggest_value[join_value])

#Open up the new CSV for additional cleaning
landmarks = pd.read_csv("landmarks_cleaned_file.csv")

#Delete unwanted/unnecessary columns
landmarks.drop(["OBJECTID_1","the_geom_x","Shape_Leng","Shape_Area","OBJECTID_y","the_geom_y"],axis=1,inplace=True)

#Delete unwanted rows (two rows of garbled data in the initial dataset)
landmarks.drop([1256,1257],axis=0)

#Replace cells in the Borough column that are blank with "Multiple" (for sites that span multiple boroughs, e.g., bridges)
landmarks["Borough"].fillna("Multiple",inplace=True)

#Save out a final dataset for parsing
landmarks.to_csv('landmarks_dataset_final.csv',index=False)