from googlesearch import search

query = input("Ask Anything : ")

for url in search(query):
    print(url)