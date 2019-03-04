import sqlite3
import datetime

conn = sqlite3.connect('newDB3.db')
c = conn.cursor()

c.execute(""" CREATE TABLE `Food` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL  ,`price` INTEGER,`size`	TEXT, `path` TEXT) """)
c.execute(""" CREATE TABLE `Optional` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL UNIQUE ) """)
c.execute(""" CREATE TABLE `Orders` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `time` NUMERIC NOT NULL ) """)
c.execute(""" CREATE TABLE "DetailOrder" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `orderID` INTEGER NOT NULL, `foodID` INTEGER NOT NULL, FOREIGN KEY(`foodID`) REFERENCES `Food`(`id`), FOREIGN KEY(`orderID`) REFERENCES `Orders`(`id`)) """)
c.execute("""CREATE TABLE `Detailorder_option` (`id`	INTEGER PRIMARY KEY AUTOINCREMENT,`orderDetailID`	INTEGER,`optionalID`	INTEGER,FOREIGN KEY(`orderDetailID`) REFERENCES `DetailOrder`(`id`));""")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Espresso',40,'M','./image/hot/Hot_Espresso.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Cappuccino',45,'M','./image/hot/Hot_Cappuccino.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Latte',45,'M','./image/hot/Hot_Latte.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Mocha',50,'M','./image/hot/Hot_Mocha.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Tea',30,'M','./image/hot/Hot_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Green_Tea_with_Milk',35,'M','./image/hot/Hot_Green_Tea_with_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Milk_Tea',35,'M','./image/hot/Hot_Milk_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Dark_chocolate',40,'M','./image/hot/Hot_Dark_chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Fresh_Milk',30,'M','./image/hot/Hot_Fresh_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Hot_Chocolate',35,'M','./image/hot/Hot_Chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Espresso',45,'M','./image/ice/Ice_Espresso.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Cappuccino',50,'M','./image/ice/Ice_Cappuccino.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Latte',50,'M','./image/ice/Ice_Latte.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Mocha',55,'M','./image/ice/Ice_Mocha.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Honey_Black_Coffee',60,'M','./image/ice/Ice_Honey_Black_Coffee.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Honey_Black_Coffee_Lemon',60,'M','./image/ice/Ice_Honey_Black_Coffee_Lemon.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Green_Tea_with_Milk',40,'M','./image/ice/Ice_Green_Tea_with_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Milk_Tea',40,'M','./image/ice/Ice_Milk_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Lemonade_Tea',40,'M','./image/ice/Ice_Lemonade_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Black_Tea',40,'M','./image/ice/Ice_Black_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Matcha_Honey',55,'M','./image/ice/Ice_Matcha_Honey.GIF')") 
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Dark_chocolate',45,'M','./image/ice/Ice_Dark_chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Fresh_Milk',35,'M','./image/ice/Ice_Fresh_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Chocolate',40,'M','./image/ice/Ice_Chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Lynchee_Juice',40,'M','./image/ice/Ice_Lynchee_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Strawberry_juice',40,'M','./image/ice/Ice_Strawberry_juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Kiwi_Juice',40,'M','./image/ice/Ice_Kiwi_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Espresso',50,'M','./image/frappe/Frappe_Espresso.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Cappuccino',55,'M','./image/frappe/Frappe_Cappuccino.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Latte',55,'M','./image/frappe/Frappe_Latte.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Mocha',60,'M','./image/frappe/Frappe_Mocha.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Green_Tea_with_Milk',45,'M','./image/frappe/Frappe_Green_Tea_with_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Milk_Tea',45,'M','./image/frappe/Frappe_Milk_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Dark_chocolate',55,'M','./image/frappe/Frappe_Dark_chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Fresh_Milk',45,'M','./image/frappe/Frappe_Fresh_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Chocolate',50,'M','./image/frappe/Frappe_Chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Lynchee_Juice',45,'M','./image/frappe/Frappe_Lynchee_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Strawberry_juice',45,'M','./image/frappe/Frappe_Strawberry_juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Kiwi_Juice',45,'M','./image/frappe/Frappe_Kiwi_Juice.GIF')")

