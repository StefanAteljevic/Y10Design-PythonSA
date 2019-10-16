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

def writeHTML(titles, people):
    myfile = open("myapi.html","w")
    myfile.write("<h1> Star Wars Data, Facts, and Statistics</h1>")
    for i in range(len(titles)):
        myfile.write(f"<h1>{titles[i]}</h1>")
    for i in range(len(people)):
        myfile.write(f"<h1>{people[i]}</h1>")
    # myfile.write("<h1>" + titles[0] + "</h1>")
    # myfile.write("<h1>JSON file returned by API call</h1>")
    # myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    # myfile.write(data)
    myfile.close()

def main():
    # use API to get place info
    movies = requests.get("https://swapi.co/api/films/")
    people = requests.get("https://swapi.co/api/people/")


    # if API call is correct
    if (movies.status_code == 200):
        data = movies.content # response comes in as byte data type
        data_as_str = data.decode()    # decode to str
          # call function to write string data to HTML file
        datajson = movies.json()
        # print(data)

        res = datajson["results"]
        peopleres = people.json()["results"]

        people = []
        for person in peopleres:
            name = person["name"]
            people.append(name)
            # print(person)


        titles = []
        for movie in res:
            title = movie['title']
            titles.append(title)
            # print(movie)


        writeHTML(titles, people)

        # load as a JSON to access specific data more easily
        # datajson = response.json()
        # cities = datajson['nearbyCities']
        # for city in cities:
            # print(city)
        
    else:
        data = "Error has occured"
        writeHTML(data)

main()