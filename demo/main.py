import faceDetection
import gestures
import listen
import textProcess
import navigation

path = "/home/nao/demo/maps/map.explo"

def main():
    headShiftCount = 0
    while True:
        if faceDetection.recognise():
            gestures.wave("Hi, can I help you?")
            question = listen.listenToText()
            # question = raw_input('listening: ')
            navigation.navigate_to_location(path, 'alpha')
            if textProcess.needHelp(question):
                question = listen.listenToText()
                # question = raw_input('listening1: ')
                item = textProcess.isWhere(question)
                navigation.navigate_to_location(path, 'alpha')
                if item:
                    print(item)
                    navigation.navigate_to_location(path, item)
                else:
                    print('no item')
                    textProcess.GPTreply(question)




        else:
            gestures.scan(headShiftCount)
            headShiftCount += 1

        





if __name__ == "__main__":
    main()