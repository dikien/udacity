# -*- coding: UTF-8 -*-
from __future__ import division
import os,copy,re,timeit,math,itertools,time,string,cProfile
import cookielib
from bs4 import BeautifulSoup
import chardet
import HTMLParser
import mechanize
from string import punctuation


html_parser = HTMLParser.HTMLParser()

def get_page(url): # 특정페이지를 출력(한글로변환)
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
    cj = cookielib.LWPCookieJar()
    br.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    #response = br.open("http://news.chosun.com/svc/list_in/list.html?catid=2&indate=20120921&source=1&pn=1")
    response = br.open(url)
    contents = response.read()
    contents = unicode(contents, 'euc-kr').encode('utf-8')
    return html_parser.unescape(contents)

    
def get_articles(url): 
    data = get_page(url)
    soup = BeautifulSoup(data)
    soup.prettify()
    content = soup.findAll("div", { "class" : "artcle_txt" })
    tmp = []
    for i in range(len(content)):
        tmp.append(''.join([e for e in content[i].recursiveChildGenerator() if isinstance(e,unicode)]))
        tmp[i] = re.sub('[a-zA-Z]+|[0-9]+.|\s+',' ',tmp[i])
        for p in list(punctuation):
            tmp[i] = tmp[i].replace(p,' ')
            tmp[i] = tmp[i].replace("“",' ').replace("”",' ').replace("·",' ').replace("△",' ').replace("■",' ').replace("‘",' ').replace("’",' ').replace("…",' ').replace("【서울 뉴시스】",' ').replace("▲",' ').replace("⊙",' ').replace("◇",' ').replace("▶",' ').replace("◆",' ').replace("【춘천 뉴시스】",' ').replace("연합뉴스",' ').replace("관련기사",' ').replace("키워드",' ').replace("동영상",' ').replace("관련블로그",' ').replace("관련연재",' ')
            tmp[i] = tmp[i].strip()
            tmp[i] = re.sub('  ',' ',tmp[i])
    content = "".join(tmp)
    return content, str(len(content)) 


def get_urls(url):
    data = get_page(url) 
    soup = BeautifulSoup(data)
    soup.prettify()
    basic_url = "http://news.donga.com"
    contents = soup.findAll("p", { "class" : "title" })
    for content in contents:
        if str(content) != '\n':
            data1 = str(content)
            soup1 = BeautifulSoup(data1)
            for link in soup1.findAll('p'):
                url = basic_url + str(link.contents[1]['href'])
                try:
                    final_content = get_articles(url)[0] # 기사내용
                    final_content_length = str(len(final_content)) # 기사길이
                except:
                    final_content = "None"
                    final_content_length = "None"
                    print url + " Error: try again"
                if len(link.contents[1].contents) != 0: # 기사제목이 없을때 에러방지
                    final_title = str(link.contents[1].contents[0])
                else:
                    final_title = ""
                for p in list(punctuation):
                    final_title = final_title.replace(p,' ')
                    final_title = final_title.replace("“",' ').replace("”",' ').replace("·",' ').replace("△",' ').replace("■",' ').replace("‘",' ').replace("’",' ').replace("…",' ').replace("▲",' ').replace("⊙",' ').replace("◇",' ').replace("▶",' ').replace("◆",' ')
                    final_title = final_title.strip()
                    final_title = re.sub('  ',' ',final_title)                        
                year = str(link.contents[3])[7:11] 
                month = str(link.contents[3])[12:14]
                day = str(link.contents[3])[15:17]
                print final_content           


print get_urls("http://news.donga.com/Economy_List/2&s=0")
