#!/usr/bin/python3
import json

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "jkldjlaj kjdlakj", "species": "Lk;ldkal;k;l"}, {"name": "Arthur Dent", "species": "Human"}] 

    for character in hitchhikers:
        print(character.get("name"))
    hitchhikers.append({"name": None, "species": "Human"})

    print(hitchhikers)
    with open("glaxyguide.json", "w") as jfile:
        json.dump(hitchhikers, jfile)

    jasonstring=json.dumps(hitchhikers)
    print(jasonstring)

    with open("datacenter.json", "r") as dfile:
        datacenterstr = dfile.read()
        print(type(datacenterstr))
    datacenterdecoded = json.loads(datacenterstr)
    print(type(datacenterdecoded))

if __name__ == "__main__":
    main()
