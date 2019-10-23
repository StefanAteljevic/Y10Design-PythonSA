#Star Wars API
#Stefan Ateljevic
#Mr. Jugoon

import requests
import json



def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("""

    <!DOCTYPE html>
    <html>

        <head>

        <body bgcolor="black">

            <title> Star Wars API </title>

        <div class="starwars-image"></div>

        <div class="starwars-text">
            <h1>Welcome to the Star Wars API</h1>
            <p>For all of your Star Wars facts and statistics!</p>
        </div>   

        <div class="subtitle">
        <h1 style="background-color:#000000;">The information you request will be displayed below:</h1>
        </div>

        </head>

    </html>""")
    myfile.write("<head><link rel='stylesheet' type='text/css' href='style.css'></head>")
    for i in range(len(data)):
        myfile.write(f"<h1>{data[i]}</h1>")
    # for i in range(len(people)):
        # myfile.write(f"<h1>{people[i]}</h1>")
    # myfile.write("<h1>" + titles[0] + "</h1>")
    # myfile.write("<h1>JSON file returned by API call</h1>")
    # myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    # myfile.write(data)

    # myfile.write("""

    # <!DOCTYPE html>
    # <html>

    #     <head>

    #         <title> Star Wars API </title>

    #     <div class="starwars-image"></div>

    #     <div class="starwars-text">
    #         <h1>Welcome to the Star Wars API</h1>
    #         <p>For all of your Star Wars facts and statistics</p>
    #     </div>   

    #     </head>

    # </html>""")

    myfile.close()

def getMovies():
    movies = requests.get("https://swapi.co/api/films/")
    if (movies.status_code == 200):
        data = movies.content 
        data_as_str = data.decode()    
        datajson = movies.json()
        movies = []
        print(datajson)
        for movie in datajson["results"]:
            print(movie)
            title = movie["title"]
            movies.append(title)
        print(movies)    
        writeHTML(movies)



def getCharacters():
    people = requests.get("https://swapi.co/api/people/")
    if (people.status_code ==200):
        data = people.content
        data_as_str = data.decode()
        datajson = people.json() 
        people = []
        print(datajson)
        for person in datajson["results"]:
            print(person)
            name = person["name"]
            people.append(name)
        print(people)
        writeHTML(people)


def getPlanets():
    planets = requests.get("https://swapi.co/api/planets/")
    if (planets.status_code ==200):
        data = planets.content
        data_as_str = data.decode()
        datajson = planets.json()
        planets = []
        print(datajson)
        for planet in datajson["results"]:
            print(planet)
            name = planet["name"]
            planets.append(name)
        print(planets)
        writeHTML(planets)

def getSpecies():
    species = requests.get("https://swapi.co/api/species/")
    if (species.status_code ==200):
        data = species.content
        data_as_str = data.decode()
        datajson = species.json()
        species = []
        print(datajson)
        for name in datajson["results"]:
            print(name)
            name = name["name"]
            species.append(name)
        print(species)
        writeHTML(species) 

def getVehicles():
    vehicles = requests.get("https://swapi.co/api/vehicles/")
    if (vehicles.status_code ==200):
        data = vehicles.content
        data_as_str = data.decode()
        datajson = vehicles.json()
        vehicles = []
        print(datajson)
        for vehicle in datajson["results"]:
            print(vehicle)
            name = vehicle["name"]
            vehicles.append(name)
        print(vehicles)
        writeHTML(vehicles)

def getStarships():
    starships = requests.get("https://swapi.co/api/starships/")
    if(starships.status_code ==200):
        data = starships.content
        data_as_str = data.decode()
        datajson = starships.json()
        starships = []
        print(datajson)
        for starship in datajson["results"]:
            print(starship)
            name = starship["name"]
            starships.append(name)
        print(starships)
        writeHTML(starships)



def main():
    print(" ")
    print("Welcome to the Star Wars API.")
    print(" ")
    print("Once you make a selection below, head over to myapi.html to view what you've    selected.")
    print(" ")
    print("1. The Movies")
    print("2. The Characters")
    print("3. The Planets")
    print("4. The Species")
    print("5. The Vehicles")
    print("6. The Starships")
    print(" ")

    choice = int(input("Which Star Wars facts would you like to learn about? Please pick a number from 1to 6.\n"))
    # use API to get place info

    if choice == 1:
        getMovies()

    elif choice == 2:
        getCharacters()

    elif choice == 3:
        getPlanets() 

    elif choice == 4:
        getSpecies() 

    elif choice == 5:
        getVehicles()  

    elif choice == 6: 
        getStarships()

    else: 
        print ("This is not a valid choice")
        print ("Hope you have a great day anyway!")




main()