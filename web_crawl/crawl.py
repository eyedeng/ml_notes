import time
from contin import continue_crawl
from find import find_first_link


start_url = "https://zh.wikipedia.org/wiki/Special:Random"
target_url = "https://zh.wikipedia.org/wiki/%E5%93%B2%E5%AD%A6"  # 哲学
article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    # add the first link to article_chain
    # delay for about two seconds
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break
    article_chain.append(first_link)
    time.sleep(2)


