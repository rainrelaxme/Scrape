"""将网页的内容爬虫回来，存入txt文件内"""

from urllib.request import urlopen

html = urlopen("http://www.baidu.com")
content = str(html.read())

file = open("scrapeContent.txt", mode = "w")
print(type(content))
file.write(content)
# (content)
