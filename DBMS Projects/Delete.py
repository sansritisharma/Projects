import streamlit as st
from sqlite3 import *
def app():
    
    st.title('Delete')
    con = connect('myTable.db')
    cur = con.cursor()
    
    number_plate2 = st.text_input('Input your Car Number plate:')
    if(st.button("Submit")):
        
        cur.execute("""DELETE FROM CAR WHERE number_plate=?;""",(number_plate2,))          
        cur.execute("""SELECT * FROM CAR;""")   
    #st.markdown("Enter a Valid Entry\n")
        
        
    rows = cur.fetchall()
    for row in rows:
        st.markdown(row)
    
    
    con.commit()
    con.close()
    
