import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#a753e757-f7b7-4e64-9d11-571f96e6ab87

#Enter your API Token
headers = {'x-access-token': 'Enter your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/api/v1/audio/create/compare/speech_recognition'

# Select providers, and audio to transcribe
payload = {'providers':'[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_to_find':'Bonjour, je suis Martin','language':'fr-FR'}

# Select file to test         
files = {'files': open('Music/0wr69-jf4nc.wav','rb')}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
