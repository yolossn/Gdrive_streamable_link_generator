from contextlib import closing
from selenium.webdriver import PhantomJS
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def getHtmlSource(url,time=20):
    with closing(Firefox()) as browser:
        browser.get(url)
        WebDriverWait(browser,timeout=time)
        source=browser.page_source
    return source
def getLinks(url):
    source=getHtmlSource(url)
    soup=BeautifulSoup(source,'html.parser')
    dclass="l-u-Ab-T-j"
    links=soup.div["l-u-Ab-T-j"]
    print(links)
#if __name__=="main":
#print(getHtmlSource("https://drive.google.com/drive/folders/0ByWO0aO1eI_MSlZkQU96NGo4SW8"))
getLinks("https://drive.google.com/drive/folders/0ByWO0aO1eI_MSlZkQU96NGo4SW8")
