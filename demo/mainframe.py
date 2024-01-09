import facedec
import listen
import time
import exploration
import navigation

def conversation():
	while True:
		instruction = raw_input("When ready to talk, please enter 's', to stop enter 'q': ")
		if instruction.lower() == "q":
			break
		if instruction.lower() == "s":
			path = "/home/nao/chat_recordings/"
			output_file_audio = "/home/nao/chat_recordings/chat.wav"
			listen.record_audio(output_file_audio)
			question = listen.hear(output_file_audio)
			print("heard ya!")

			firstThree = question.lower().split()[:3]
			lastWord = question.lower().split()[3]

			if firstThree == [u'where', u'is', u'the']:
				lastWord = lastWord.encode('ascii', 'ignore')
				lastWord = lastWord[:-1]
				return lastWord

			if question == ['bye']:
				return False
			listen.reply(question)



def main():
	n = 0
	exploration.main()
	while True:
		inp = raw_input("when ready let me know with a 'r': ")
		if inp == 'r':
			break
	while True:

		if facedec.recognise():
			facedec.wave()
			if listen.initiate():
				res = conversation()
				print(res)
				if res == False:
					print("shift")
				else:
					navigation.navigate_to_location(res)
			else:
				print("shift")

		else:
			# keep trying for 5 seconds
			# then shift
			if n >= 5:
				print("shift")
				n = 0

			else:
				time.sleep(1)
				n+=1


if __name__ == '__main__':
	main()