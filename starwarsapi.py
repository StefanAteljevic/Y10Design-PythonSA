#Star Wars API
#Stefan Ateljevic
#Mr. Jugoon's class

import requests
import json
import webbrowser
#This imports all of the required applications to run my program. 


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
    myfile.close()

#This is where we access the HTML file, open it, and alter it.
#We added design customizations, and links to allow the program to run.

def getMovies():
    movies = requests.get("https://swapi.co/api/films/")
    if (movies.status_code == 200):
        data = movies.content 
        data_as_str = data.decode()    
        datajson = movies.json()
        movies = []
        for movie in datajson["results"]:
            title = movie["title"]
            movies.append(title)   
        writeHTML(movies)



def getCharacters():
    people = requests.get("https://swapi.co/api/people/")
    if (people.status_code ==200):
        data = people.content
        data_as_str = data.decode()
        datajson = people.json() 
        people = []
        for person in datajson["results"]:
            name = person["name"]
            people.append(name)
        writeHTML(people)


def getPlanets():
    planets = requests.get("https://swapi.co/api/planets/")
    if (planets.status_code ==200):
        data = planets.content
        data_as_str = data.decode()
        datajson = planets.json()
        planets = []
        for planet in datajson["results"]:
            name = planet["name"]
            planets.append(name)
        writeHTML(planets)

def getSpecies():
    species = requests.get("https://swapi.co/api/species/")
    if (species.status_code ==200):
        data = species.content
        data_as_str = data.decode()
        datajson = species.json()
        species = []
        for name in datajson["results"]:
            name = name["name"]
            species.append(name)
        writeHTML(species) 

def getVehicles():
    vehicles = requests.get("https://swapi.co/api/vehicles/")
    if (vehicles.status_code ==200):
        data = vehicles.content
        data_as_str = data.decode()
        datajson = vehicles.json()
        vehicles = []
        for vehicle in datajson["results"]:
            name = vehicle["name"]
            vehicles.append(name)
        writeHTML(vehicles)

def getStarships():
    starships = requests.get("https://swapi.co/api/starships/")
    if(starships.status_code ==200):
        data = starships.content
        data_as_str = data.decode()
        datajson = starships.json()
        starships = []
        for starship in datajson["results"]:
            name = starship["name"]
            starships.append(name)
        writeHTML(starships)

#These 6 definitions are for the 6 sections of the API.
#We access the API, fetch the information we want, and display it.

def main():
    print(" ")
    print("Welcome to the Star Wars API.")
    print(" ")
    print("Once you make a selection below, head over to myapi.html to view what you've selected.")
    print(" ")
    print("1. The Movies")
    print("2. The Characters")
    print("3. The Planets")
    print("4. The Species")
    print("5. The Vehicles")
    print("6. The Starships")
    print(" ")

    choice = int(input("Which Star Wars facts would you like to learn about? Please pick a number from 1 to 6.\n"))
    #This is where we ask the user what they would like to learn about.

    if choice == 1:
        getMovies()
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

    elif choice == 2:
        getCharacters()
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

    elif choice == 3:
        getPlanets() 
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

    elif choice == 4:
        getSpecies() 
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

    elif choice == 5:
        getVehicles()  
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

    elif choice == 6: 
        getStarships()
        print("Fetching your selection...")
        webbrowser.open("file:///Users/stefan.ateljevic/Desktop/Github/Y10Design-PythonSA/myapi.html")

#The choices shown here use the definitons we made earlier.

    else: 
        print ("This is not a valid choice.")
        print (" ")
        print ("Hope you have a great day anyway!")

#If the input is incorrect, the program will gracefully stop.

main()