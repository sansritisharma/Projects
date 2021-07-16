import streamlit as st
from sqlite3 import *
def app():
    
    st.title('Display')
    con = connect('myTable.db')
    cur = con.cursor()
    
    cur.execute("""SELECT * FROM CAR;""")          
    
        
        
    rows = cur.fetchall()
    for row in rows:
        st.markdown(row)
    
    
    con.commit()
    con.close()
    
