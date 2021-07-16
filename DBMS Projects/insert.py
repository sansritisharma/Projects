import streamlit as st
from sqlite3 import *
def app():
    
    st.title('Insert')
    number_plate = st.text_input('Input your Car Number plate:')
    Owner_name = st.text_input('Input your Name:')
    model_year= st.text_input('Input your model year:')
    model_name= st.text_input('Input your car model name:')
    model_cost= st.text_input('Input your car model cost:')
    model_service= st.text_input('Input your car service cost:')
    
    con = connect('myTable.db')
    cur = con.cursor()
    if(st.button("Submit")):
        cur.execute("""INSERT INTO CAR(number_plate,Owner_name,model_year,model_name,model_cost,model_service) VALUES(?,?,?,?,?,?);""",(number_plate,Owner_name,model_year,model_name,model_cost,model_service))
        st.markdown("Inserted")
    con.commit()
    con.close()
