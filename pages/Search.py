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

stop_words = ['and', 'i' '']

search_string = st.chat_input('meal id')
# Generate Meals
if search_string:
  #st.write(df_meal_directory.loc[df_meal_directory['id'] == int(meal_id)])

  try:
    df_display = df_meal_directory.loc[df_meal_directory['id'] == int(search_string)]
  except:
    search_string_list = search_string.split(" ")
    for each in search_string_list:
      if each not in stop_words:
        st.write(each)
        df_search_rows = df_meal_directory.loc[df_meal_directory['dish_name'].str.contains(each, case=False)]
        st.write(df_search_rows)
        #df_prospective_meals = 
        #if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
        #df_menu = pd.concat([df_menu, df_prospective_meal])
        
      

        
  for index, row in df_display.iterrows():
    st.image("img/" + str(row['id']) + ". " + row['dish_name'] + ".jpg")
    st.write(str(row['id']) + ". " + row['dish_name'] + "  \n " + row['dish_sub_name'] + "  \n (" + row['style'] + ") - " + "[view]("+ row['link'] +")")
    st.write(" ")
