from os import system
from Googlesearch import search

# to search 
query = input(">>")

for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 