from datetime import datetime, timedelta, timezone
from supabase import create_client, Client
import time
import streamlit as st
import pandas as pd


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
df_meal_directory = pd.read_csv('meal_directory.csv')
df_ingredient_directory = pd.read_csv('ingredient_directory.csv')
df_display = pd.DataFrame()

meal_id = st.chat_input('meal id')
# Generate Meals
if meal_id:
  #st.write(df_meal_directory.loc[df_meal_directory['id'] == int(meal_id)])

  try:
    df_display = df_meal_directory.loc[df_meal_directory['id'] == int(meal_id)]
  except:
    pass

        
  for index, row in df_display.iterrows():
    st.image("img/" + str(row['id']) + ". " + row['dish_name'] + ".jpg")
    st.write(str(row['id']) + ". " + row['dish_name'] + "  \n " + row['dish_sub_name'] + "  \n (" + row['style'] + ") - " + "[view]("+ row['link'] +")")
    st.write(" ")
