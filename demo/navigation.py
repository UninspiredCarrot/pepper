import numpy
from PIL import Image
from naoqi import ALProxy
from naoqi import ALBroker
import time
import pprint
import move as mv
import json
#broker
myBroker = ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)

aln = ALProxy("ALNavigation")
move = ALProxy("ALMotion")
tts = ALProxy("ALTextToSpeech")


   
def navigate_to_location(item):
    with open("locations.json", "r") as file:
        content = file.read()

    locations = json.loads(content)
    if item in locations.keys():
        aln.navigateToInMap(locations[item])
        time.sleep(5)
                
        aln.navigateToInMap(locations["home"])
        return True
    
    return False

