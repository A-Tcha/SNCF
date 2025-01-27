# SNCF - Lost objects in trains (France)

This a personal project using data from SNCF (French National railway company). The data set used is about objects which have been found in trains. The main goal of this project is to visualize objects found on a map.


The data is available in Power BI on this [link](https://app.powerbi.com/view?r=eyJrIjoiM2IzOGEyMDMtMjc2Ni00ZjIwLTliNTEtMjJkYTUwMzMzYWIyIiwidCI6IjllMDA2ZDc1LTk4YzgtNDhkMi1iNmI0LTEyMzc4Y2M3OWViMSJ9&pageName=8163f93de0fe84b9bbf1
) 

More information about the data can be found here: https://ressources.data.sncf.com/explore/dataset/objets-trouves-restitution/api/?sort=date


The script sncf_script.py fetches the data for every days within the date range selected. Once the script is finished, the output is saved as an Excel file (.xlsx). The Excel file is then used for building the dashboard in Power BI and Tableau.


Notes:
The project is still ongoing. Updates will be published regularly. 
