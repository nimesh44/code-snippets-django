from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def translate(request):
    if request.method == 'POST':
        data = request.POST
        word = data.get('word')
        print(word)
        # Alternatively
        word = data['word']
        # print(word)

        # GET request to website
        payload ={'q':word}
        r = requests.get('http://www.englishnepalidictionary.com/',params=payload)
        # To see request url
        print(r.url)
        # To see respose
        print(dir(r))

        # Getting only text from response
        request_ = requests.get('http://www.englishnepalidictionary.com/',params=payload).text
        # return response in the form of html
        soup = bs(request_,'lxml')
        print(soup)

        # getting meaning by evaluating specific class and tag where meaning is returned
        # by analysing corresponding meaning in network response

        # return h3 tag
        word_meaning_ = soup.find('div',class_ = 'search-result').h3
        print(word_meaning_)

        # return text inside h3 tag
        word_meaning = soup.find('div',class_= 'search-result').h3.text
        print(word_meaning)

        context = {
            'word_meaning':word_meaning
        }

    return render(request,'templates/translate.html',context)
