import sqlite3
import datetime

conn = sqlite3.connect('newDB.db')
c = conn.cursor()

## do some thing
c.execute("INSERT INTO Orders (time) VALUES (?)", (datetime.datetime(2019,1,25,21,0,0),) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  1,  36,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  1,  46,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  2,  17,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  3,  22,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  4,  36,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  4,  41,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  5,  14,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  6,  12,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  6,  42,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  7,  3,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  7,  42,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  8,  11,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  8,  45,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  9,  29,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,14,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  10,  45,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  10,  36,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,14,0,0), )) 
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  11,  12,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,15,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  12,  13,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  12,  42,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  12,  45,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,15,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  13,  24,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,13,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  14,  32,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  14,  41,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  14,  46,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  15,  18,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  16,  13,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  16,  42,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,18,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  17,  19,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  17,  46,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,17,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  18,  35,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  18,  40,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  18,  41,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  18,  46,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  19,  17,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  20,  22,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  21,  24,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  21,  45,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  22,  38,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  22,  44,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  23,  19,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  24,  11,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  25,  13,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  26,  11,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  27,  17,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  28,  18,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  29,  11,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  30,  20,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0), ) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  31,  10,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,9,0,0) ,) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  32,  32,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  33,  36,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  33,  41,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,11,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  34,  11,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  34,  40,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,10,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  35,  13,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  35,  43,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  36,  22,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  36,  42,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  36,  41,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,12,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  37,  14,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  37,  41,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  37,  43,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,19,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  38,  24,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  38,  41,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,20,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  39,  38,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,5,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  40,  14,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  40,  45,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,5,30,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  41,  14,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  41,  41,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,6,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  42,  13,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  42,  44,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  42,  45,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  42,  47,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,7,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  43,  2,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,8,0,0) ,))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  44,  1,  1) )

c.execute("INSERT INTO Orders (time) VALUES (?)", ( datetime.datetime(2019,1,25,8,0,0), ))
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  45,  24,  1) )
c.execute("INSERT INTO DetailOrder (orderID, foodID, optionalID) VALUES (?,?,?)", (  45,  41,  1) )

conn.commit()