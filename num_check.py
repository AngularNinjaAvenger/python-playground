#! python3

import re

numSearch = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
x = numSearch.findall("hello this is my number mhen 555-668-999")
print(x)
