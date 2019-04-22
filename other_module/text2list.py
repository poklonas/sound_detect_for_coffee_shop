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
        self.word_filter = ["ร้อน","เย็น","ปั่น","แก้ว","ใหญ่","หวาน","น้ำตาล","นม","นมข้น","วิปครีม","วิป","ไม่","ใส่","น้อย","ปกติ","กลาง","มาก","เยอะ","เพิ่ม"]
        with open("other_module/menu.csv",encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.lang_convert_th_eng[row[0]] = row[1]
                #self.menu.append([row[0],row[1]])
                self.menus.append(row[0])
        self.keyword = [item for item in self.menus if item != "ชา"]
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
        items_translated_2 = self.translate2(words)
        # items = self.split_item(words)
        # items_translated_1 = []
        # for item in items:
        #     item = self.translate1(item)
        #     items_translated_1.append(item)
        # if items_translated_2 != items_translated_1:
        #     print(raw_text)
        #     print(items_translated_1)
        #     print(items_translated_2)
        if (items_translated_2 == []) :
            res["status"] = "fail to processing \"{}\".".format(raw_text)
        else:
            res["status"] = "process word \"{}\" complete.".format(raw_text)
        res["item"] = items_translated_2
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
        res = []
        item = [word for word in item if word in self.word_filter or word in self.menus or word.isdigit()]
        text = "".join(item)
        regex = r"(?P<menu>menus)(?P<type>ร้อน|เย็น|ปั่น)?(?P<size>แก้วใหญ่)?((?P<sweetnon>ไม่หวาน|ไม่ใส่น้ำตาล)|(?P<sweet>น้ำตาล|หวาน)(?P<sweetlevel>น้อย|ปกติ|ปานกลาง|กลาง|มาก|เยอะ)?|(?P<milknon>ไม่ใส่นม|ไม่ใส่นมข้น|ไม่นม|ไม่นมข้น)|(?P<milk>ใส่นมข้น|ใส่นม|นมข้น)(?P<milklevel>(น้อย|ปกติ|ปานกลาง|กลาง|มาก|เยอะ)?)|(?P<whipcream>ใส่วิปครีม|ใส่วิป|เพิ่มวิปครีม|เพิ่มวิป)|(?P<qty>\d+))*"
        menu = "|".join(reversed(self.menus))
        regex = regex.replace("menus",menu)
        matches = re.finditer(regex, text)
        for match in matches:
            name = self.lang_convert_th_eng[match.group("menu")]
            qty = int(match.group("qty")) if match.group("qty") != None else 1
            size = "L" if match.group("size") != None else "M"
            type = self.lang_convert_th_eng[match.group("type")] if match.group("type") != None else "Ice"
            sugar = None
            milk = None
            whip_cream = None
            optional = []
            if match.group("sweetnon")!=None:
                sugar="No_Sugar"
            elif match.group("sweet")!=None:
                sugar="Extra_Sugar"
                if match.group("sweetlevel") in ["น้อย"]:
                    sugar="Low_Sugar"
                elif match.group("sweetlevel") in ["ปกติ","ปานกลาง","กลาง"]:
                    sugar=None
            if match.group("milknon")!=None:
                milk="No_Milk"
            elif match.group("milk")!=None:
                milk="Extra_Milk"
                if match.group("milklevel") in ["น้อย"]:
                    milk="Low_Milk"
                elif match.group("milklevel") in ["ปกติ","ปานกลาง","กลาง"]:
                    milk=None   
            if match.group("whipcream")!=None:
                whip_cream="Extra_Whipped_Cream"
            if sugar is not None:
                optional.append(sugar)
            if milk is not None:
                optional.append(milk)
            if whip_cream is not None:
                optional.append(whip_cream)
            if name in ["Tea"]:
                type = "Hot"
            if name in ["Honey_Black_Coffee","Honey_Black_Coffee_Lemon","Lemonade_Tea","Black_Tea","Matcha_Honey"]:
                type = "Ice"
            if name in ["Lynchee_Juice","Strawberry_juice","Kiwi_Juice"] and type == "Hot":
                type = "Ice"
            if type == "Hot":
                size = "M"
            if name in ["Cookie","Brownies","Cake","Croissant","Hotdog","Toast","Honey-Toast","Hamburger"]:
                res.append([name,qty,[],"N"])                 
            else: 
                res.append([type+"_"+name,qty,optional,size])
        return res     
        
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
        
        