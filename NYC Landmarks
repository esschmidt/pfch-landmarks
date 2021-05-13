This project was created for Professor Matt Miller’s Programming for Cultural Heritage course at the Pratt Institute, School of Information in Spring 2021.

The two initial datasets are from the Landmarks Preservation Commission, via NYC Open Data:
<br>https://data.cityofnewyork.us/Housing-Development/Individual-Landmark-Sites/ts56-fkf5
<br>https://data.cityofnewyork.us/Housing-Development/LPC-Individual-Landmark-and-Historic-District-Buil/7mgd-s57w

(The files used for this project were last updated on April 14, 2021.)

This project aimed to analyze the characteristics of landmarked buildings in New York City, which are those considered to have “a special character or special historical or aesthetic interest or value.” The Landmarks Preservation Commission (LPC), the mayoral agency responsible for the city’s historic preservation program, makes a variety of information available via the NYC Open Data portal. I was interested in creating a holistic picture of what types of buildings have been deemed worthy of preservation and to communicate some common characteristics of landmarked buildings.

This project had two steps: First, downloading (as .csv), joining, and cleaning the two relevant LPC datasets to create a one primary dataset. The hope was to have a robust dataset on landmarked buildings that combines information currently split across two sources into one file. While the initial datasets are readily available, several problems arose in joining the files: the lack of no unique identifier used in both datasets, many missing/empty fields, older data (e.g., building identifiers) that have not been updated uniformly, and data entry errors. This Python script uses the csv and Pandas modules to join and clean the files, but due to these issues the resulting dataset—while largely complete—does contain errors including incorrectly joined rows. <b>For this reason, this file should not be considered authoritative.</b>

Second, I wrote a Python script to loop through the primary .csv file and group certain building characteristics. I focused on four columns that had mostly complete and consistently structured data: the location (borough) of each landmarked building, the primary building material, the original building type (e.g., residential, civic), and the decade built. I used the resulting .csv files to create visualizations in Tableau Public.

There are many future possibilities for this project (after reconciling remaining dataset errors)—creating more granular visualizations, comparing landmarks data to citywide building data to find out what is over- and underrepresented, building a website or other public resource to easily explore landmarked buildings, using natural language processing on the linked Designation Reports for each building… For now, know that a “historic” building most likely has at least one of these characteristics: a brick residential building in Manhattan built around the turn of the twentieth century.

The visualizations are available at: 
https://public.tableau.com/views/NYCLandmarks/Material
