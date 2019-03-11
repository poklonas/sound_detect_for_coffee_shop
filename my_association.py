import associate.fpgrowth as orange_asso
import Orange as orange
#from Orange.data import Domain, DiscreteVariable, ContinuousVariable
#mport numpy as np
#import pandas as pd
import pickle 
import sqlite3

def update_rule(dbfile, target):
    conn = sqlite3.connect(dbfile)
    query = """ SELECT o.id, f.id FROM DetailOrder d
                INNER JOIN FOOD f ON f.id == d.foodID
                INNER JOIN Orders o ON o.id == d.orderID
            """
    orders = list(conn.execute(query))
    query = """ SELECT f.id ,f.name FROM Food f """
    headers = conn.execute(query)
    header_list = {}
    for header in headers:
        header_list[header[0]] = header[1]
        #header_list.append(ContinuousVariable.make(str(header[1])))
    #domain = Domain(header_list)
    order_list = []
    old_id = orders[0][0]
    temp_list = []
    for order in orders:
        if(old_id != order[0]):
            order_list.append(temp_list)
            temp_list = []
        temp_list.append(order[1])
        old_id = order[0]
    order_list.append(temp_list)
    item_set = dict(orange_asso.frequent_itemsets(order_list, 2))
    rule = orange_asso.association_rules(item_set, .4)
    rules = list(rule)
    with open(target, 'wb') as file:
        pickle.dump([rules,header_list], file)
