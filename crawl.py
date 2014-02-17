index = {}

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def add_page_to_index(index,url,content):
    content_split = content.split()
    for con in content_split:
        add_to_index(index,con,url)
    return

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return index

print crawl_web("http://www.google.com")


#def add_to_index(index,keyword,url): # using list
#    for entry in index:
#        if entry[0] == keyword:
#            entry[1].append(url)
#            return
#    index.append([keyword,[url]])

#def lookup(index,keyword):
#    for i in index:
#        if i[0] == keyword:
#            return i[1]
#    return []