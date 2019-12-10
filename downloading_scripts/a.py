import requests
import re
from bs4 import BeautifulSoup
import random
import os
import time
from selenium import webdriver
import webbrowser
import random
random = random.randint(1,100)

var = 9 # IF Website Changes, THis Must Be Updated

# reads inital urls from TikToks.txt
def url_Reader():
    with open("TikToks.txt", 'r+',encoding="cp437") as links:
        link_reader = links.read()
        url_copier = re.findall(r'http://vm.tiktok.com/[aA-zZ0-9]+/', link_reader)
    return url_copier


def cUrl():
    dUrl_Caller = url_Reader() #[0]
    print(dUrl_Caller)
    # print(dUrl_Caller)
    final_contest = []
    beta = 0
    for i in dUrl_Caller:
        with requests.session() as myrequest:
            #print(i)
            obtain_info = myrequest.get(
                i,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                    "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
            )
            beta+=1
            soup = BeautifulSoup(obtain_info.text, 'html.parser')
            #print(soup.encode('UTF-8'))
            # "soup obtained for number: " + str(beta))


            #codes: v09044c80000binse7c108gtvk2r1cog && v09044020000binaqr9rt1gpfgn3b52g
            # v09044c80000binse7c108gtvk2r1cog video=id; uri; url_key
            Direct_Txt = open("TikTokDLUrls.txt", 'w')
            for img in soup.find_all('script')[var]:
                Direct_Txt.write(str(img.encode('utf-8')))



            Direct_Txt.close()
            #dr_read = open("TikTokDLUrls.txt","r")
            #print(dr_read.read())


            with open("TikTokDLUrls.txt", 'r+') as orgnial_files:
                contents = orgnial_files.read()
                #print(contents)

            # (?="uri":")"uri":"[a-z0-9]{32}
            new_contest = re.findall(r'(?<=video_id=)[a-z0-9]+' ,contents)
           #print(new_contest)
            orgnial_files.close()
            #removes temporary

            templer = list(set(new_contest))

            final_contest.append(templer)

#str_list = filter(None, str_list) # fastest

    #print(final_contest)
    return final_contest



def fUrl():
    complete_url = []
    dyanmic = cUrl()
    print(dyanmic)
    base = 'https://api2.musical.ly/aweme/v1/play/?video_id='
    for i in dyanmic:
        for j in i:
            adder = base + str(j)
            complete_url.append(adder)


    print(complete_url)
    return complete_url


def uOpner():
    beta = 0
    tOpen = fUrl()
    for i in tOpen:
        webbrowser.open_new(i)
        beta+=1
    print("you opened %s" % beta + " tiktoks") # Direct_Txt.write("%s\n" % img)
    return beta

R = uOpner()
