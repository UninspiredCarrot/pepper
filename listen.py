import naoqi
import subprocess
import json
import time
import os

myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
AD = naoqi.ALProxy("ALAudioDevice")
ATTS = naoqi.ALProxy("ALAnimatedSpeech")
VR = naoqi.ALProxy("ALVideoRecorder")
ALM = naoqi.ALProxy("ALMotion")
openai_api_key = [x[1] for x in [x.split('=') for x in open('keys.txt').read().split()] if x[0] == 'OpenAIKey'][0]

def record_audio(output_file, duration=None):
	try:
		AD.startMicrophonesRecording(output_file)
	except RuntimeError:
		AD.stopMicrophonesRecording()
		AD.startMicrophonesRecording(output_file)
	if duration == None:
		while True:
			instruction = raw_input("When finished talking, enter 'q': ")
			if instruction.lower() == "q":
				break
		AD.stopMicrophonesRecording()
		return 'finished recording'
	time.sleep(duration)
	AD.stopMicrophonesRecording()

def record_video(path, output_file):
	ALM.setAngles("HeadYaw", 0, 0.7)
	ALM.setAngles("HeadPitch", 0, 0.7)
	VR.setCameraID(1)
	VR.startRecording(path, output_file)
	while True:
		instruction = raw_input("When finished recording, enter 'q': ")
		if instruction.lower() == "q":
			break
	VR.stopRecording()

def hear(output_file):
	url = "https://api.openai.com/v1/audio/transcriptions"
	file_path = output_file
	model = "whisper-1"
	language = "en"

	curl_command = [
	    "curl",
	    url,
	    "-H", "Authorization: Bearer {}".format(openai_api_key),
	    "-H", "Content-Type: multipart/form-data",
	    "-F", "file=@{}".format(file_path),
	    "-F", "model={}".format(model),
	    "-F", "language={}".format(language)
	]


	response = subprocess.check_output(curl_command, stderr=subprocess.STDOUT)
	lines = response.splitlines()
	formatted_output = ''
	start_reading = False
	for i, line in enumerate(lines):
		if line == '{':
			start_reading = True
		if start_reading:
			formatted_output += line
		if line == '}':
			break

	json_response = json.loads(formatted_output)
	text_value = json_response.get("text", "")

	print(response)
	return text_value

def speak(answer):
	ATTS.say(answer)

def has_text(input_text):
    return any(char.isalnum() for char in input_text)

def listenToText():
	record_audio("recordings/temp.wav", 4)
	reply = hear("recordings/temp.wav")
	print(reply)
	return reply
