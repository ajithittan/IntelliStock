from lxml import html
import configparser
import requests
import ast

class retrievedatafromweb:

    def retrievedatafromweb_legacy (self,inpSiteInd,inpDataType):
        page = requests.get('https://finance.yahoo.com/quote/CL=F?p=CL=F')
        tree = html.fromstring(page.content)
        print("Last Price - " ,tree.xpath('//td[@data-test="LAST_PRICE-value"]/span/text()'))
        print("Day's range - " ,tree.xpath('//td[@data-test="DAYS_RANGE-value"]/text()'))
        print("Ask Price - " ,tree.xpath('//td[@data-test="ASK-value"]/span/text()'))
        print("Bid Price - " ,tree.xpath('//td[@data-test="BID-value"]/span/text()'))
        return

    def retDatafromWeb(self,inpQuoteFor,inpStk):
        urldef = ""
        listofItems = []
        urldef = self.retURLParam(inpQuoteFor)
        listofItems = self.retDataToRun(inpQuoteFor)

        urldef = self.retURLParam(inpQuoteFor)
        urldef = urldef.replace("XXXX",eachdata)
        page = requests.get(urldef)
        tree = html.fromstring(page.content)
        print(eachdata)
        print("Last Price - " ,tree.xpath('//td[@data-test="ASK-value"]/span/text()'))
        print("Day's range - " ,tree.xpath('//td[@data-test="DAYS_RANGE-value"]/text()'))
        print("Ask Price - " ,tree.xpath('//td[@data-test="ASK-value"]/span/text()'))
        print("Bid Price - " ,tree.xpath('//td[@data-test="BID-value"]/span/text()'))

        return

    def retDataToRun (self,inpQuoteFor):
        list_of_items = []
        config = configparser.ConfigParser()
        config.read("configitems.ini")
        if inpQuoteFor == "HIST" or inpQuoteFor == "CURRENT":
            list_of_items = ast.literal_eval(config.get("STOCK_QTS", "STK_ITEMS"))
            print(list_of_items)
        return list_of_items

    def retURLParam (self,inpQuoteFor):
        urlParam = ""
        config = configparser.ConfigParser()
        config.read("configitems.ini")
        if inpQuoteFor == "HIST":
            urlParam = config.get('URL','YH_STK_HIST_QT')
        elif inpQuoteFor == "CURRENT":
            urlParam = config.get('URL','YH_STK_CURR_QT')
        else:
            print("Not a valid param")
        return urlParam

#objretdata = retrievedatafromweb()
#objretdata.retDatafromWeb("CURRENT")
