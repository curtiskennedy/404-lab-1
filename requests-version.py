import requests

# print requests version
print("requests library version:", requests.__version__)

# get the google homepage
# can access headers, text, etc. using response object.
res = requests.get("http://www.google.com/")

# print res object
print("Google Homepage:", res)

# get the source code of this script from github
raw = "https://raw.githubusercontent.com/curtiskennedy/404-lab-1/main/requests-version.py"
res = requests.get(raw)

# print the source code
print("\nSCRIPT SOURCE CODE:\n", res.text)
