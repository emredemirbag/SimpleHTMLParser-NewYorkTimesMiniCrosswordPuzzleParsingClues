#Simple HTML Parser coded by Emre Demirbag https://github.com/emredemirbag
#New York Times Mini Crossword Puzzle,by Joel Fagliano,(https://www.nytimes.com/crosswords/game/mini) link and it parses clues from the page writes to html file.
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

	html = "<html><body>"

	for i in one:

		title = i.findAll("h3")

		html += "<h3>" + title[0].text.strip() + "</h3><ul>"

		li = i.findAll("li")

		for j in li:
			html += "<li>"
			span = j.findAll("span")
			html += "<span><b>" + span[0].text.strip() + ".</b></span> <span>" + span[1].text.strip() + "</span></li>"
		html += "</ul>"

	html += "</body></html>"
	return html


if __name__ == "__main__":

	url = "https://www.nytimes.com/crosswords/game/mini"

	s = getHTML(url)

	html = getColoumns(s)


	htmlFile = open("a.html", "w")
	htmlFile.write(html)
	htmlFile.close()
