from pythainlp.tokenize import word_tokenize,dict_word_tokenize,create_custom_dict_trie
from pythainlp.tag import pos_tag
import csv

class CoffeeShopNLP:
    def __init__(self):
        self.menus = []
        #self.menu = {}
        self.normwords = []
        self.lang_convert_th_eng = { 
            "ร้อน" : "Hot",
            "เย็น" : "Ice",
            "ปั่น" : "Frappe",
        }
        with open("other_module/menu.csv",encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.lang_convert_th_eng[row[0]] = row[1]
                #self.menu.append([row[0],row[1]])
                self.menus.append(row[0])
        self.menu_dict=create_custom_dict_trie(self.menus)
        with open("other_module/normwords.csv",encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.normwords.append(row)
        #print(self.normwords)

    def text_to_item(self,text):
        res = {}
        text=self.replace_word(text)
        words=dict_word_tokenize(text,self.menu_dict)
        new_w=[]
        for w in words:
            if w in self.menus:
                new_w.append(w)
            else:
                word=word_tokenize(w)
                [new_w.append(i) for i in word]
        words = new_w
        #print(words)
        items = self.split_item(words)
        #print(items)
        item_formated = []
        for item in items:
            item_formated.append(self.to_format(item))
        if (items == []) :
            res["status"] = "Fail to process word \"{}\".".format(text)
        else:
            res["status"] = "Process word \"{}\" complete.".format(text)
        res["item"] = item_formated
        return res
        
    def replace_word(self,text):
        for word in self.normwords:
            for w in word[1:]:
                text=text.replace(w, word[0])
        return(text)
        
        
    def split_item(self,word_tokenizes):
        split_index = []
        res = [] 
        for id, word in enumerate(word_tokenizes):
            if word in self.menus:
                split_index.append(id)
        split_index.append(len(word_tokenizes))
        for i in range(len(split_index)-1):
            res.append(word_tokenizes[split_index[i]:split_index[i+1]])
        return res
        
    def to_format(self,item):
        name = self.lang_convert_th_eng[item[0]]
        qty = 1
        size,type = "M","Ice"
        sugar = None
        optional = []
        neg = 0
        sweet_state = 0
        for word in item :
            if (word in ["ร้อน","เย็น","ปั่น"]) :
                type = self.lang_convert_th_eng[word]
            elif (word in ["ใหญ่"]) :
                size = "L"
            elif (word in ["ไม่"]):
                neg = 1
            elif (word in ["น้ำตาล","หวาน"]):
                if neg :
                    sugar = 'No_Sugar'
                    neg = 0
                else :
                    sugar = 'Add_Sugar'
                    sweet_state = 1
            elif (word in ["น้อย"]):
                sugar = 'LowSugar'
            elif word.isdigit():
                qty = word
        if sugar is not None:
            optional.append(sugar)
        if name in ["Cookie","Brownies","Cake","Croissant","Hotdog","Toast","Honey-Toast","Hamburger"]:
            return([name,qty,[],"N"])
        return([type+"_"+name,qty,optional,size])   
             
        
        