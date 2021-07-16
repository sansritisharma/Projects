import streamlit as st
from sqlite3 import *
def app():
    
    st.title('Update')
    con = connect('myTable.db')
    cur = con.cursor()
    number_plate1 = st.text_input('Input your Car Number plate:')
    if(st.button("Submit")):
        
        
        cur.execute("""SELECT * from CAR WHERE number_plate=?;""",(number_plate1,))
        rows = cur.fetchall()
        for row in rows:
            st.markdown(row)
        #app1 = st.selectbox('What do you want to update',('-','Owner_name','model_year','model_name','model_cost','model_service'))
        app1=st.text_input("What do you wanna update")
        a = st.text_input('Input :')
        '''
        if app1=='Owner_name':
            a = st.text_input('Input your Car Owner Name:')
        
            cur.execute("""UPDATE CAR SET Owner_name=? WHERE number_plate=?;""",(a,number_plate1))
        elif app1=='model_year':
            a = st.text_input('Input your Car model year:')
            
            cur.execute("""UPDATE CAR SET model_year=? WHERE number_plate=?;""",(a,number_plate1))
        elif app1=='model_name':
            a = st.text_input('Input your Car model name:')
            cur.execute("""UPDATE CAR SET model_name=? WHERE number_plate=?;""",(a,number_plate1))
        elif app1=='model_cost':
            a = st.text_input('Input your Car model cost:')
            cur.execute("""UPDATE CAR SET model_cost=? WHERE number_plate=?;""",(a,number_plate1))
        elif app1=='model_service':
            a = st.text_input('Input your Car model service cost:')
            cur.execute("""UPDATE CAR SET model_service=? WHERE number_plate=?;""",(a,number_plate1))
        elif app1=="-":
            pass
        else:
            st.markdown("Error")
        '''    
    con.commit()
    con.close()
    
