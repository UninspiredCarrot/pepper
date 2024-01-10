import subprocess
import json
import listen
import select

openai_api_key = [x[1] for x in [x.split('=') for x in open('keys.txt').read().split()] if x[0] == 'OpenAIKey'][0]

def needHelp(question):
	if u'yes' == question.lower()[:3]:
		return True
	return False

def isWhere(question):
	with open("maps/locations.json", "r") as file:
		content = file.read()
	locations = list(json.loads(content).keys())	

	formatted_question = ''
	for word in question:
		formatted_question += word.encode('ascii', 'ignore')

	if 'where' in formatted_question.split():
		return 'alpha'
		for location in locations:
			if location in formatted_question.split():
				return location
	
	return False
	

def GPTreply(question):

	url = "https://api.openai.com/v1/chat/completions"

	json_payload = {
		"model": "gpt-3.5-turbo",
		"messages": [
			{"role": "system", "content": "You are a helpful cute shopping assistant named Pepper."},
			{"role": "user", "content": question}
		],
		"temperature": 0.3,
		"stream": True
		}
	
	with open("request_payload.json", "w") as json_file:
		json.dump(json_payload, json_file)
	
	curl_command = [
		"curl",
		url,
		"-H", "Content-Type: application/json",
		"-H", "Authorization: Bearer {}".format(openai_api_key),
		"--data-binary", "@request_payload.json"
	]

	process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
	dialogue = ""
	word_count = 0

	while process.poll() is None:
		ready_to_read, _, _ = select.select([process.stdout], [], [], 0.1)
		if ready_to_read:
			for line in process.stdout:
				if line.startswith("data: "):
					try:
						json_content = json.loads(line[6:])
						content = json_content.get("choices", [{}])[0].get("delta", {}).get("content", "").encode('ascii', 'ignore')

						if any(char.isalnum() for char in content) or word_count == 10:
							dialogue += content
							word_count += 1
						else:
							print(dialogue)
							listen.speak(dialogue)
							dialogue = ""
							word_count = 0
					except ValueError:
						print("[DONE]")

	# Read any remaining output after the process has finished
	for line in process.stdout:
		if line.startswith("data: "):
			try:
				json_content = json.loads(line[6:])
				content = json_content.get("choices", [{}])[0].get("delta", {}).get("content", "").encode('ascii', 'ignore')

				if any(char.isalnum() for char in content) or word_count == 10:
					dialogue += content
					word_count += 1
				else:
					print(dialogue)
					listen.speak(dialogue)
					dialogue = ""
					word_count = 0
			except ValueError:
				print("[DONE]")

	# Check for errors
	if process.returncode != 0:
		print("Error:", process.stderr.read())
