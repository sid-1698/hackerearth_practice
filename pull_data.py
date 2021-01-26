from bs4 import BeautifulSoup
import urllib.request
import requests
import os

site = "https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/"
soup = BeautifulSoup(requests.get(site).content, "html.parser")
problems = soup.find_all("h4",{"class":"prob-title"})
path = "./Basic_Programming/Basics_of_Input_Output/"
if os.path.exists(path) == False:
    os.makedirs(path)

page = 1
next_page = 1
while next_page >= page:

    soup = BeautifulSoup(requests.get(site).content, "html.parser")
    problems = soup.find_all("h4",{"class":"prob-title"})
    for prob in problems:
        link = prob.find("a").get("href")
        link = "https://www.hackerearth.com/"+link
        prob_name = link.split("/")[-2]
        prob_name = prob_name.replace("-","_")
        if os.path.exists(path+prob_name+".py") == False:
            with open(path+prob_name+".py", "w+") as file:
                file.write("# "+link)
    navs = soup.find_all("a",{"class":"load-prob-pagination"})

    for item in navs:
        try:
            next_page = int(item.find("span").text)
            next_page_link = item.get("href")
            if next_page > page:
                break
        except:
            pass
    next_page_link = "/".join(next_page_link.split("/")[:-1])
    site = "https://www.hackerearth.com"+next_page_link
    page += 1


