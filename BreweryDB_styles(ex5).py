import json,urllib

flag="y"
while flag!="n":
    url = "http://api.brewerydb.com/v2/styles?key=df245f7b047257e9a006d0ff484c5b88&format=json"
    data = urllib.urlopen(url).read()
    output = json.loads(data)
    #styles=[]
    print "Styles of Beers:\n"
    for i in range(len(output["data"])):
        #styles.append(output["data"][i]["name"].encode('ascii','ignore'))
        print output["data"][i]["id"],". ",output["data"][i]["name"]
    print "\nChoose one of the beer categories above (1-",(i+1),")"
    style=int(raw_input())
    url ="http://api.brewerydb.com/v2/beers?key=df245f7b047257e9a006d0ff484c5b88&format=json&styleId="+str(style)
    #print url
    data = urllib.urlopen(url).read()
    output = json.loads(data)
    pages=int(output["numberOfPages"])
    res=0
    for i in range(pages):
        url ="http://api.brewerydb.com/v2/beers?key=df245f7b047257e9a006d0ff484c5b88&format=json&styleId="+str(style)+"&p="+str(i+1)
        data = urllib.urlopen(url).read()
        output = json.loads(data)
        for j in range(len(output["data"])):
            print output["data"][j]["name"]
            res+=1
    print "(",res,"Results)"
    flag=raw_input("Do you want to continue ??? (y/n) ")
