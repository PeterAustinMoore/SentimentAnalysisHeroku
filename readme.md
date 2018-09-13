## Sentiment Analysis Endpoint on Heroku

### Initialization
- Assumption: existing Heroku account and CLI toolkit installed
- Download this repository as a zip file and unzip
- Create the app on heroku and follow the instructions for initializing a folder as repository
- Do usual `git add . && git commit -m "init" && git push heroku master`

### Using the endpoint
The endpoint exists at the {Your heroku app domain}/sentiment and can be accessed via a GET request with the "data" query param, for example:

https://mySentimentApp.herokuapp.com/sentiment?data=I%20love%20cake
returns: {"sentiment":"positive", "value":0.6369}

**Note: Because this is a request through the URL, length limits are enforced. So you will want to limit it to 500 characters or so**

### About the Application
The application uses the NLTK VADER `polarity_scores` function.


### Example python code
```python
import requests
session = requests.Session()

endpoint = "https://mySentimentApp.herokuapp.com/sentiment?data={sentence}"

sentences = ["This is good", "This is bad", "This is cake!"]

for sentence in sentences:
  url = endpoint.format(sentence=sentence)
  resp = session.get(url)
  print(resp.json())

# {"sentiment":"positive", "value":0.6033}
# {"sentiment":"slight negative", "value":0.344}
# {"sentiment":"neutral", "value":0}
```
