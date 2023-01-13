import requests

# print requests version
print("requests library version:", requests.__version__)

# get the google homepage
# can access headers, text, etc. using response object.
res = requests.get("http://www.google.com/")

# print res object
print("Google Homepage:", res)
