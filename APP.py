from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import pandas as pd
 
import google.generativeai as generativeai
 
 
generativeai.configure(api_key=os.getenv("API_KEY"))
 
def get_gemini_response(question , prompt):
    model = generativeai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0] , question])
    return response.text
 
def read_sql_query (sql , db ):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
 
    return rows
 
def string_replace(sql_text , character_to_replace):
    new_string = sql_text.replace(character_to_replace,'')
    return(new_string)
 
prompt = [
    """
      You are an expert in coverting the english question to sql query . The query is to be generated in the context of python sqllite syntax
    The sql database has the name oe_order_headers and has column ORDER_NUMBER , bill_customer , SHIP_CUSTOMER AND header_id as primary key
    it also has the oe_order_lines which is the child table of oe_order_headers and has header_id a primary key and it contain isbn details
    Example 1 - How many orders are present would look something like this select count(1) from oe_order_headers ;
    Example 2 --how many lines are present for an order would look selct count(1) from oe_order_lines but we have to check for the associated header recrods
    Please  remove the ``` in the beginning and end of sql word  and the sql text generated should not have ```
    """
    ]
 
 
##sTREAMLIT APP
st.set_page_config(page_title="MHE Sql tech request generator")
st.header("Gemini app to retrive sql data from text")
 
question=st.text_input("Input ", key="input")
 
submit=st.button("Please ask the question ")
 
if submit:
    response=get_gemini_response(question, prompt)
    print(response)
   
    st.subheader("Response sql text")
   
    new_string1= string_replace(response,'`')
    new_string2= string_replace(new_string1,'sql')
    print(new_string2)
   
    st.header(new_string2)
    data =read_sql_query(new_string2,"students.db")
    st.subheader('Data content')
    list=[]
    for row in data:
       list.append(row)
 
    df = pd.DataFrame(list, columns=['cUST#', 'Count#(isbn)'])  
 
    st.dataframe(df)