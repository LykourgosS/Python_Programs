import json,urllib

flag="y"
while flag!="n":
    movie=raw_input("Give the title of the movie...\n").replace(" ","+")
    url = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" %(movie)
    data = urllib.urlopen(url).read()
    output = json.loads(data)
    print "\n",output["Title"],"(",output["Year"],")"
    print "Awards: "+(output["Awards"])
    print "IMDB Rating: "+(output["imdbRating"])+"\n"
    flag=raw_input("Do you want to continue ??? (y/n) ")
