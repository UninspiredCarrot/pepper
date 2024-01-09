import numpy
from PIL import Image
from naoqi import ALProxy
from naoqi import ALBroker
import time
import os
import json

import pprint
import move as mv

#broker
myBroker = ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
aln = ALProxy("ALNavigation")
tts = ALProxy("ALTextToSpeech")

locations = {}

def main():
    radius = int(raw_input("What radius do you want me to move? "))
    aln.explore(radius)
    print("Exploration done!")
    aln.stopExploration()
    path = aln.saveExploration()
    aln.stopLocalization()	 
    aln.loadExploration(path)
    map_array = aln.getMetricalMap()
    mpp = map_array[0]
    aln.startLocalization()
    locations["home"] = aln.getRobotPositionInMap()[0]

    os.rename(path, "/home/nao/map.explo")

    move()
    create_json(locations)

def move():
    mo = True
    while mo:
        mv.main()
        inp = raw_input("name or q: ")
        if inp.lower() == "n":
            inp = raw_input("Give a name for this location: ")
            locations[inp] = aln.getRobotPositionInMap()[0]
            print("locations: ", locations.items())
        if inp.lower() == "q":
            mo = False 

    aln.navigateToInMap(locations["home"])

def create_json(dictionary):
    json_object = json.dumps(dictionary)

    with open("locations.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    main()
#aln.stopLocalization()
#aln.loadExploration(path)
#map_array = aln.getMetricalMap()
#mpp = map_array[0]
#aln.startLocalization()

