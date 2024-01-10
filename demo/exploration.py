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