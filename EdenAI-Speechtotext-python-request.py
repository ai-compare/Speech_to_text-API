import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/audio/speech_recognition'

# Select providers, and audio to transcribe
payload = {'providers':'[\'ibm\', \'microsoft\', \'aws\', \'google_cloud\']','text_to_find':'Bonjour, je suis Martin','language':'fr-FR'}

# Select file to test         
files = {'files': open('Music/0wr69-jf4nc.wav','rb')}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
