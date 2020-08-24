from bs4 import BeautifulSoup
import requests
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
import re


def get_script(base):
    base_url = 'https://transcripts.fandom.com/wiki/'
    url = base_url + base

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    script = soup.find(id='mw-content-text').find_all('b')
    script2 = [row.next_sibling for row in script]
    script3 = soup.find(id='mw-content-text').find_all('i')
    script4 = [row.text for row in script3]

    script5 = script2 + script4

    return ' '.join(str(v) for v in script5)

def get_script2(base):
    base_url = 'https://transcripts.fandom.com/wiki/'
    url = base_url + base

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    script = soup.find(id='mw-content-text').find_all('b')
    script2 = [row.next_sibling for row in script]
    script3 = soup.find(id='mw-content-text').find_all('i')
    script4 = [row.text for row in script3]
    script5 = soup.find(id='mw-content-text').find_all('ul')
    script6 = [row.text for row in script5]

    script7 = script2+script4+script6

    blob2 = [' '.join(str(v) for v in script7)]
    return blob2

def get_script3(base):
    base_url = 'https://transcripts.fandom.com/wiki/'
    url = base_url + base

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    script = soup.find(id='mw-content-text').find_all('b')
    script2 = [row.next_sibling for row in script]
    script3 = soup.find(id='mw-content-text').find_all('i')
    script4 = [row.text for row in script3]
    script5 = soup.find(id='mw-content-text').find_all('pre')
    script6 = [row.text for row in script5]

    script7 = script2+script4+script6

    blob3 = [' '.join(str(v) for v in script7)]
    return blob3


def lemmatizer_tokenizer(str_input):
    lemmatizer = WordNetLemmatizer()
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def verb_adj(text):
    v_adj = lambda pos: pos[:2] == 'JJ'
    tokenized = word_tokenize(text)
    adj = [word for (word, pos) in pos_tag(tokenized) if v_adj(pos)]
    return ' '.join(adj)