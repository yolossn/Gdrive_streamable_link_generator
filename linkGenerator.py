from selenium.webdriver import PhantomJS
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
import argparse
def getHtmlSource(url,time=10):
    driver=PhantomJS( service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
    driver.get(url)
    WebDriverWait(driver,timeout=time)
    source=driver.page_source
    #driver.save_screenshot('a.png')
    return source

def getLinks(url):
    source=getHtmlSource(url)
    soup=BeautifulSoup(source,'html.parser')
    divs= soup.findAll("div", { "class" : "l-u-Ab-T-j" })
    names=soup.findAll("span",{ "class" : "l-Ab-T-r" })
    def ids(x):
        x=x.get("id")
        x=x.lstrip(":g.")
        x=x.rstrip(":label")
        return x
    names=[span.text for span in names]
    divs=[ids(div) for div in divs]
    links={}
    print(names)
    print(divs)
    for name,div in zip(names,divs):
        url="https://drive.google.com/uc?export=download&id={}".format(div)
        resp=requests.head(url)
        print(url)
        if resp.status_code!=404:
            links[name]=url
            print("video={}\nDownload_link={}\n".format(name,url))
    return links
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("url",help="enter the Gdrive link",type=str)
    args=parser.parse_args()
    url=args.url
    links=getLinks(url)


