from errno import EMEDIUMTYPE
import requests
import webbrowser
from requests import get
from PyPDF2 import PdfFileReader

'''imports'''
import requests
import time




import phonenumbers

# geocoder: to know the specific
# location to that phone number
from phonenumbers import geocoder

  
# carrier: to know the name of 
# service provider of that phone number
from phonenumbers import carrier



cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'




print(red+"""_____           _     _  ______                 _           _
  ___        __           ____       _   _               _               _____           _ 
 |_ _|_ __  / _| ___     / ___| __ _| |_| |__   ___ _ __(_)_ __   __ _  |_   _|__   ___ | |
  | || '_ \| |_ / _ \   | |  _ / _` | __| '_ \ / _ \ '__| | '_ \ / _` |   | |/ _ \ / _ \| |
  | || | | |  _| (_) |  | |_| | (_| | |_| | | |  __/ |  | | | | | (_| |   | | (_) | (_) | |
 |___|_| |_|_|  \___(_)  \____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |   |_|\___/ \___/|_|
                                                                 |___/                                                                                                           
""")

print(cyan+"Information gathering tool ")
print(cyan+"\nAll Copy Right Reserved |******")
print(red+"\n BY -- Akshay Bhardwaj\n\n")
print("\nA Project ")
#print(cyan+"\nUnder the guidance of Shivam sir")
print(y+""" +-+-+-+-+-+ +-+-+-+-+-+-+-+
               |I|G|N|O|U| |P|r|o|j|e|c|t|
               +-+-+-+-+-+ +-+-+-+-+-+-+-+  
      """)



# print("choose the option : - ")
print(green+"\n\nchoose the option : -\n(01)  - Information of the IP address \n(02)  - Reverse IP \n(03)  - PDF Analysis -  :  \n(04)  - Info from user name -  :")
print("\n\n\n")
print("_________________________________________________________")
ak =int(input())
if ak ==1:
    def iplocate():

        print(red+'''
         ██╗      ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ███████╗ ██████╗ ██████╗     ██╗██████╗                                   
         ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔════╝██╔═══██╗██╔══██╗    ██║██╔══██╗                                  
         ██║     ██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗    █████╗  ██║   ██║██████╔╝    ██║██████╔╝                                  
         ██║     ██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║    ██╔══╝  ██║   ██║██╔══██╗    ██║██╔═══╝                                   
         ███████╗╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝    ██║     ╚██████╔╝██║  ██║    ██║██║         ██╗██╗██╗██╗██╗██╗██╗██╗██╗██╗
         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝         ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
                                                                                                                                      
          ''')

        print(green+"[+] Searching for IP")
        

        ipinfo={}
        ip=input("Ip address >> ")
        url="http://ip-api.com/json/"+ip
        r=requests.get(url)
        ipinfo=r.json()
        if ipinfo['status'] == 'success':
            lat=ipinfo['lat']
            lon=ipinfo['lon']        
            print(green+"Ip location Found !!")
            print('Country     : ',ipinfo['country'])
            print('Region Name : ',ipinfo['regionName'])
            print('City        : ',ipinfo['city'])
            print('Time zone   : ',ipinfo['timezone'])
            print('ISP         : ',ipinfo['isp'])
            print(cyan+'Opening Location in browser')
            mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
            webbrowser.open(mapurl, new=2) 
            print('')
        else:
            print(red+"Ip location Not Found !!")



    if __name__=="__main__":
        iplocate()

elif ak ==2:
    def ReverseIP():
        print(red+"""
               ██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗        ██╗██████╗                             
               ██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝        ██║██╔══██╗                            
               ██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗          ██║██████╔╝                            
               ██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝          ██║██╔═══╝                             
               ██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗        ██║██║         ██╗██╗██╗██╗██╗██╗██╗██╗
               ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝        ╚═╝╚═╝         ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
                                                                                                             
                                                                                                                                           
                    """)
        host=input("Enter host >> ")
        lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
        try:
            result = get(lookup).text
            print(cyan+"[+]"+result)
        except:
            print(red+'Invalid IP address')
    if __name__=="__main__":
        ReverseIP()

