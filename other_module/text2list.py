from pythainlp.tokenize import word_tokenize,dict_word_tokenize,dict_trie
from pythainlp.tag import pos_tag
from pythainlp.corpus import wordnet

import csv
import re

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
        self.keyword = [item for item in self.menus]
        self.keyword.append("วิป")
        self.keyword.append("วิปครีม")
        self.keyword_dict=dict_trie(self.keyword)
        with open("other_module/normwords.csv",encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.normwords.append(row)
        #print(self.normwords)

    def text_to_item(self,raw_text):
        res = {}
        text=self.replace_word(raw_text)
        words=dict_word_tokenize(text,self.keyword_dict)
        new_w=[]
        for w in words:
            if w in self.keyword:
                new_w.append(w)
            else:
                word=word_tokenize(w)
                [new_w.append(i) for i in word]
        words = new_w
        # print(words)
        items = self.split_item(words)
        items_translated = []
        for item in items:
            i1 = self.translate1(item)
            # i2 = self.translate2(item)
            # if i1 != i2:
                # print(raw_text)
                # print(i1)
                # print(i2)
            items_translated.append(i1)
            #items_translated.append(self.translate2(item))
        if (items == []) :
            res["status"] = "fail to processing \"{}\".".format(raw_text)
        else:
            res["status"] = "process word \"{}\" complete.".format(raw_text)
        res["item"] = items_translated
        return res
        
    def replace_word(self,text):
        for word in self.normwords:
            for w in word[1:]:
                w.lower()
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
        
    def translate2(self,item):
        text = "".join(item)
        text = text.replace("ๆ","")
        regex = r"(menu)(ร้อน|เย็น|ปั่น)?\s*(แก้วใหญ่)?\s*((ไม่|ไม่ใส่)?(หวาน(น้อย|ปกติ|กลาง|มาก)?|น้ำตาล(เยอะ|น้อย|นิดหน่อย|อ่อน)?)|((ไม่)?(ใส่นมข้น|ใส่นม))|((ไม่)?(เพิ่ม|ใส่)(วิปครีม|วิป)))*(\d+)?"
        menu = "|".join(reversed(self.menus))
        regex = regex.replace("menu",menu)
        matches = re.finditer(regex, text)
        
        for matchNum, match in enumerate(matches, start=1):          
            #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1              
                # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                
                name = self.lang_convert_th_eng[match.group(1)]
                qty = int(match.group(16)) if match.group(16) != None else 1
                size = "L" if match.group(3) != None else "M"
                type = self.lang_convert_th_eng[match.group(2)] if match.group(2) != None else "Ice"
                sugar = None
                milk = None
                whip_cream = None
                optional = []
                if match.group(6) != None:
                    if match.group(5) != None:
                        sugar="No_Sugar"
                    elif match.group(7) in ["น้อย"] or match.group(8) in ["น้อย","นิดหน่อย","อ่อน"]:
                        sugar="Low_Sugar"
                    elif match.group(7) in ["มาก"] or match.group(8) in ["เยอะ"]:
                        sugar="Extra_Sugar"
                    elif match.group(6) == "หวาน":
                        sugar="Extra_Sugar"
                if match.group(9) != None:
                    if match.group(10) != None:
                        milk="No_Milk"
                    else:   
                        milk="Extra_Milk"
                if match.group(12) != None:
                    if match.group(13) == None:
                        whip_cream="Extra_Whipped_Cream"
        if sugar is not None:
            optional.append(sugar)
        if milk is not None:
            optional.append(milk)
        if whip_cream is not None:
            optional.append(whip_cream)
        if name in ["Cookie","Brownies","Cake","Croissant","Hotdog","Toast","Honey-Toast","Hamburger"]:
            return([name,qty,[],"N"])                 
        return([type+"_"+name,qty,optional,size]) 
        
    def translate1(self,item):
        name = self.lang_convert_th_eng[item[0]]
        qty = 1
        size,type = "M","Ice"
        sugar = None
        milk = None
        whip_cream = None
        optional = []
        neg = 0
        sweet_state = 0
        milk_state = 0
        for word in item :
            if (word in ["ร้อน","เย็น","ปั่น"]) :
                type = self.lang_convert_th_eng[word]
            elif (word in ["ใหญ่",'L']) :
                size = "L"
            elif (word in ["ไม่"]):
                neg = 1
            elif (word in ["น้ำตาล","หวาน"]):
                milk_state = 0
                if neg :
                    sugar = 'No_Sugar'
                    neg = 0
                else:
                    sweet_state = 1 
                    sugar = 'Extra_Sugar'
            elif (word in ["นม","นมข้น"]):
                sweet_state = 0
                if neg :
                    milk = 'No_Milk'
                    neg = 0
                else:
                    milk_state = 1
                    milk = 'Extra_Milk'
            elif (word in ["วิป","วิปครีม","ครีม"]):
                milk_state = 0
                sweet_state = 0
                if neg :
                    neg = 0
                else:
                    whip_cream = 'Extra_Whipped_Cream'
            elif (word in ["ปกติ","กลาง","ปานกลาง"]):
                if sweet_state == 1: 
                    sugar = None
                    sweet_state = 0
                elif milk_state == 1: 
                    milk = None
                    milk_state = 0
            elif (word in ["น้อย","อ่อน"]):
                if sweet_state == 1: 
                    sugar = 'Low_Sugar'
                    sweet_state = 0
                elif milk_state == 1: 
                    milk = 'Low_Milk'
                    milk_state = 0
            elif word.isdigit():
                qty = int(word)
        if sugar is not None:
            optional.append(sugar)
        if milk is not None:
            optional.append(milk)
        if whip_cream is not None:
            optional.append(whip_cream)
        if name in ["Cookie","Brownies","Cake","Croissant","Hotdog","Toast","Honey-Toast","Hamburger"]:
            return([name,qty,[],"N"])  
        if name in ["Tea"]:
            type = "Hot"
        if name in ["Honey_Black_Coffee","Honey_Black_Coffee_Lemon","Lemonade_Tea","Black_Tea","Matcha_Honey"]:
            type = "Ice"
        if name in ["Lynchee_Juice","Strawberry_juice","Kiwi_Juice"] and type == "Hot":
            type = "Ice"
        if type == "Hot":
            size = "M"
        return([type+"_"+name,qty,optional,size])        
        
        