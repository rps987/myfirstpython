#!/usr/bin/python3
##define URL as global
import requests
NASAURL = "https://api.nasa.gov/planetary/apod?api_key="

def main():
    """
    code to talk to NASA APOD
    """
    ## read in our nasa api key
    with open("/Users/rajes2/nasa.creds", "r") as ncreds:
        myapikey = ncreds.read()
    myapikey = myapikey.rstrip('\n')

    ## append to our url
    ##NASAURL = NASAURL + myapikey
    ## make an API request
    apod = requests.get(NASAURL + myapikey)

    ## parse out json
    apod = apod.json()

    ## print out date

    print(apod.get("date"))

    ## print out explanation
    print(apod.get("explanation"))

    ## print out URL
    print(apod.get("hdurl"))

if __name__ == '__main__':
    main()

