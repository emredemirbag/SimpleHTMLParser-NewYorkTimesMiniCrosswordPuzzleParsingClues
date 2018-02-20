#Simple HTML Parser program by Emre Demirbag https://github.com/emredemirbag
#This program sends HTTP request to New York Times Mini Crossword Puzzle,by Joel Fagliano,(https://www.nytimes.com/crosswords/game/mini) link and it parses clues from the page and writes to a text file.
#Libraries: requests:(http://docs.python-requests.org/en/master/), soup:(https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 


import requests
from bs4 import BeautifulSoup as Soup

session = requests.Session()

def getHTML(url):

	r = session.get(url)
	soup = Soup(r.content, "lxml")

	return soup

def getColoumns(soup):

	one = soup.find_all("div", {"class": "ClueList-wrapper--3m-kd"})

	html = ""

	for i in one:

		title = i.findAll("h3")

		html += " " + title[0].text + "\n"

		li = i.findAll("li")

		for j in li:
			span = j.findAll("span")
			html += " " + span[0].text.strip()  + " "+ span[1].text.strip() + "\n"

	return html
          

if __name__ == "__main__":

           

	url = "https://www.nytimes.com/crosswords/game/mini"

	s = getHTML(url)

	html = getColoumns(s)

	file_r = open("text.txt", "w")

	file_r.write(html)
	file_r.close()
