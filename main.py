import wikipediaapi
import requests
import os

wiki_wiki = wikipediaapi.Wikipedia('en')
API_KEY = os.getenv('APIKEY')
SE_ID = os.getenv('SEID')

print('What do you want to learn about:')
x = input()
page_py = wiki_wiki.page(x)

section = page_py.section_by_title('See also')

page = 1
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SE_ID}&q=how+to+learn+{x}&start={start}"
data = requests.get(url).json()

print("="*65)
print("SOMETHING ABOUT THE TOPIC --->")
print("-"*65)
if page_py.exists():
  print("Topic: %s" % page_py.title)
  # Page - Title
  print("Summary: %s" % page_py.summary)
  # Page - Summary
  print("="*65)
  print("YOUR CURRICULAM --->")
  print("-"*65)
  print(section.text)
else:
  print("The page dosen't exist.")

print("="*65)
print("YOUR RESOURCES --->")
print("-"*65)
try:
  # get the resources
  search_items = data.get("items")
  # iterate over 10 resources found
  for i, search_item in enumerate(search_items, start=1):
    # get the page title
    title = search_item.get("title")
    # extract the page url
    link = search_item.get("link")
    # print the resources
    print("-"*25, f"Resources #{i+start-1}", "-"*25)
    print("Title:", title)
    print("URL:", link, "\n")
except:
  print("An error occoured.")