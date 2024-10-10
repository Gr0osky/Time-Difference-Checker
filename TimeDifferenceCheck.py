# CENTRAL TIME ZONES
China = [8, 0]
India = [5, 20]
United_States = [-6, -20]
Indonesia = [7, 0] 
Pakistan = [5, 0]
Brazil = [-3, 0]
Nigeria = [1, 0]
Bangladesh = [6, 0]
Russia = [3, 0]
Mexico = [-6, 0]
Japan = [9, 0]
Ethiopia = [3,0]
Philippines = [8,0]
Egypt = [2,0]
Vietnam = [7,0]
DR_Congo = [1,0]
Turkey = [3,0]
Iran = [3, 30]
Germany = [1, 0]
Thailand = [7,0]
United_Kingdom = [0,0]
France = [1,0]
Italy = [1,0]
South_Africa = [2,0]
Tanzania = [3,0]
Myanmar = [6, 30]
South_Korea = [9,0]
Colombia = [5,0]
Kenya = [3,0]
Spain = [1,0]



# FUNCTIONS

def checkTimeZone(a, b, c, d):
    Country1Hour = a[0]
    Country1Minute = a[1]
    Country2Hour = b[0]
    Country2Minute = b[1]
    TimeDifferenceHours = Country1Hour - Country2Hour
    TimeDifferenceMinutes = Country1Minute -  Country2Minute
    if TimeDifferenceMinutes < 0:
        TimeDifferenceMinutes = -(TimeDifferenceMinutes)
    if TimeDifferenceHours < 0:
        TimeDifferenceHours = -(TimeDifferenceHours)
    print(f"Time difference between {c} and {d} is {TimeDifferenceHours} hours and {TimeDifferenceMinutes} minutes.")


# Welcoming User

for i in range (0, 100):

    print("Welcome to Time Zone Guesser Program by Gr0osky!")
    Country = input("Country 1: ")
    Country2 = input("Country 2: ")


    # VALUES OF "a"
    if Country.lower() == "china":
        a = China
    elif Country.lower() == "india":
        a = India
    elif Country.lower() == "united states" or Country.lower() == "usa":
        a = United_States
    elif Country.lower() == "indonesia":
        a = Indonesia
    elif Country.lower() == "pakistan":
        a = Pakistan
    elif Country.lower() == "brazil":
        a = Brazil
    elif Country.lower() == "nigeria":
        a = Nigeria
    elif Country.lower() == "bangladesh":
        a = Bangladesh
    elif Country.lower() == "russia":
        a = Russia
    elif Country.lower() == "mexico":
        a = Mexico
    elif Country.lower() == "japan":
        a = Japan
    elif Country.lower() == "ethiopia":
        a = Ethiopia
    elif Country.lower() == "philippines":
        a = Philippines
    elif Country.lower() == "egypt":
        a = Egypt
    elif Country.lower() == "vietnam":
        a = Vietnam
    elif Country.lower() == "democratic republic of congo":
        a = DR_Congo
    elif Country.lower() == "turkey":
        a = Turkey
    elif Country.lower() == "iran":
        a = Iran
    elif Country.lower() == "germany":
        a = Germany
    elif Country.lower() == "thailand":
        a = Thailand
    elif Country.lower() == "united_kingdom":
        a = United_Kingdom
    elif Country.lower() == "france":
        a = France
    elif Country.lower() == "italy":
        a = Italy
    elif Country.lower() == "south africa":
        a = South_Africa
    elif Country.lower() == "tanzania":
        a = Tanzania
    elif Country.lower() == "myanmar":
        a = Myanmar
    elif Country.lower() == "south korea":
        a = South_Korea
    elif Country.lower() == "colombia":
        a = Colombia
    elif Country.lower() == "kenya":
        a = Kenya
    elif Country.lower() == "spain":
        a = Spain
    else:
        a = None

    # VALUES OF "b"
    if Country2.lower() == "china": 
        b = China
    elif Country2.lower() == "india":   
        b = India
    elif Country2.lower() == "united_states":   
        b = United_States
    elif Country2.lower() == "indonesia":   
        b = Indonesia
    elif Country2.lower() == "pakistan":    
        b = Pakistan
    elif Country2.lower() == "brazil":  
        b = Brazil
    elif Country2.lower() == "nigeria": 
        b = Nigeria
    elif Country2.lower() == "bangladesh":
        b = Bangladesh
    elif Country2.lower() == "russia":
        b = Russia
    elif Country2.lower() == "mexico":
        b = Mexico
    elif Country2.lower() == "japan":
        b = Japan
    elif Country2.lower() == "ethiopia":
        b = Ethiopia
    elif Country2.lower() == "philippines":
        b = Philippines
    elif Country2.lower() == "egypt":
        b = Egypt
    elif Country2.lower() == "vietnam":
        b = Vietnam
    elif Country2.lower() == "dr_congo":
        b = DR_Congo
    elif Country2.lower() == "turkey":
        b = Turkey
    elif Country2.lower() == "iran":
        b = Iran
    elif Country2.lower() == "germany":
        b = Germany
    elif Country2.lower() == "thailand":
        b = Thailand
    elif Country2.lower() == "united_kingdom":
        b = United_Kingdom
    elif Country2.lower() == "france":
        b = France
    elif Country2.lower() == "italy":
        b = Italy
    elif Country2.lower() == "south_africa":
        b = South_Africa
    elif Country2.lower() == "tanzania":
        b = Tanzania
    elif Country2.lower() == "myanmar":
        b = Myanmar
    elif Country2.lower() == "south_korea":
        b = South_Korea
    elif Country2.lower() == "colombia":
        b = Colombia
    elif Country2.lower() == "kenya":
        b = Kenya
    elif Country2.lower() == "spain":
        b = Spain
    else:
        b = None
    if(a == None or b == None):
        print("No such countries in the database.")
        continue
    checkTimeZone(a, b, Country, Country2)



