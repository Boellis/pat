import http.client, uuid, json
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

subscriptionKey = 'ac021a114b2c4dd7bc255ff25b4850ed'

host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

# Translate to Spanish and Italian
params = "&to=es&to=it&to=fr&to=ja&to=pt&to=hi&to=zh-Hans&to=ko&to=en"
langDict  = {"spanish":"0",
             "italian":"1",
             "french":"2",
             "japanese":"3",
             "portuguese":"4",
             "hindi":"5",
             "chinese":"6",
             "korean":"7",
             "english":"8"
             }
def translate(content):
    headers = {
        'Ocp-Apim-Subscription-Key' : subscriptionKey,
        'Content-type' : 'application/json',
        'X-ClientTraceId' : str(uuid.uuid4())
    }

    conn = http.client.HTTPSConnection(host)
    conn.request("POST", path + params, content, headers)
    response = conn.getresponse()
    return response.read().decode('utf-8')



def outputTranslation(text,lang):
    # Text that we're sending to Azure Translation API
    requestBody = [{'Text' : text,}]

    # Takes the JSON object and returns an encoded string
    content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
    # Translates the encoded string
    result = translate(content)

    ''' Note: We convert result, which is JSON,
    to and from an object so we can pretty-print itself.
    We want to avoid escaping any Unicode characters that result contains.'''

    # Returns an object from the translated string
    output = json.loads(result)

    translatedText = ""
    #----------------------------#

    # Check if the language passed in by the parameter is in the dictionary of languages you provided
    if lang in langDict:
        # Create a variable that stores the value from the key passed
        #in for a language in the dictionary
        langVal = int(langDict["{0}".format(lang)])
        # Our Json object(output) returns text and translations for each of the parameters
        # We only need to return the translation for the language we selected
        translatedText = output[0]['translations'][langVal]['text']
    else:
        print("Did not enter correct language, defaulting to Spanish")
        translatedText = output[0]['translations'][0]['text']

    return translatedText
