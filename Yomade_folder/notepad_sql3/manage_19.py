from db_funcs_19 import *

cases_file = open("C:/Users/Yomade/Desktop/univelcity/Yomade_Folder/notepad_sql2/time_series_covid19.csv")
deaths_file = open("C:/Users/Yomade/Desktop/univelcity/Yomade_Folder/notepad_sql2/time_series_covid19_deaths_global.csv")
recovered_file = open("C:/Users/Yomade/Desktop/univelcity/Yomade_Folder/notepad_sql2/time_series_covid19_recovered_global.csv")

countries_of_choice = ["Italy", "Japan", "Jordan", "Nigeria", "Norway"]
heading = cases_file.readlines(1)
heading_deaths = deaths_file.readlines(1)
heading_recovered = recovered_file.readlines(3) 
#print(file.readlines(1))


for case_line, death_line, recovered_line in zip(cases_file.readlines(), deaths_file.readlines(), recovered_file.readlines()):
    #print("-"*20) 
    #print(line[0])
    #print(line[1])
    #print(line[2])
    #print("\n")

    case_line = case_line.split(",")
    death_line = death_line.split(",")
    recovered_line = recovered_line.split(",")
    

    country_name = case_line[1]

    if country_name in countries_of_choice:
        country_exists = check_country(country_name)
        #print(country_exists)

        if country_exists:

            for data in list(zip(case_line, heading[0].split(","), death_line, recovered_line))[5:]:
                #print(data)
                #print(format(data[1]), data[1])
                country_id = country_exists[0]['ID']
                date = format_time(data[1])
                cases = data[0]
                deaths = data[2]
                recovered = data[3]
                write_case_with_recoveries(country_id, date, cases, deaths, recovered)

        else:
            write_country(country_name, case_line[2], case_line[3])

           
        






"""
    Italy
    Japan
    Jordan
    Nigeria
    Norway
"""  