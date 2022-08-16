#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

page = requests.get("https://247ctf.com/scoreboard")

soup = BeautifulSoup(page.content, "html.parser")

# Print all the text in the content, without HTML-tags
print(soup.text)

# Print the title, with or without HTML-tags
print(soup.title.name)
print(soup.title.string)

# Find the first fitting element in the content, in this case the first link.
print(soup.find("a"))

# Find all fitting elements in the content, in this case the first link; print
# out either the full link or only the reference it's sending you to.
for line in soup.find_all("a"):
    print(line)
    print(line.get("href"))

# Find an element having a specific ID, belonging to a specific class or an
# element of a specific type belonging to a specific class; because 'class' is
# a protected word in Python it has to be suffixed with an underscore
print(soup.find(id="fetch-error"))
print(soup.find(class_="nav-link"))
print(soup.find("a", class_="nav-link"))

table = soup.find("table")
#print(table)
table_body = table.find("tbody")
rows = table_body.find_all("tr")
for row in rows:
    print("---")
    #print(row)
    cols = [x.text.strip() for x in row.find_all("td")]
    #print(cols)
    print(f"{cols[2]} is in place {cols[0]} with {cols[4]}")
