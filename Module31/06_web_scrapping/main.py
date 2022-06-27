import requests
from lxml import html


site = requests.get('http://www.columbia.edu/~fdc/sample.html')

code = html.fromstring(site.text)

h3_list = code.xpath('//h3')
for i in h3_list:
    print(i.text)