elif ak ==3:
    def pdfinfo():
        print(red+'''
              ██████╗ ██████╗ ███████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███╗   ██╗ ██████╗                                   
              ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝                                   
              ██████╔╝██║  ██║█████╗      ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║██╔██╗ ██║██║  ███╗                                  
              ██╔═══╝ ██║  ██║██╔══╝      ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║██║╚██╗██║██║   ██║                                  
              ██║     ██████╔╝██║         ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║██║ ╚████║╚██████╔╝    ██╗██╗██╗██╗██╗██╗██╗██╗██╗██╗
              ╚═╝     ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
                                                                                                                                    
                                                                                                                                                                                                                  
          ''')
        filep=input("File path >> ")
        with open(filep, 'rb') as f:
                pdf = PdfFileReader(f)
                info = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()
        try:
            author = info.author
            creator = info.creator
            producer = info.producer 
            print(cyan+"[+] Author        : ",author)
            print(cyan+"[+] Creator       : ",creator)
            print(cyan+"[+] Producer      : ",producer)
            cdate=info['/CreationDate']
            cyear=cdate[2:6]
            cmonth=cdate[6:8]
            cd=cdate[8:10]
            print(C+"[+] Creation Date : ",cd,":",cmonth,":",cyear) 
            mdate=info['/ModDate']
            myear=cdate[2:6]
            mmonth=cdate[6:8]
            md=cdate[8:10]    
            print(C+"[+] Modified Date : ",md,":",mmonth,":",myear) 
        except:
            print(red+"[-] Meta data not available")
    if __name__=="__main__":
        pdfinfo()

elif ak ==4:
    ''' INPUT USERNAME TO FOR SEARCH '''
    username = input('\033[92m{+} Enter username to SEARCH: ')
# INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

# FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

#TWITTER
    twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
    youtube = f'https://www.youtube.com/{username}'

# BLOGGER
    blogger = f'https://{username}.blogspot.com'

# GOOGLE+
    google_plus = f'https://plus.google.com/s/{username}/top'

# REDDIT
    reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
    wordpress = f'https://{username}.wordpress.com'

# PINTEREST
    pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
    github = f'https://www.github.com/{username}'

# TUMBLR
    tumblr = f'https://{username}.tumblr.com'

# FLICKR
    flickr = f'https://www.flickr.com/people/{username}'

# STEAM
    steam = f'https://steamcommunity.com/id/{username}'

# VIMEO
    vimeo = f'https://vimeo.com/{username}'

# SOUNDCLOUD
    soundcloud = f'https://soundcloud.com/{username}'

# DISQUS
    disqus = f'https://disqus.com/by/{username}'
    


# # DEVIANTART
#     deviantart = f'https://{username}.deviantart.com'

# # VK
#     vk = f'https://vk.com/{username}'

# # ABOUT.ME
#     aboutme = f'https://about.me/{username}'

# # IMGUR
#     imgur = f'https://imgur.com/user/{username}'

# # FLIPBOARD
#     flipboard = f'https://flipboard.com/@{username}'

# # SLIDESHARE
#     slideshare = f'https://slideshare.net/{username}'

# # FOTOLOG
#     fotolog = f'https://fotolog.com/{username}'

# # SPOTIFY
#     spotify = f'https://open.spotify.com/user/{username}'

# # MIXCLOUD
#     mixcloud = f'https://www.mixcloud.com/{username}'

# # SCRIBD
#     scribd = f'https://www.scribd.com/{username}'

# # BADOO
#     badoo = f'https://www.badoo.com/en/{username}'

# # PATREON
#     patreon = f'https://www.patreon.com/{username}'

# # BITBUCKET
#     bitbucket = f'https://bitbucket.org/{username}'

# # DAILYMOTION
#     dailymotion = f'https://www.dailymotion.com/{username}'

# # ETSY
#     etsy = f'https://www.etsy.com/shop/{username}'

# # CASHME
#     cashme = f'https://cash.me/{username}'

# # BEHANCE
#     behance = f'https://www.behance.net/{username}'

# # GOODREADS
#     goodreads = f'https://www.goodreads.com/{username}'

# # INSTRUCTABLES
#     instructables = f'https://www.instructables.com/member/{username}'

# # KEYBASE
#     keybase = f'https://keybase.io/{username}'

# # KONGREGATE
#     kongregate = f'https://kongregate.com/accounts/{username}'

# # LIVEJOURNAL
#     livejournal = f'https://{username}.livejournal.com'

# # ANGELLIST
#     angellist = f'https://angel.co/{username}'

# # LAST.FM
#     last_fm = f'https://last.fm/user/{username}'

# # DRIBBBLE
#     dribbble = f'https://dribbble.com/{username}'

# # CODECADEMY
#     codecademy = f'https://www.codecademy.com/{username}'

# # GRAVATAR
#     gravatar = f'https://en.gravatar.com/{username}'

# # PASTEBIN
#     pastebin = f'https://pastebin.com/u/{username}'

# # FOURSQUARE
#     foursquare = f'https://foursquare.com/{username}'

# # ROBLOX
#     roblox = f'https://www.roblox.com/user.aspx?username={username}'

# # GUMROAD
#     gumroad = f'https://www.gumroad.com/{username}'

# # NEWSGROUND
#     newsground = f'https://{username}.newgrounds.com'

