import requests
from bs4 import BeautifulSoup
r=requests.get("https://topnovelbooks.com/novel-book-full/outside-of-time/chapter-1-surviving-1")
soup= BeautifulSoup(r.content, 'html.parser')


n=30
while n<300:
    f0=open("fileno%d.txt"%n,"w")
    print(file=f0)
    


    number=0
    while number <10:
        a= (soup.find('p').get_text())    
        f1= open("fileno%d.txt"%n, "a",encoding='utf-8')
        tit=soup.find("span", {"class": "chr-text"}).get_text(strip=True)
        print(tit,file=f1)
        print(a, file=f1)

        for i in soup.find_all('a',{"id":'next_chap'} ,href=True):
            if('https://topnovelbooks.com/novel-book-full/outside-of-time' in i['href']):
                nextpage=requests.get(i['href'])
                nextsoup=BeautifulSoup(nextpage.content,'html.parser')
        
                b= (nextsoup.find('p').get_text())
            
        soup=nextsoup
        a=b
        number = number + 1
        print(number)
        
        f1.close()


    f0.close()
    n=n+10   




