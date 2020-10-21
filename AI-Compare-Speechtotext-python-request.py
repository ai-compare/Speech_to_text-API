import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/Speech%20Recognition

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/audio/speech_recognition'

# Select providers, and audio to transcribe
payload = {'providers':'[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_to_find':'Bonjour, je suis Martin','language':'fr-FR'}

# Select file to test         
files = {'files': open('Music/0wr69-jf4nc.wav','rb')}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
