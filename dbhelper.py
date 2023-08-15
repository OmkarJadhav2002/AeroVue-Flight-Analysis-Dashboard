# database related code
import mysql.connector

class DB:
    # connect to the database
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database= "flight_dash"
            )
            # creating a cursor object
            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except:
            print("Connection Error")

    # fetching all the city names(unique) from the database
    def fetch_cities(self):
        city = []
        self.mycursor.execute("""
            select distinct(Source) from flights
            union
            select distinct(Destination) from flights
        """)

        # get the results (fetch all the data)
        data = self.mycursor.fetchall()
        # print(data)
        for item in data:
            city.append(item[0])

        return city

    # to get the each flight
    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
            select Airline, Route, Dep_time, Duration, Price from flights
            where Source = '{}' and Destination = '{}' """.format(source, destination))

        data = self.mycursor.fetchall()
        return data

    # to get the count of each flights
    def fetch_airline_count(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
            select Airline, count(*) as "No_of_Flights" from flights
            group by Airline""")

        data = self.mycursor.fetchall()
        # return data
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    # to get the busiest airport
    def fetch_busy_airport_cities(self):

        city = []
        frequency = []

        self.mycursor.execute("""
                    select Source, count(*) as "No_of_flights" from (select Source from flights
								                        UNION all
                                                        select Destination from flights ) t
                                                        group by t.source
                                                        order by No_of_flights desc """)

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def fetch_daily_flights(self):
        date = []
        frequency = []

        self.mycursor.execute("""select Date_of_Journey, count(*) as "no_of_flights" from flights
                            group by Date_of_Journey
                            """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

    def fetch_price(self):
        price = []
        self.mycursor.execute("""
                    select Price as "Price" from flights
                """)
        # get the results (fetch all the data)
        data = self.mycursor.fetchall()
        # print(data)
        for item in data:
            price.append(item)

        return price


