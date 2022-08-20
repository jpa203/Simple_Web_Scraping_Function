import bs4
import requests
def WebScraping(url): # creating a web scraping function that takes a url as an input
    res = requests.get(url)
    try: #try and except statement in case an error occurs 
        res.raise_for_status()
    except AssertionError:
        print('Something is wrong with the link!')

    soup = bs4.BeautifulSoup(res.text) #call BeautifulSoup to pull data from HTLM/XML files.
    elems = soup.select(css) #enter the CSS selector link here.
    return elems[0].text.strip() #text inside html element (as a list) and removed white space


check = WebScraping(url)
print('This is what you requested' + check)
