import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
from sqlite3 import *
import time
from apps import insert, Update, Delete, Display
from multiapp import MultiApp
app=MultiApp()


st.title("CAR Sales Management System")
st.markdown("This application is a streamlit dashboard that can be used to analyze the motor vehicle sales.")
    

app.add_app("Insert",insert.app)
app.add_app("UPdate",Update.app)
app.add_app("Delete",Delete.app)
app.add_app("Display",Display.app)

app.run()   




            
            
            
        
        
        
        
                