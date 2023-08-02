#python to be installed in the system
#the below mentioned libraries should pe installed before running the program: scrapy, newspaper, spacy
#enter "cd news" in the terminal to access the project
#run the command "scrapy crawl Compile" in the terminal to run the script
#delete the .txt files before running the script if previous data is not required
import scrapy
from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
            nlp = spacy.load("en_core_web_sm")
            doc= nlp(text)
            tokens=[token.text for token in doc]
            word_frequencies={}
            for word in doc:
                if word.text.lower() not in list(STOP_WORDS):
                    if word.text.lower() not in punctuation:
                        if word.text not in word_frequencies.keys():
                            word_frequencies[word.text] = 1
                        else:
                            word_frequencies[word.text] += 1
            max_frequency=max(word_frequencies.values())
            for word in word_frequencies.keys():
                word_frequencies[word]=word_frequencies[word]/max_frequency
            sentence_tokens= [sent for sent in doc.sents]
            sentence_scores = {}
            for sent in sentence_tokens:
                for word in sent:
                    if word.text.lower() in word_frequencies.keys():
                        if sent not in sentence_scores.keys():                            
                            sentence_scores[sent]=word_frequencies[word.text.lower()]
                        else:
                            sentence_scores[sent]+=word_frequencies[word.text.lower()]
            select_length=int(len(sentence_tokens)*per)
            summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
            final_summary=[word.text for word in summary]
            summary=''.join(final_summary)
            return summary


class CompileLSpider(scrapy.Spider):
    name = "Compile"
    
    #def start_requests(self):
    #    links= ['https://www.moneycontrol.com/news/business/', 'https://www.moneycontrol.com/news/business/economy/','https://www.livemint.com/latest-news','https://www.livemint.com/market','https://www.business-standard.com/economy-policy','https://www.business-standard.com/finance','https://www.thehindubusinessline.com/']
        
    """ for i in links:
            if "money" in i:
                yield scrapy.Request(url=i, callback=self.parse)
            if "mint" in i:
                yield scrapy.Request(url=i, callback=self.mint)
            if "business-standard" in i:
                yield scrapy.Request(url=i, callback=self.busn) """
            
    start_url = ["https://www.sec.gov/Archives/edgar/data/884394/000095013500005227/b37488ssn-30d.txt"]            

    def parse(self,response):
        
                """ site_links = []
                site_headings = []
                for site in response.xpath('//*[@id="cagetory"]'):
                    site_links = site.xpath('//*[@class="clearfix"]/h2/a/@href').extract()
                    site_links.append(site_links)
                    site_headings = site.xpath('//*[@class="clearfix"]/h2/a/text()').extract()
                    site_headings.append(site_headings)
            #print("Links= ",site_links)
                sl = list(site_links)
                sl.remove(sl[-1])
            #print(sl)
                sh = list(site_headings)
                sh.remove(sh[-1])
                #print(sh)
                print("links= ",len(site_links))
                print("headings= ",len(site_headings))

                for i in range(len(sl)):            
                    article = Article(sl[i])
                    article.download()
                    article.parse()
                    print(sh[i])
                    print(summarize(article.text,0.75))
                    print("\n\n\n")
                    with open("MoneyControl.txt", 'a+' ) as txtfile:
                        txtfile.write(sh[i])
                        txtfile.write(summarize(article.text,0.75))
                        txtfile.write("\n\n\n")
    def mint(self,response):
                        site_links = []
                        site_headings = []
                        for site in response.xpath('//*[@class="mainSec"]'):
                            site_links = site.xpath('//*[@class="headline"]/a/@href').extract()
                            site_links.append(site_links)
                            
                            site_headings = site.xpath('//*[@class="headline"]/a/text()').extract()
                            site_headings.append(site_headings)
                            sl = list(site_links)
                            sl.remove(sl[-1])
                        #print(sl)
                            sh = list(site_headings)
                            sh.remove(sh[-1])
                            #print(sh)
                            print("links= ",len(site_links))
                            print("headings= ",len(site_headings))

                        for i in range(len(sl)):          
                                    article = Article("https://www.livemint.com" + sl[i])
                                    article.download()
                                    article.parse()
                                    print(sh[i])
                                    print(summarize(article.text,0.75))
                                    print("\n\n\n")
                                    with open("LiveMint.txt", 'a+' ) as txtfile:
                                        txtfile.write(sh[i])
                                        txtfile.write(article.text)
                                        txtfile.write("\n\n\n")
    def busn(self,response):
                        site_links = []
                        site_headings = []
                        for site in response.xpath('//*[@class="row-panel"]'):
                                site_links = site.xpath('//*[@id="bs-new-top-story-listing-ajax-block"]/div/h2/a/@href').extract()
                                site_links.append(site_links)
                                
                                site_headings = site.xpath('//*[@id="bs-new-top-story-listing-ajax-block"]/div/h2/a/text()').extract()
                                site_headings.append(site_headings)
                        sl = list(site_links)
                        sl.remove(sl[-1])
                        #print(sl)
                        sh = list(site_headings)
                        sh.remove(sh[-1])
                        #print(sh)
                        print("links= ",len(site_links))
                        print("headings= ",len(site_headings))

                        for i in range(len(sl)):          
                                    article = Article("https://www.business-standard.com/" + sl[i])
                                    article.download()
                                    article.parse()
                                    print(sh[i])
                                    print(summarize(article.text,0.75))
                                    print("\n\n\n")
                                    with open("BusinessStandard.txt", 'a+' ) as txtfile:
                                        txtfile.write(sh[i])
                                        txtfile.write(summarize(article.text,0.75))
                                        txtfile.write("\n\n\n")
  """