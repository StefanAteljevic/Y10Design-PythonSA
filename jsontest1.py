'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json

# Find APIs at - https://apilist.fun/
# some will require an API key, boo hiss!

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

#Which information would you like?
#Movies, characters, planets.
#User will select the one that they want. 

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<head><link rel='stylesheet' type='text/css' href='style.css'></head>")
    myfile.write("<h1> Star Wars Data, Facts, and Statistics</h1>")
    for i in range(len(data)):
        myfile.write(f"<h1>{data[i]}</h1>")
    # for i in range(len(people)):
        # myfile.write(f"<h1>{people[i]}</h1>")
    # myfile.write("<h1>" + titles[0] + "</h1>")
    # myfile.write("<h1>JSON file returned by API call</h1>")
    # myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    # myfile.write(data)
    myfile.close()

def getMovies():
    #do all the stuff
    movies = requests.get("https://swapi.co/api/films/")
    if (movies.status_code == 200):
        data = movies.content # response comes in as byte data type
        data_as_str = data.decode()    # decode to str
          # call function to write string data to HTML file
        datajson = movies.json()
        # print(data)
        titles = []
        for movie in res:
            title = movie['title']
            titles.append(title)
            # print(movie)
        writeHTML(titles)



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
            # print(person)
        print(people)
        writeHTML(people)


def main():
    print("Welcome to the Star Wars API.")
    print(" ")
    print("1. The Movies")
    print("2. The Characters")
    print("3. The planets")
    print(" ")

    choice = int(input(" Which Star Wars facts would you like to learn about? Please pick a number from 1 to 3.\n"))
    # use API to get place info

    if choice == 1:
        getMovies()

    elif choice == 2: 
        getCharacters()

    else: 
        print ("This is not a valid choice")
        print ("Hope you have a great day anyway!")



    # # if API call is correct
    # if (movies.status_code == 200):
    #     data = movies.content # response comes in as byte data type
    #     data_as_str = data.decode()    # decode to str
    #       # call function to write string data to HTML file
    #     datajson = movies.json()
    #     # print(data)

    #     res = datajson["results"]
    #     peopleres = people.json()["results"]

    #     people = []
    #     for person in peopleres:
    #         name = person["name"]
    #         people.append(name)
    #         # print(person)


    #     titles = []
    #     for movie in res:
    #         title = movie['title']
    #         titles.append(title)
    #         # print(movie)


    #     writeHTML(titles, people)

        
    # else:
    #     data = "Error has occured"
    #     writeHTML(data)

main()