# # WATTPAD
#     wattpad = f'https://www.wattpad.com/user/{username}'

# # CANVA
#     canva = f'https://www.canva.com/{username}'

# # CREATIVEMARKET
#     creative_market = f'https://creativemarket.com/{username}'

# # TRAKT
#     trakt = f'https://www.trakt.tv/users/{username}'

# # 500PX
#     five_hundred_px = f'https://500px.com/{username}'

# # BUZZFEED
#     buzzfeed = f'https://buzzfeed.com/{username}'

# # TRIPADVISOR
#     tripadvisor = f'https://tripadvisor.com/members/{username}'

# # HUBPAGES
#     hubpages = f'https://{username}.hubpages.com'

# # CONTENTLY
#     contently = f'https://{username}.contently.com'

# # HOUZZ
#     houzz = f'https://houzz.com/user/{username}'

# #BLIP.FM
#     blipfm = f'https://blip.fm/{username}'

# # WIKIPEDIA
    # wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
    hackernews = f'https://news.ycombinator.com/user?id={username}'

# # CODEMENTOR
#     codementor = f'https://www.codementor.io/{username}'

# # REVERBNATION
#     reverb_nation = f'https://www.reverbnation.com/{username}'

# # DESIGNSPIRATION
#     designspiration = f'https://www.designspiration.net/{username}'

# # BANDCAMP
#     bandcamp = f'https://www.bandcamp.com/{username}'

# # COLOURLOVERS
#     colourlovers = f'https://www.colourlovers.com/love/{username}'

# # IFTTT
    # ifttt = f'https://www.ifttt.com/p/{username}'

# # EBAY
#     ebay = f'https://www.ebay.com/usr/{username}'

# # SLACK
#     slack = f'https://{username}.slack.com'

# # OKCUPID
#     okcupid = f'https://www.okcupid.com/profile/{username}'

# # TRIP
#     trip = f'https://www.trip.skyscanner.com/user/{username}'

# # ELLO
#     ello = f'https://ello.co/{username}'

# # TRACKY
#     tracky = f'https://tracky.com/user/~{username}'

# BASECAMP
    basecamp = f'https://{username}.basecamphq.com/login'


    ''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
    WEBSITES = [
    instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
    wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus,basecamp,hackernews
    # EMEDIUMTYPE, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
    # mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
    # goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
    # dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
    # wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
    # contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
    # bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
    ]


    ''' COLOUR PRINTING FUNCTION '''
    def outer_func(colour):
        def inner_function(msg):
            print(f'{colour}{msg}')
        return inner_function
    
    
    ''' COLOUR PRINTS '''
    GREEN = outer_func('\033[92m')
    YELLOW = outer_func('\033[93m')
    RED = outer_func('\033[91m')
    
    
    ''' BANNER '''
    def banner():
        YELLOW(red+'''
      _                 _    _                      
     | |               | |  (_)                     
     | |     ___   ___ | | ___ _ __   __ _   ______ 
     | |    / _ \ / _ \| |/ / | '_ \ / _` | |______|
     | |___| (_) | (_) |   <| | | | | (_| |         
     |______\___/ \___/|_|\_\_|_| |_|\__, |         
                                      __/ |         
                                     |___/          
             _          ______
            | |        | |    \ 
            | |        | |     |
            | |        | |     |
            | |        | |     |
            | |        | |     |
            |_|        |_|____/
      ''')

    
    def search():
        GREEN(f'[+] Searching for username:{username}')
        time.sleep(1)
        print('.......')
        time.sleep(1)
        print('.......\n')
        time.sleep(1)
    
        GREEN(f'[+] Looking-IP is working\n')
        time.sleep(1)
        print('.......')
        time.sleep(1)
        print('.......\n')
        time.sleep(1)
    
        time.sleep(2)
    
        count = 0
        match = True
        for url in WEBSITES:
            r = requests.get(url)
    
            if r.status_code == 200:
                if match == True:
                    GREEN('[+] FOUND MATCHES')
                    match = False
                YELLOW(f'\n{url} - OK')
                if username in r.text:
                    GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
                else:
                    GREEN(f'POSITIVE MATCH: Username:{username} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')#
            count += 1
    
        total = len(WEBSITES)
        GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')
    
    
    
    if __name__=='__main__':
        banner()
        search()   
           
else :
    
    print(red+"""
         ████████╗██████╗ ██╗   ██╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗
         ╚══██╔══╝██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║
            ██║   ██████╔╝ ╚████╔╝     ███████║██║  ███╗███████║██║██╔██╗ ██║
            ██║   ██╔══██╗  ╚██╔╝      ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║
            ██║   ██║  ██║   ██║       ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║
            ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
                                                                    
          """)
    print("\n Please Select correct option :")
    print("\n Try again")