c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Espresso',50,'L','./image/ice/Ice_Espresso.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Cappuccino',55,'L','./image/ice/Ice_Cappuccino.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Latte',55,'L','./image/ice/Ice_Latte.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Mocha',60,'L','./image/ice/Ice_Mocha.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Honey_Black_Coffee',65,'L','./image/ice/Ice_Honey_Black_Coffee.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Honey_Black_Coffee_Lemon',65,'L','./image/ice/Ice_Honey_Black_Coffee_Lemon.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Green_Tea_with_Milk',45,'L','./image/ice/Ice_Green_Tea_with_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Milk_Tea',45,'L','./image/ice/Ice_Milk_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Lemonade_Tea',45,'L','./image/ice/Ice_Lemonade_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Black_Tea',45,'L','./image/ice/Ice_Black_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Matcha_Honey',60,'L','./image/ice/Ice_Matcha_Honey.GIF')") 
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Dark_chocolate',50,'L','./image/ice/Ice_Dark_chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Fresh_Milk',40,'L','./image/ice/Ice_Fresh_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Chocolate',45,'L','./image/ice/Ice_Chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Lynchee_Juice',45,'L','./image/ice/Ice_Lynchee_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Strawberry_juice',45,'L','./image/ice/Ice_Strawberry_juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Ice_Kiwi_Juice',45,'L','./image/ice/Ice_Kiwi_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Espresso',55,'L','./image/frappe/Frappe_Espresso.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Cappuccino',60,'L','./image/frappe/Frappe_Cappuccino.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Latte',60,'L','./image/frappe/Frappe_Latte.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Mocha',65,'L','./image/frappe/Frappe_Mocha.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Green_Tea_with_Milk',50,'L','./image/frappe/Frappe_Green_Tea_with_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Milk_Tea',50,'L','./image/frappe/Frappe_Milk_Tea.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Dark_chocolate',60,'L','./image/frappe/Frappe_Dark_chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Fresh_Milk',50,'L','./image/frappe/Frappe_Fresh_Milk.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Chocolate',55,'L','./image/frappe/Frappe_Chocolate.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Lynchee_Juice',50,'L','./image/frappe/Frappe_Lynchee_Juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Strawberry_juice',50,'L','./image/frappe/Frappe_Strawberry_juice.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Frappe_Kiwi_Juice',50,'L','./image/frappe/Frappe_Kiwi_Juice.GIF')")

c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Cookie',60,'N','./image/etc/Cookie.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Brownies',60,'N','./image/etc/Brownies.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Cake',45,'N','./image/etc/Cake.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Croissant',25,'N','./image/etc/Croissant.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('hotdog',80,'N','./image/etc/hotdog.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('Toast',35,'N','./image/etc/Toast.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('honey-toast',25,'N','./image/etc/honey.GIF')")
c.execute("INSERT INTO Food (name, price, size, path) VALUES ('hamburger',20,'N','./image/etc/hamburger.GIF')")


c.execute("INSERT INTO Optional (name) VALUES ('Normal')")
c.execute("INSERT INTO Optional (name) VALUES ('No_Sugar')")
c.execute("INSERT INTO Optional (name) VALUES ('Low_Sugar')")
c.execute("INSERT INTO Optional (name) VALUES ('Add_Sugar')")
c.execute("INSERT INTO Optional (name) VALUES ('No_Milk')")
c.execute("INSERT INTO Optional (name) VALUES ('Low_Milk')")
c.execute("INSERT INTO Optional (name) VALUES ('Add_Milk')")
c.execute("INSERT INTO Optional (name) VALUES ('ฺNo_Cream')")
c.execute("INSERT INTO Optional (name) VALUES ('Low_Cream')")
c.execute("INSERT INTO Optional (name) VALUES ('Add_Cream')")
c.execute("INSERT INTO Optional (name) VALUES ('Whip_Cream')")

conn.commit()