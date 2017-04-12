from lxml import html
import requests
import winsound
import time
from Mail_module import Mail_module

THREADHOLD = 70 # show item only price decrease THREADHOLD%
STOP = 15 # Lower bound to search for watchlist item
IGNORE_LIST = "rag_ignore_list.txt"
WATCH_LIST = "rag_watch_list.txt"
MAIL_SERVER = 'smtp.gmail.com:587'
REFRESH_TIME = 7200 # report list item refresh rate in second, 2H
CLEAN_COUNTER = 12 

def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

class item:
    def __init__(self, name, price, discount, time ):
        self.name = name
        self.price = price
        self.discount = discount
        self.time = time
        

class Rag_crawler:
    def __init__(self, report, stop):
        self.report = report
        self.stop = stop
        self.mm = None
        self.report_list = {} # list of item object that already reported to recipient
        
        with open(WATCH_LIST) as f:
            self.watch_list = f.readlines()
        self.watch_list = [x.strip() for x in self.watch_list]

        with open(IGNORE_LIST) as f:
            self.ignore_list = f.readlines()
        self.ignore_list = [x.strip() for x in self.ignore_list]

    def init_mail_module( self, username, pw, to_addr ):
        self.mm = Mail_module( username, pw, MAIL_SERVER )
        self.mm.set_from( "RAG Crawler Bot")
        self.mm.to_addr = to_addr

    def get_rag(self):
        base_url = 'http://ragi.al/cheap/iRO-Renewal'
        count = 0
        page = requests.get(base_url+'/'+str(count))
        tree = html.fromstring(page.content)
        discount = self.stop  + 1
        msg = ""
        report = False

        while ( discount > self.stop ):
            count = count + 1
            page = requests.get(base_url+'/'+str(count))
            tree = html.fromstring(page.content)
            
            for table in tree.xpath('//div[@class="ilist"]/table'):
                data = [[text(td) for td in tr.xpath('td')] for tr in table.xpath('//tr')]
                for i in range (1, len(data)):
                    item_name = data[i][0].lstrip()
                    item_price = data[i][2].replace('z', '')
                    discount = int(data[i][3].replace('-','').replace('%', ''))

                    if ( item_name in self.ignore_list ):
                        continue
                    
                    if ( discount >= self.report or (item_name in self.watch_list)):
                        if ( item_name in self.report_list ):
                            # Possibly already report this item
                            if ( self.report_list[item_name].discount > discount ):
                                self.report_list[item_name].discount = discount
                                self.report_list[item_name].time = time.time()
                                #print("Found lower price for %s" %(item_name))
                                msg = msg + "%s, %s, %d\n" %(item_name, item_price, discount)
                                report = True
                            else:
                                #print("Already reported (%s)" %(item_name))
                                continue
                        else: # not in list
                            #print("inserting %s into list" %(item_name))
                            self.report_list[item_name] = item(item_name, item_price, discount, time.time())
                            msg = msg + "%s, %s, %d\n" %(item_name, item_price, discount)
                            report = True
                            
        if ( report ):
            self.mm.sendmail(self.mm.to_addr, "Rag Discount Item", msg)
            print("mail content: \n%s" %(msg))
        else :
            print("Did not found anything new")
            
    def clean_report_list( self ):
        print("Running clean_report_list")
        now = time.time()
        key_list = list(self.report_list.keys())
        for k in key_list:
            if ( REFRESH_TIME < int(now - self.report_list[k].time) ):
                del self.report_list[k]
                


if __name__ == "__main__":
    clean_counter = CLEAN_COUNTER
    username = input("Enter bot mail username: ")
    pw = input("Enter pw: ")
    to_addr = input("Enter recipient email addr: ")
    rc = Rag_crawler( THREADHOLD, STOP )
    rc.init_mail_module( username, pw, to_addr )
    while True:
        rc.get_rag()
        clean_counter = clean_counter - 1
        if ( clean_counter <= 0 ):
            clean_counter = CLEAN_COUNTER
            rc.clean_report_list()
        time.sleep(10)
