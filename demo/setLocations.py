import exploration
import json
import os

def main():
    mapPath = exploration.generateMap()
    os.rename(mapPath, "/home/nao/demo/maps/map.explo")

    locations = exploration.setLocations()

    with open("maps/locations.json", "w") as outfile:
        outfile.write(json.dumps(locations))






if __name__ == "__main__":
    main()