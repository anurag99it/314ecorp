import requests 
from bs4 import BeautifulSoup, SoupStrainer 
import operator 
import httplib2
from collections import Counter

allclean_list=[]
def start(url):
    wordlist = [] 
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.findAll('div', {'class':'entry-content'}): 
        content = each_text.text
        words = content.lower().split() 
          
        for each_word in words: 
            wordlist.append(each_word) 
        clean_wordlist(wordlist)
def create_dictionary(clean_list): 
    word_count = {} 
      
    for word in clean_list: 
            if word in word_count: 
                word_count[word] += 1
            else: 
                word_count[word] = 1    
            
    c = Counter(word_count) 
       # returns the most occurring elements 
    top = c.most_common(10) 
    print(top)  

def clean_wordlist(wordlist): 
      
    for word in wordlist: 
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
          
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '') 
              
        if len(word) > 0: 
            allclean_list.append(word)  
    
def getlinks(url):
    links=[]
    http = httplib2.Http()
    status, response = http.request(url)
    for link in BeautifulSoup(response, 'html.parser',parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            links.append(link['href'])
    return links        

url="https://www.314e.com"
c=1      
def begin(url):
          if c==4:
            return 0;
          else:
            ++c
            start(url)
            links=getlinks(url)
            if links:
                for link in links :
                    return begin(link)
begin(url)
create_dictionary(allclean_list)  

            
