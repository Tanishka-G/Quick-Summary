#Tanishka Ghosh 
#Created: 2024-01-11
#Last Updated: 2024-01-11
#Webscrapper that takes in a word or phrase from the user, which is then
#searched in Wikipedia and the first paragraph is outputted as a summary
#of the topic. If there is an error or if there is more than one possible
#entries for the search term, the first possible entry listed on the 
#error page is used.

from bs4 import BeautifulSoup
import requests

#ask the user what they would like to learn about
print("Hello! What would you like to learn more about?")
word = input()

def find(word):
    #the start of all wikipedia url's, from where data is being scrapped
    url = "https://en.wikipedia.org/wiki/"

    #replace any space in the word with a underscore for the wikipedia url
    url = url + word.replace(" ", "_")

    #get the html from the url to parse it
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    summary = ""

    try:
        #find the main body of the page
        body = soup.find("div", {"class": "mw-content-ltr mw-parser-output"})

        #find all the paragraphs of the main body
        paras = body.find_all("p")

        #get the first paragraph containing actual content (more than 50 characters)
        for para in paras:
            #if there are multiple pages, pick the first one
            if "refer to" in para.text:            
                find(body.find("ul").find("a").get('title'))
                break
            if len(para.text) > 40:
                summary = para.text
                break
    except AttributeError:
        summary = "There seems to be an error, try a different word";

    #output the summary found to the user
    print(summary)

#call the find function to find what the user wants
find(word)
