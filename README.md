# Speech to text - AI-Compare API
## Description
This repositery provides code to implement Eden AI Speech-to-text API. Eden AI Speech-to-text API allows to call Speech-to-text APIs from multpile speech-to-text providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is AI-Compare ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your IAM [here](https://app.edenai.run/admin/user).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://dev-api.edenai.run/v1/pretrained/audio/speech_recognition'
```
### Select parameters 
Set audio file to transcribe, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers':'[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_to_find':'Bonjour, je suis Martin','language':'en-US'}
files = [  ('files', open('Music/example.mp3','rb'))]
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
```json
{
  "result": [
    {"solution_name": "Google cloud","execution_time": "14.179207","result": {"audio_path": "media/data/files/speech_recognition_XcpGMph.wav","transcribe": "allô oui bonjour Martin à Paris","confidence": 0.8405160903930664},"api_response": {"results": [{"alternatives": [{"transcript": "allô oui bonjour à Martin à Paris","confidence": 0.8906704187393188}],"languageCode": "fr-fr"}]},"matching_text": 0.7222222222222222}]
    }
```

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](Logo complet Eden AI - format PNG.png)
