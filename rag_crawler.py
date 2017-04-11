from lxml import html
import requests

THREADHOLD = 80 # show item only price decrease THREADHOLD%
STOP = 15
IGNORE_LIST = "rag_ignore_list.txt"
WATCH_LIST = "rag_watch_list.txt"

def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')


class Rag_crawler:
    def __init__(self, report, stop):
        self.report = report
        self.stop = stop
        
        with open(WATCH_LIST) as f:
            self.watch_list = f.readlines()
        self.watch_list = [x.strip() for x in self.watch_list]

        with open(IGNORE_LIST) as f:
            self.ignore_list = f.readlines()
        self.ignore_list = [x.strip() for x in self.ignore_list]


    def get_rag(self):
        base_url = 'http://ragi.al/cheap/iRO-Renewal'
        count = 0
        page = requests.get(base_url+'/'+str(count))
        tree = html.fromstring(page.content)
        discount = self.stop  + 1

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
                    
                    if ( discount >= self.report ):
                        print("REPORT!! %s, %s, %d" %(item_name, item_price, discount))
                    else:
                        print ("%s, %s, %d" %(item_name, item_price, discount))

                    if ( item_name in self.watch_list ):
                        print("Found (%s) in watch list, REPORT!!" %(item_name))


if __name__ == "__main__":
    rc = Rag_crawler( THREADHOLD, STOP )
    rc.get_rag()
