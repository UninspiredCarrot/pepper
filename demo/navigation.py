from naoqi import ALProxy
from naoqi import ALBroker
import json
#broker
myBroker = ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)

aln = ALProxy("ALNavigation")
move = ALProxy("ALMotion")
tts = ALProxy("ALTextToSpeech")


   
def navigate_to_location(path, item):
    aln.stopLocalization()	 
    aln.loadExploration(path)
    map_array = aln.getMetricalMap()
    mpp = map_array[0]
    aln.startLocalization()
    with open("maps/locations.json", "r") as file:
        content = file.read()

    locations = json.loads(content)
    if item in locations.keys():
        aln.navigateToInMap(locations[item])        
        aln.navigateToInMap(locations["home"])
        return True
    
    return False

