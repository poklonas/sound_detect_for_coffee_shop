#from pythainlp.tokenize import word_tokenize,dict_word_tokenize,create_custom_dict_trie
from pythainlp.tag import pos_tag
from pythainlp.tokenize import *
import csv

class CoffeeShopNLP:
    def __init__(self):
        self.menus = []
        with open("menu.csv",encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.menus.append(row[0])
        self.menu_dict=create_custom_dict_trie(self.menus)

    def text_to_item(self,text):
        words=dict_word_tokenize(text,self.menu_dict)
        res,item = [],['',1]
        for word in words :
            if word.isdigit() and item[0]!='':
                item[1] = int(word)
            else:
                for menu in self.menus :
                    if word == menu:
                        if item[0]=='':
                            item[0]=menu
                        else:
                            res.append(item)
                            item=[menu,1]
        if not item[0] == '': res.append(item)
        return res
