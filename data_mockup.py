import sqlite3
 
##connect to sqllite 3
 
connection = sqlite3.connect("students.db")
 
 
## create a cursor to insert update and create table veiw
cursor = connection.cursor()
 
 
##create the table
order_table_info = """
 CREATE table oe_order_headers (
 ORDER_NUMBER VARCHAR2(100),
 BILL_CUSTOMER VARCHAR2(100) ,
 SHIP_CUSTOMER VARCHAR2(100),
 ORDER_TYPE VARCHAR2(100),
 header_id integer not null PRIMARY KEY )
 
"""
 
order_lines_info = """
CREATE table oe_order_lines (
 header_id integer not null ,
 line_id integer not null PRIMARY KEY AUTOINCREMENT ,
 ISBN varchar2(100)
 )
 
"""
 
cursor.execute(order_table_info)
 
cursor.execute( order_lines_info)
 
 
cursor.execute('''INSERT INTO oe_order_headers values ( '123','amazon bill to' ,'amazon shipto' ,'SALE-US',1)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '456','MYNTRA bill to' ,'MYNTRA shipto' ,'SALE-US',2)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '789','borders bill to' ,'borders shipto' ,'SALE-US',3)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '666','123xyx bill to' ,'123xyx shipto' ,'SALE-US',4)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '555','45677 bill to' ,'478965 shipto' ,'SALE-US',5)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '444','flipkart bill to' ,'flipkart shipto' ,'SALE-US',6)''')
cursor.execute('''INSERT INTO oe_order_headers values ( '222','future retail bill to' ,'future retail shipto' ,'SALE-US',7)''')
 
 
cursor.execute('''INSERT INTO oe_order_lines values ( '1','11' ,'ISBN1')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '2','22' ,'ISBN2')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '3','33' ,'ISBN3')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '4','44' ,'ISBN4')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '5','55' ,'ISBN5')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '6','66' ,'ISBN6')''')
cursor.execute('''INSERT INTO oe_order_lines values ( '7','77' ,'ISBN7')''')
 
 
print("The inserted records are ")
 
data = cursor.execute('''select * from oe_order_headers''')
 
for row in data:
    print(row)
 
data2 = cursor.execute('''sELECT bill_customer,
       COUNT(*) AS count_of_isbn_details
FROM oe_order_headers
JOIN oe_order_lines ON oe_order_headers.header_id = oe_order_lines.header_id
GROUP BY bill_customer''')  
 
for row2 in data2:
     print(row2)
 
 
connection.commit()
connection.close()
 