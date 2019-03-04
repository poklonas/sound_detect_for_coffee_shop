import sqlite3
import datetime

conn = sqlite3.connect('newDB3.db')
c = conn.cursor()

## do some thing
c.execute("INSERT INTO Orders (time) VALUES (?)", (datetime.datetime(2019,1,25,21,0,0),) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  1,  36) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,? )", (  1,  46) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,? )", (  2,  17) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  3,  22) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  4,  36) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  4,  4) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  5,  14) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  6,  12) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  6,  42) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  7,  3) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  7,  42) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  8,  11) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  8,  45) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  9,  29) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,14,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  10,  45) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  10,  36) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,14,0,0), )) 
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  11,  12) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,15,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  12,  13) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  12,  42) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  12,  45) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,15,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  13,  24) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  14,  32) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  14,  41) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  14,  46) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  15,  18) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  16,  13) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  16,  42) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,18,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  17,  19) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  17,  46) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  18,  35) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  18,  40) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  18,  41) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  18,  46) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  19,  17) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  20,  22) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  21,  24) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  21,  45) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  22,  38) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  22,  44) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  23,  19) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  24,  11) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  25,  13) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  26,  11) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  27,  17) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  28,  18) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  29,  11) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  30,  20) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  31,  10) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  32,  32) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  33,  36) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  33,  41) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  34,  11) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  34,  40) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  35,  13) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  35,  43) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  36,  22) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  36,  42) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  36,  41) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  37,  14) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  37,  41) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  37,  43) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,19,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  38,  24) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  38,  41) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,20,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  39,  38) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,5,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  40,  14) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  40,  45) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,5,30,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  41,  14) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  41,  41) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,6,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  42,  13) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  42,  44) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  42,  45) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  42,  47) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,7,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  43,  2) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,8,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  44,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,8,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  45,  24) )
c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  45,  41) )

conn.commit()