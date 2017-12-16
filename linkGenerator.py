from contextlib import closing
from selenium.webdriver import PhantomJS
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def getHtmlSource(url,time=10):
    with closing(Firefox()) as browser:
        browser.get(url)
        WebDriverWait(browser,timeout=time)
        source=browser.page_source
    return source
def getLinks(url):
    source=getHtmlSource(url)
    soup=BeautifulSoup(source,'html.parser')
    divs= soup.findAll("div", { "class" : "l-u-Ab-T-j" })
    names=soup.findAll("span",{ "class" : "l-Ab-T-r" })
    #print(names)
    lnames=[]
    links=[]
    for name in names:
        lnames.append(name.text)
    for div in divs:
        ids=div.get("id")
        ids=ids.lstrip(":g.")
        ids=ids.rstrip(":label")
        links.append(ids)
    for n,l in zip(names,ids):
        print("video={}\nDownload_link=https://drive.google.com/uc?export=download&id={}\n".format(n,l))
if __name__=="__main__":
    url="" #enter the url
    getLinks(url)

