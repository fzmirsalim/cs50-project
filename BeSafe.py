# library
import string
from random import*
import colorama
from colorama import*

# reset colors of texts
print(Style.RESET_ALL)

title = "Be Safe"
print(Back.RED + Fore.BLACK + "{0:*^50}".format(title))
print(Style.RESET_ALL)
print(Back.WHITE + Fore.BLUE + "\n\nFOR EXIT PROGRAM TYPE EXIT")


while True:
    # rest colors of texts
    print(Style.RESET_ALL)
    
    # get user input to decide which program start
    INPUT_DECIDING = input(Fore.WHITE +"""\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
    # check user input
    while True:
        # variables
        digits = string.digits
        punctuation = string.punctuation
        letters = string.ascii_letters
        
        
        if INPUT_DECIDING == "" or INPUT_DECIDING.isspace():
            INPUT_DECIDING = input(Fore.LIGHTRED_EX + """\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
        
        elif INPUT_DECIDING in ["exit", "EXIT"]:
            quit()
            
        elif INPUT_DECIDING in digits:
            INPUT_DECIDING = int(INPUT_DECIDING)
            if INPUT_DECIDING == 0:
                INPUT_DECIDING = input(Fore.LIGHTRED_EX + """\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
                
            elif INPUT_DECIDING <= 3:
                break
            
            else:
                INPUT_DECIDING = input(Fore.LIGHTRED_EX + """\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
        
        elif INPUT_DECIDING in (punctuation or letters):
            INPUT_DECIDING = input(Fore.LIGHTRED_EX + """\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
        
        else:
            INPUT_DECIDING = input(Fore.LIGHTRED_EX + """\nchoose one of this: 
1. check that it is fake page or not
2. check how much your password is strong
3. make strong password

_ import number of a item >> """)
    
    
    
    # check that we need run which program        
    if INPUT_DECIDING == 1:
        # START LINK PROGRAM
        
        print(Style.RESET_ALL)
        # list of site
        SITES_NAMES = ["sky", "yelp", "amazon", "amazon french", "french amazon", "psychologytoday", "shutterstock", "hatena", "discord", "20minutos", "biglobe", "gooyaabitemplates", "abc", "wikia", "ytimg", "espn", "alexa", "doubleclick", "indiatimes", "naver", "apache", "google", "wikipedia", "japaneasewikipedia", "wikipediajapanease", "discord", "express", "shopify", "ft", "financialtimes", "spiegel", "theatlantic", "nydailynews", "nginx", "news", "disqus", "loc", "libraryofcongress", "mit", "php", "sciencedirect", "gofundme", "engadget", "mysql", "lg", "cbc", "ruwikipidi", "russianwikipedia", "wikipediarussian", "smh", "outlook","cornell", "spotify", "lycos", "storagegoogleapis", "googleapisstorage", "googlestorage", "netflix", "bitly", "themeforest", "pbs", "sciencemag", "picasagoogle", "googlpicasa", "lefigaro", "usnews", "over blog", "mega", "erecht24", "berkeley", "home", "tripadvisor", "yadi", "oracle", "fb", "alibaba", "metro", "afternic", "nationalgeographic", "discord", "over-blog", "overblog", "nbcnews", "akamaihd", "whitehouse", "deezer", "mashable", "icann", "plwikipedia", "PolishWikipedia", "WikipediaPolish", "4shared", "welt", "indonesianwikipedia", "wikipediaindonesia", "id.wikipedia", "nikkei", "ziddu", "disney", "sedo", "detik", "??ox.ac", "eventbrite", "box", "gmail", "thetimes", "rtve", "allaboutcookies", "wikihow", "cnil", "rt", "stanford", "nature", "washington", "cnbc", "godaddy", "amazon", "zendesk", "cambridge", "????adsesetting", "rambler", "wikipedia", "theverge", "about", "ea", "sfgate", "google", "variety", "twitch", "googleblog", "ikea", "target", "yandex", "????bp2.blogger", "mailchimp", "epa", "qq", "entrepreneur", "????so-net", "imgur", "wn", "mystrikingly", "thestar", "undeveloped", "behance", "coursera", "corriere", "nvidia", "about", "springer", "???group.yahooo", "vkontakte", "airbnb", "ca", "skype", "oecd", "thehindu", "tiktok", "prezi", "doi", "irs", "dreniq", "ucoz", "steamcommunity", "arstechnica", "hbr", "aparat", "digikala", "varzesh3", "shaparak", "telewebion", "namnak", "divar", "namasha", "ninisite", "farsnews", "khabargozarifaes", "filimo.com", "bankmellat", "beytoote", "fararu", "setare", "jamnews????????", "rokna", "khabarnegaranjavan", "yjc", "asriran", "dalfak", "tsetmc", "bmi", "soft98", "blogfa", "wikipedia", "shomanews", "isna", "donyaeeqtesad", "tarafdari", "tci", "sheypoor", "agah", "tasnimnews", "sanjesh", "tamin", "sazmansanjesh", "delgarm", "blog", "argamag", "arga-mag", "parsfootball", "mehrnews", "mehr", "khabargozarimehr", "mofidonline", "mofid", "kargozarimofid", "emalls", "tabnak", "bankmeliiran", "time", "khabaronline", "popfa", "tamasha", "post", "chetor", "tehran", "cafebazaar", "donyaeeghtesad", "cafebazar", "mokhaberatiran", "mokhaberat", "namava", "???bpi", "sahamyab", "afkarnews", "afkar", "khabargozariafkar", "e-estekhdam", "estekhdam", "eestekhdam", "irancell", "asiatech", "didestan", "takhfifan", "mci", "snappfood", "fardanews", "farda", "khabargozarifarda", "niniban", "??cbi", "postbank", "toplearn", "edbi", "ttbank", "bankrefah", "banksepah", "bankmarkazi", "banksanatmadan", "bim", "bankgharzolhasane", "qmb", "bankghavamin", "ghbi", "bankkeshavarzi", "agribank", "bankagri", "bankmaskan", "bank-maskan", "bankansar", "ansarbank", "amraheman", "hamrahaval", "bankeghtesadnovin", "enbank", "bankiranzamin", "iranibank", "bankiran", "bankayande", "tatbank", "parsian-bank", "parsianbank", "bankparsian", "bankpasargad", "bpi", "bankhakmatiranian", "hibank24", "bank-day", "bankday", "sinabank", "banksina", "sb24", "sbank", "citybank", "city-bank", "bankshahr", "???bsi", "rqbank", "karafarinbank", "bankkarafarin", "tourismbank", "bankmellat", "tejaratbank", "banktejarat", "namava", "youtube", "apple", "google", "googleplay", "cloudflare", "microsoft", "googlesupport", "blogge", "wordpress", "mozilla", "englishwikipedia", "wikipediaenglish", "enwikipedia", "googlemaps", "docsgoogle", "docgoogle", "googledocs", "googledoc", "linkedin", "youtu", "gooledrive", "googleplus", "adobe", "googlesites", "googlesite", "vimeo", "googleusercontent", "googleaccounts", "europa", "facebook", "telegram", "istockphoto", "uol", "github", "vk", "bpblogspot", "blogspotbp", "whatsapp", "amazon", "bbc", "paypal", "terra", "gstatic", "nih", "netvibes", "nytimes", "who", "hugedomains", "slideshare", "issuu", "globo", "newsgoogle", "googlenews", "frwikipedia", "francewikipedia", "wikipediafrance", "policiesgoogle", "googlepolicies", "feedburner", "???ptwikipedia", "cnn", "bbc", "w3", "eswikipedia", "mail", "googlemail", "mailgoogle", "brandbucket", "weebly", "forbes", "google", "creativecommons", "wikimedia", "theguardian", "dropbox", "washingtonpost", "google", "myspace", "reuters", "google", "medium", "msn", "yahoo", "live", "opera", "googledevelopers", "developersgoogle", "google", "dailymotion", "t???", "telegram", "cpanel", "ft", "harvard", "googlebooks", "booksgoogle", "wired", "twitter", "office", "abril", "pinterest", "telegraph", "elpais", "fileswordpress", "wordpressfiles", "mediafire", "google", "elmundo", "fandom", "fb", "fb", "telegram", "independent", "independent", "draftblogger", "bloggerdraft", "thesun", "translategoogle", "googletranslate", "huffpost", "android", "wa", "bloomberg", "booking", "ok", "???ok", "amazon", "google", "soundcloud", "yahoonews", "newsyahoo", "googlephotos", "photosgoogle", "aliexpress", "bit", "bitly", "steampowered", "tinyurl", "picasawebgoogle", "googlepicasaweb", "searchgoogle", "googlesearch", "google", "amazon", "foxnews", "samsung", "amazon", "ebay", "businessinsider", "nasa", "ig", "aboutads", "time", "usatoday", "cnet", "abcnews", "scribd", "myaccountgoogle", "googlemyaccount", "change", "getgoogle", "googleget", "dan", "archive", "youronlinechoices", "dailymail", "itwikipedia", "gov", "gravatar", "enablejavascript", "forms", "cbsnews", "google", "googlemarketingplatform", "marketingplatformgoogle", "mirror", "cdc", "namecheap", "dewikipedia", "plesk", "cpanel", "networkadvertising", "jimdofree", "berkeley", "amazon", "hollywoodreporter","clickbank", "biglobe", "quora", "target", "abc", "wix", "ign", "gnu", "gizmodo", "walmart","bandcamp", "mwikipedia", "lemonde", "googlecode", "codegoogle", "weibo", "ria", "nypost", "addtoany", "rottentomatoes", "wp", "guardian", "imageshack", "news", "disqus", "loc", "afternic", "php", "googleadssettings", "adssettingsgoogle", "nginx", "washington", "stackoverflow", "lg", "tmz", "storagegoogleapis", "netflix", "shopify", "express", "addthis.", "themeforest", "mozilla", "googlepicasa", "picasagoogle", "lefigaro", "usnewss", "hm", "oup", "mega", "fb", "alibaba", "akamaihd", "amazon", "arxiv", "amzn", "deezer", "google", "nationalgeographic", "ietf", "hp", "google", "fda", "secureserver", "ibm", "whitehouse", "4shared", "welt", "zoom", "techcrunch", "newsweek", "disney", "eventbrite", "wikihow", "stanford", "economist", "netlify", "rambler", "???smh", "twitch", "kafebook", "shabestan", "instagram"]
        SITES_LINKS = ["sky.com", "yelp.com", "amazon.fr", "psychologytoday.com", "shutterstock.com", "hatena.ne.jp", "discord.gg", "20minutos.es", "biglobe.ne.jp", "gooyaabitemplates.com", "abc.es", "wikia.com", "ytimg.com", "espn.com", "alexa.com", "doubleclick.net", "indiatimes.com", "naver.com", "apache.org", "google.co.id", "ja.wikipedia.org", "discord.com", "express.co.uk", "shopify.com", "ft.com", "spiegel.de", "theatlantic.com", "nydailynews.com", "nginx.com", "news.com.au", "disqus.com", "loc.gov", "mit.edu", "php.net", "sciencedirect.com", "gofundme.com", "engadget.com", "mysql.com", "lg.com", "cbc.ca", "ru.wikipedia.org", "smh.com.au", "outlook.com", "cornell.edu", "spotify.com", "lycos.com", "storage.googleapis.com", "netflix.com", "bitly.com", "themeforest.net", "pbs.org", "sciencemag.org", "picasa.google.com", "lefigaro.fr", "usnews.com", "over-blog.com", "mega.nz", "e-recht24.de", "berkeley.edu", "home.neustar", "tripadvisor.com", "yadi.sk", "oracle.com", "fb.me", "alibaba.com", "metro.co.uk", "afternic.com", "nationalgeographic.com", "arxiv.org", "bing.com", "nbcnews.com", "akamaihd.net", "whitehouse.gov", "deezer.com", "mashable.com", "icann.org", "pl.wikipedia.org ", "4shared.com", "welt.de", "id.wikipedia.org", "nikkei.com", "ziddu.com", "disney.com", "sedo.com", "detik.com", "ox.ac.uk", "eventbrite.com", "box.com", "gmail.com", "thetimes.co.uk", "rtve.es", "allaboutcookies.org", "wikihow.com", "cnil.fr", "rt.com", "stanford.edu", "nature.com", "washington.edu", "cnbc.com", "godaddy.com", "amazon.it", "zendesk.com", "cambridge.org", "adssettings.google.com", "rambler.ru", "wikipedia.org", "theverge.com", "about.com", "ea.com", "sfgate.com", "google.ca", "variety.com", "twitch.tv", "googleblog.com", "ikea.com", "target.com", "yandex.ru", "bp2.blogger.com", "mailchimp.com", "epa.gov", "qq.com", "entrepreneur.com", "so-net.ne.jp", "imgur.com", "wn.com", "mystrikingly.com", "thestar.com", "undeveloped.com", "behance.net", "coursera.org", "corriere.it", "nvidia.com", "about.me", "springer.com", "groups.yahoo.com", "vkontakte.ru", "airbnb.com", "ca.gov", "skype.com", "oecd.org", "thehindu.com", "tiktok.com", "prezi.com", "doi.org", "irs.gov", "dreniq.com", "ucoz.ru", "steamcommunity.com", "arstechnica.com", "hbr.org", "aparat.com", "digikala.com", "varzesh3.com", "shaparak.ir", "telewebion.com", "namnak.com", "divar.ir", "namasha.com", "ninisite.com", "farsnews.com", "filimo.com", "bankmellat.ir", "beytoote.com", "fararu.com", "setare.com", "jamnews.com", "rokna.net", "yjc.ir", "asriran.com", "dalfak.com", "tsetmc.com", "bmi.ir", "soft98.ir", "blogfa.com", "wikipedia.org", "shomanews.com", "isna.ir", "donya-e-eqtesad.com", "tarafdari.com", "tci.ir", "sheypoor.com", "agah.com", "tasnimnews.com", "sanjesh.org", "tamin.ir", "delgarm.com", "blog.ir", "arga-mag.com", "parsfootball.com", "mehrnews.com", "mofidonline.com", "torob.com", "yektanet.com", "emalls.ir", "tabnak.ir", "time.ir", "khabaronline.ir", "popfa.ir", "tamasha.com", "post.ir", "chetor.com", "tehran.ir", "cafebazaar.ir", "namava.ir", "bpi.ir", "sahamyab.com", "afkarnews.com", "e-estekhdam.com", "alibaba.ir", "shatel.ir", "irancell.ir", "asiatech.ir", "didestan.com", "takhfifan.com", "mci.ir", "snappfood.ir", "fardanews.com", "mobile.ir", "faradars.org", "niniban.com", "cbi.ir", "postbank.ir", "toplearn.com", "edbi.ir", "ttbank.ir", "bankrefah.ir", "banksepah.ir", "bim.ir", "qmb.ir", "ghbi.ir", "agri-bank.com", "bank-maskan.ir", "ansarbank.com", "enbank.ir", "iranibank.com", "tatbank.ir", "parsian-bank.com", "bpi.ir", "hibank24.com", "bank-day.ir", "sinabank.ir", "sb24.com", "sbank.ir", "city-bank.ir", "bsi.ir", "rqbank.ir", "karafarinbank.com", "tourismbank.ir", "bankmellat.ir", "tejaratbank.ir", "namava.ir", "amazon.ca", "youtube.com", "apple.com", "google.com", "play.google.com", "cloudflare.com", "microsoft.com", "support.google.com", "blogger.com", "wordpress.org", "mozilla.org", "en.wikipedia.org", "maps.google.com", "docs.google.com", "linkedin.com", "youtu.be", "drive.google.com", "plus.google.com", "adobe.com", "sites.google.com", "vimeo.com", "googleusercontent.com", "accounts.google.com", "europa.eu", "facebook.com", "t.me", "istockphoto.com", "uol.com.br", "github.com", "vk.com", "bp.blogspot.com", "whatsapp.com", "amazon.com", "bbc.co.uk", "paypal.com", "terra.com.br", "gstatic.com", "nih.gov", "netvibes.com", "nytimes.com", "who.int", "hugedomains.com", "slideshare.net", "issuu.com", "globo.com", "news.google.com", "fr.wikipedia.org", "policies.google.com", "feedburner.com", "pt.wikipedia.org", "cnn.com", "bbc.com", "w3.org", "es.wikipedia.org", "mail.ru", "mail.google.com", "brandbucket.com", "weebly.com", "forbes.com", "google.co.jp", "creativecommons.org", "wikimedia.org", "theguardian.com", "dropbox.com", "washingtonpost.com", "google.de", "myspace.com", "reuters.com", "google.com.br", "line.me", "medium.com", "msn.com", "imdb.com", "yahoo.com", "live.com", "opera.com", "developers.google.com", "google.es", "dailymotion.com", "t.co", "cpanel.com", "ft.com", "harvard.edu", "books.google.com", "wired.com", "twitter.com", "office.com", "abril.com.br", "pinterest.com", "telegraph.co.uk", "elpais.com", "files.wordpress.com", "mediafire.com", "google.it", "elmundo.es", "fandom.com", "fb.com", "telegram.me", "independent.co.uk", "draft.blogger.com", "thesun.co.uk", "translate.google.com", "huffpost.com", "android.com", "wa.me", "bloomberg.com", "booking.com", "ok.ru", "amazon.de", "google.pl", "soundcloud.com", "news.yahoo.com", "photos.google.com", "aliexpress.com", "bit.ly", "steampowered.com", "tinyurl.com", "picasaweb.google.com", "search.google.com", "google.ru", "amazon.co.jp", "foxnews.com", "samsung.com", "amazon.co.uk", "ebay.com", "businessinsider.com", "nasa.gov", "ig.com.br", "aboutads.info", "time.com", "usatoday.com", "cnet.com", "abcnews.go.com", "scribd.com", "myaccount.google.com", "change.org", "get.google.com", "dan.com", "archive.org", "youronlinechoices.com", "dailymail.co.uk", "it.wikipedia.org", "gov.uk", "gravatar.com", "enable-javascript.com", "forms.gle", "cbsnews.com", "google.fr", "marketingplatform.google.com", "mirror.co.uk", "cdc.gov", "namecheap.com", "de.wikipedia.org", "plesk.com", "cpanel.net", "networkadvertising.org", "jimdofree.com", "berkeley.edu", "amazon.fr", "hollywoodreporter.com", "clickbank.net", "biglobe.ne.jp", "quora.com", "target.com", "e-recht24.de", "abc.net.au", "wix.com", "ign.com", "gnu.org", "gizmodo.com", "walmart.com", "bandcamp.com", "m.wikipedia.org", "lemonde.fr", "code.google.com", "weibo.com", "ria.ru", "nypost.com", "addtoany.com", "rottentomatoes.com", "wp.com", "guardian.co.uk", "imageshack.us", "news.com.au", "disqus.com", "loc.gov", "afternic.com", "php.net", "adssettings.google.com", "nginx.org", "washington.edu", "stackoverflow.com", "lg.com", "tmz.com", "storage.googleapis.com", "netflix.com", "shopify.com", "ja.wikipedia.org", "express.co.uk", "addthis.com", "themeforest.net", "mozilla.com", "picasa.google.com", "lefigaro.fr", "usnews.com", "hm.com", "oup.com", "mega.nz", "fb.me", "alibaba.com", "akamaihd.net", "amazon.es", "arxiv.org", "amzn.to", "deezer.com", "google.co.in", "nationalgeographic.com", "ietf.org", "hp.com", "google.co.id", "fda.gov", "secureserver.net", "ibm.com", "pl.wikipedia.org", "whitehouse.gov", "4shared.com", "welt.de", "zoom.us", "techcrunch.com", "newsweek.com", "disney.com", "eventbrite.com", "wikihow.com", "stanford.edu", "economist.com", "netlify.app", "rambler.ru", "smh.com.au", "twitch.tv", "kafebook.ir", "shabestan.ir", "instagram.com"]
        # this variable contain sall punctuation
        punctuation = string.punctuation
        

        # start get inputs and work on links
        # get link name from user
        INPUT_NAME = input(Fore.LIGHTMAGENTA_EX + "\nenter your name site: ")
        while True:
            
            
            if INPUT_NAME == "":
                INPUT_NAME = input(Fore.LIGHTRED_EX + "please enter your name site: ")   
            
            elif INPUT_NAME.isspace():
                INPUT_NAME = input(Fore.LIGHTRED_EX + "please enter your name site: ") 
    
            elif INPUT_NAME.isnumeric():
                INPUT_NAME = input(Fore.LIGHTRED_EX + "please enter your name site: ")
    
            elif INPUT_NAME in punctuation:
                INPUT_NAME = input(Fore.LIGHTRED_EX + "please enter your name site: ")
                
            
            #elif INPUT_NAME in y:
            elif "." in INPUT_NAME:
                INPUT_NAME = input(Fore.LIGHTRED_EX + "your link name must contains just letters and numbers, enter your name site: ")
        
            else:
                break
    
        # start editing user input
        # every alpha become lower case   
        INPUT_NAME = INPUT_NAME.lower()
        # replace space with nothing
        INPUT_NAME = INPUT_NAME.replace(' ', '')
        # replace (site) and (web) words with nothing => delete them
        INPUT_NAME = INPUT_NAME.replace('site', '')
        INPUT_NAME = INPUT_NAME.replace('website', '')
    
    
        if INPUT_NAME in SITES_NAMES:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + "import your link like this: www.name.com => format of site can be anything you want")
            INPUT_LINK = input(Fore.LIGHTMAGENTA_EX + "enter your Link: ")
    
            while True:
                # this variable contain sall punctuation
                punctuation = string.punctuation
                
                print(Style.RESET_ALL)
                if INPUT_LINK == "":
                    print(Fore.YELLOW  + "import your link like this: www.name.com => format of site can be anything you want")
                    INPUT_LINK = input(Fore.LIGHTRED_EX + "please enter your Link: ")
        
                elif INPUT_LINK.isspace():
                    print(Fore.YELLOW  + "import your link like this: www.name.com => format of site can be anything you want")
                    INPUT_LINK = input(Fore.LIGHTRED_EX + "please enter your Link: ")
        
                elif INPUT_LINK.isnumeric():
                    print(Fore.YELLOW  + "import your link like this: www.name.com => format of site can be anything you want")
                    INPUT_LINK = input(Fore.LIGHTRED_EX + "please enter your Link: ")
                
                else:
                    break
    
            INPUT_LINK = INPUT_LINK.lower()
    
    
            # delete www. from links
            if "www." in INPUT_LINK:
                INPUT_CHANGING = INPUT_LINK.replace("www.", "")
                # check link if fake page or not
                if INPUT_CHANGING in SITES_LINKS:
                    print(Fore.GREEN + "this IS NOT FAKE PAGE")
    
                else:
                    print(Back.WHITE + Fore.RED + "this IS FAKE PAGE")
            else:
                if INPUT_LINK in SITES_LINKS:
                    print(Fore.GREEN + "this IS NOT FAKE PAGE")
    
                else:
                    print(Back.WHITE + Fore.RED + "this IS FAKE PAGE")
                
        else:
            print(Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + "we don't support this site, sorry :(")  
                
    if INPUT_DECIDING == 2:
        # START CHECK PASSSWORD PROGRAM
        
        # reset colors of text
        print(Style.RESET_ALL)
        
        # get user input
        INPUT = input(Fore.LIGHTCYAN_EX +"\nenter your password to check: ")
        # get user input again if didn't enter anything
        while True:
            if INPUT == "" or INPUT.isspace():
                INPUT = input(Fore.LIGHTRED_EX + "please enter your password to check: ")
            
            else:
                break
        
        # replace space with nothing = delete space
        INPUT = INPUT.replace(' ', '') 


        # VARIABLES
    
        # each 3 variable contains all letters , digit and punctuation
        letters = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation
    
        # 3 situations
        situation = ["Your Password is 10% Strong", "Your Password is 60% Strong", "Your Password is Completely Strong"]
    
        # chicking if password include letters
        have_letters = 0
        # chicking if password include digit
        have_digits = 0
        # chicking if password include punctuation
        have_punctuation = 0
    
    
        # check how much user password is strong
        for item in INPUT: 
            if item in letters:
                have_letters = 1
    
            elif item in digits:
                have_digits = 1
    
            elif item in punctuation:
                have_punctuation = 1

        print()
        print(Fore.LIGHTYELLOW_EX + situation[have_letters + have_digits + have_punctuation -1])
        print(Fore.YELLOW + "thanks for used our servies :)")
      
    if INPUT_DECIDING == 3:
        # START MAKE PROGRAM
        
        print(Style.RESET_ALL)
        # get user input
        INPUT_CONTAINS = input(Fore.WHITE + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
    
        # check user input for contains
        while True:
            # thsese 2 variabls contains all digits and punctuation
            digits = string.digits
            punctuation = string.punctuation
        
            if INPUT_CONTAINS == "":
                INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
        
            elif INPUT_CONTAINS in digits:
                INPUT_CONTAINS = int(INPUT_CONTAINS)
                if INPUT_CONTAINS == 0:
                    INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
                
                elif INPUT_CONTAINS <= 7:
                    break
            
                else:
                    INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
        
            elif INPUT_CONTAINS in punctuation:
                INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
            
            elif INPUT_CONTAINS.isspace():
                INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
             
            else:
                INPUT_CONTAINS = input(Fore.LIGHTRED_EX + """\nyour password have to include:
1. letters, digits, punctuation
2. letters, digits
3. letters, punctuation
4. digits, punctuation
5. letters
6. digits
7. punctuation

_ import number of a item >> """)
  
        # reset texts color
        print(Style.RESET_ALL)
  
        # VARIABLES
        
        # each 3 variable contains all letters , digit and punctuation
        digits = string.digits
        punctuation = string.punctuation
        letters = string.ascii_letters  
        
        # start making password
        
        # make password with letters and punctuation and digits
        if INPUT_CONTAINS == 1:    
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(4))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password)  
                        break
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "you must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                    
            
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
      
        # password with letters and digits                 
        elif INPUT_CONTAINS == 2: 
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
            
                    
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                                    
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
    
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.digits + string.ascii_letters + string.digits
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                        
            
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")                     
                             
        # password with letters and punctuation   
        elif INPUT_CONTAINS == 3:
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    if INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters + string.punctuation
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
         
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ") 
                                   
                    
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
     
        # password with punctuation and digits     
        elif INPUT_CONTAINS == 4:   
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "your password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "your password : ", password)
                        break
        
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "your password : ", password)
                        break
                
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.ascii_letters + string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "your password : ", password)
                        break     
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "your password : ", password)
                        break
    
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "your password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.punctuation + string.digits
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "your password : ", password)
                        break
        
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "you must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                    
                    
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
     
        # password with letters      
        elif INPUT_CONTAINS == 5:  
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
    
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.ascii_letters
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
           
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                                
                    
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
     
        # password with digit    
        elif INPUT_CONTAINS == 6:
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                       
                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password) 
                        break
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
    
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.digits
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ") 
                                   
            
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")                     
                    
        # password with punctuation    
        elif INPUT_CONTAINS == 7:
            # get user input
            INPUT_formaking = input(Fore.CYAN + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            while True:
                # check user input
            
                if INPUT_formaking == "":
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in digits or INPUT_formaking in ("4", "5", "6", "8", "10", "15", "20"):
                    INPUT_formaking = int(INPUT_formaking)
                    if INPUT_formaking == 4:
                        # make password with 4 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(4, 4)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
                    
                    elif INPUT_formaking == 5:
                        # make password with 5 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(5, 5)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break

                    elif INPUT_formaking == 6:
                        # make password with 6 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(6, 6)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
            
                    elif INPUT_formaking == 8:
                        # make password with 8 char
                        char = string.punctuation
                        password = "".join(choice(char) for x in range(randint(8, 8)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
            
                    elif INPUT_formaking == 10:
                        # make password with 10 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(10, 10)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
    
                    elif INPUT_formaking == 15:
                        # make password with more than 10 char less than 17 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(15, 15)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break
        
                    elif INPUT_formaking == 20:
                        # make password with more than 10 char less than 17 char
                        contains = string.punctuation
                        password = "".join(choice(contains) for x in range(randint(20, 20)))
                        print(Fore.GREEN + "\nYour Password : ", password)
                        break

                    else:
                        print(Fore.YELLOW + "\nyou have to choose one of these number")
                        INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                               
            
                elif INPUT_formaking in letters:
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking in punctuation:  
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")  
                
                elif INPUT_formaking.isspace():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
                
                elif INPUT_formaking.isalpha():
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "\nyou must import A NUMBER\nhow long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")
            
                else:
                    print(Fore.YELLOW + "\nyou have to choose one of these number")
                    INPUT_formaking = input(Fore.LIGHTRED_EX + "how long your password have to be(4, 5, 6, 8, 10, 15, 20)? ")            
                    
        # last talk with user   
        last_talk = "\nNOTICE, we didn't ask you if there is a specific\ncharacter, number or symbol that you would like\nto have in your password or not? if we did, your\npassword would be guessable."
        print(Fore.YELLOW + last_talk)
        
        # we have another way to make password for user with for loop :)            
        
        
# DONE, THANKS GOD