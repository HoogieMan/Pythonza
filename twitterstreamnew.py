import oauth2 as oauth
import urllib2 as urllib
import json

## Twitter API credentials, from my dev account
access_token_key = "2391549210-O2GrmpV0E10coYHQT3NdkumMrRHnI5HWXl7Ssye"
access_token_secret = "YJZPTnqbzQG9C66emPIgs37WzzOlw8wsaH4uNik3V7zqY"

consumer_key = "W4LOJKsaNZw6xWETL5jbQ"
consumer_secret = "2eKrsyZWprJbg3BkVlUmwQYUTubNEPPZERif0nU2oc"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)


## Constructs, signs, and opens a twitter request using credentials above

def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

## Fetches tweets/data. q='insert search term here'
def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=IBM"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()
    return response

if __name__ == '__main__':
  fetchsamples()
  
## pipe data to text file for analysis
