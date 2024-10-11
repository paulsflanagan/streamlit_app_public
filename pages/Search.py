from datetime import datetime, timedelta, timezone
from supabase import create_client, Client
import time
import streamlit as st
import pandas as pd
import os

meal_directory_path = os.path.realpath("../meal_directory.csv")
ingredient_directory_path = os.path.realpath("../ingredient_directory.csv")


spb_url = st.secrets["spb_url"]
spb_key = st.secrets["spb_key"]
supabase: Client = create_client(spb_url, spb_key)
userName = st.experimental_user.email

st.title('Gourmet Guru')

with st.sidebar:
        st.title('Settings:')
        st.text("User: " + str(st.experimental_user['email']))
        st.divider()


# Import Meal Directory and Ingredient Directory
df_meal_directory = pd.read_csv(meal_directory_path)
df_ingredient_directory = pd.read_csv(ingredient_directory_path)



# Generate Meals
if st.button('ID Search'):
  st.write('Hello!')
