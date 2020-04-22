from tempfile import TemporaryFile
import xlwt

book = xlwt.Workbook()
general = book.add_sheet("Combined Data")

general.write(0, 0, "NAME OF COUNTRY")
general.write(0, 1, "LATITUDE")
general.write(0, 2, "LONGITUDE")
general.write(0, 3, "CASES")
general.write(0, 4, "DEATHS")
general.write(0, 5, "RECOVERIES")
general.write(0, 6, "DATE")

def format_time(date):
    
    "1/22/20" 
    month, day, year = date.split("/") 
   
    fixed_date = "-".join([year.replace('\n','')+'20', month, day]) 
    "2020-1-22"
    return fixed_date


file1 = open("C:/Users/BABATOLA/Documents/DATASCIENCE/Classes at Univelcity/Second Half/Database/Dami's Database/My_covid_data/time_series_covid19_confirmed_global.csv")



country_name_list = []
for lines1 in file1.readlines():
    country_name = lines1.split(",")[1]
    country_name_list.append(country_name)
    
for _ in country_name_list:
    file1 = open("C:/Users/BABATOLA/Documents/DATASCIENCE/Classes at Univelcity/Second Half/Database/Dami's Database/My_covid_data/time_series_covid19_confirmed_global.csv")
    file2 = open("C:/Users/BABATOLA/Documents/DATASCIENCE/Classes at Univelcity/Second Half/Database/Dami's Database/My_covid_data/time_series_covid19_deaths_global.csv")
    file3 = open("C:/Users/BABATOLA/Documents/DATASCIENCE/Classes at Univelcity/Second Half/Database/Dami's Database/My_covid_data/time_series_covid19_recovered_global.csv")


    heading1 = file1.readlines(1)
    heading2 = file2.readlines(1)
    heading3 = file3.readlines(1)

    for lines1 in file1.readlines():
        cases_data = lines1.split(",")
        if cases_data[1] == _:
            number_of_cases = cases_data[4:]
            break

    
    for lines2 in file2.readlines():
        deaths_data = lines2.split(",")
        if deaths_data[1] == _:
            number_of_deaths = deaths_data[4:]
            break

    for lines3 in file3.readlines():
        recoveries_data = lines3.split(",")
        if recoveries_data[1] == _:
            number_of_recoveries =  recoveries_data[4:]
            break

    country_latitude = cases_data[2]
    country_longitude = cases_data[3]


    i = 0
    for data in list(zip(number_of_cases, number_of_deaths, number_of_recoveries, heading1[0].split(",")[4:])):
        general.write(i + 1, 0, _)
        general.write(i + 1, 1, country_latitude)
        general.write(i + 1, 2, country_longitude)
        general.write(i + 1, 3, data[0] + "\n")
        general.write(i + 1, 4, data[1] + "\n")
        general.write(i + 1, 5, data[2] + "\n") 
        general.write(i + 1, 6, format_time(data[3]) + "\n")
        i += len(heading1[0].split(",")[4:])


name = "Combined_data.xls"
book.save(name)
book.save(TemporaryFile())


