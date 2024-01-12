import numpy
from PIL import Image
from naoqi import ALProxy, ALBroker
import move

myBroker = ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
aln = ALProxy("ALNavigation")
tts = ALProxy("ALTextToSpeech")

def generateMap():
    radius = float(raw_input("What radius do you want me to move? "))
    aln.explore(radius)
    print("Exploration done!")
    aln.stopExploration()
    path = aln.saveExploration()

    return path

def setHome():
    print("Set a home position")
    move.main()
    return aln.getRobotPositionInMap()[0]

locations = {}
def setLocations():
    if "home" not in locations:
        locations['home'] = setHome()
    input_ = raw_input("Set a location y/n?: ")
    if input_ == 'n':
        return locations
    else:
        move.main()
        name = raw_input("What is this location called?: ")
        locations[name] = aln.getRobotPositionInMap()[0]
        aln.navigateToInMap(locations["home"])
        return setLocations()