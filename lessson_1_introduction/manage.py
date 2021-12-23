var = "Hello world"
print(var)
if var:
    print(True)
else:
    print(False)

List = ['any', 'data', True, 6, 'type', 'can', {'find': 'here'}]
Dict = {
    'name': "Strange",
    'surname': "Stephan",
    'isMarried': False,
    'language': "javaScript"
}
print(List)

let = "something"

 # print(3 + let) # error
print(str(3) + let)

import requests
url = "https://english-tester-nu.vercel.app/"
page = requests.get(url)
print(page.text)