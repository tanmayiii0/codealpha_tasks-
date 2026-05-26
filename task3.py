import re

file = open("sample.txt", "r")

text = file.read()

emails = re.findall(r'\S+@\S+', text)

print(emails)
