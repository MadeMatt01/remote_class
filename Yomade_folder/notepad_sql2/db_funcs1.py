import pymysql.cursors

#  Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='covid19_1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_tables(): 
    with connection.cursor() as Cursor:
        
        create_countries_table = "create table IF NOT EXISTS countries (ID int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, Name VARCHAR(100), lng float, lat float)"

        Cursor.execute(create_countries_table)
        

        create_cases_table = """CREATE table IF NOT EXISTS cases_with_deaths (ID int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, Country_ID INT(10), 
                            FOREIGN KEY (Country_ID) REFERENCES countries(ID), Cases INT(100), Death INT(200), `Date` DATE)"""

        Cursor.execute(create_cases_table)

        connection.commit()
        


def write_country(Name, lng, lat):

    with connection.cursor() as Cursor:
        
        add_country = f"INSERT INTO countries (Name, lat, lng) values('{Name}','{lat}','{lng}')"

        Cursor.execute(add_country)
        
        connection.commit()

def write_case(Country_ID, Date, Cases):

   with connection.cursor() as Cursor:
        
       add_case = f"INSERT INTO cases (Country_ID, Date, Cases) values('{Country_ID}','{Date}','{Cases}')"

       Cursor.execute(add_case)
        
       connection.commit()

def write_case_with_deaths(Country_ID, Date, Cases, Death):

    with connection.cursor() as Cursor:
        
        add_cases = f"INSERT INTO cases_with_deaths (Country_ID, Date, Cases, Death) values('{Country_ID}','{Date}','{Cases}' '{Death}')"

        Cursor.execute(add_cases)
        
        connection.commit()

def check_country(Name):
    with connection.cursor() as Cursor:
        
        get_country = f"SELECT * FROM countries where name = '{Name}'"

        Cursor.execute(get_country)
        
        return Cursor.fetchall()


def format_time(Date):
    
    "1/22/20" # before split
    month, day, year = Date.split("/") #["1","22", "20"] #after split
   
    fixed_date = "-".join([year.replace('\n','')+'20', month, day]) #20+20 ==== 2020
    "2020-1-22"
    return fixed_date

#write_country("Norway", 8.4689, 60.472)
#write_case(2, "2020-01-23", 3, 7675)
#create_tables()
