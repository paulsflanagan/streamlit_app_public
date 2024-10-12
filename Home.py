from datetime import datetime, timedelta, timezone
from supabase import create_client, Client
import time
import os
import streamlit as st
import pandas as pd
import numpy as np
import io
import zipfile

spb_url = st.secrets["spb_url"]
spb_key = st.secrets["spb_key"]
supabase: Client = create_client(spb_url, spb_key)
userName = st.experimental_user.email

st.title('Gourmet Guru')
#col1, col2 = st.columns([1, 3])
#st.write("ignore this testing something...")
#col1.image("img/1. Teriyaki Prawn Poke Style Bowl.jpg")
#col2.write("1. Gochujang Salmon Poke Bowl  \n with Sesame Sweet Potato and Smacked Cucumber  \n (Korean)  \n[view recipe](https://drive.google.com/file/d/1bYXra2YLgPNHpicqFlTA7bSHacX8nrYO/view?usp=sharing)")
#col1.image("img/2. Thai Style Pork Rice Bowl.jpg")
#col2.write("1. Gochujang Salmon Poke Bowl  \n with Sesame Sweet Potato and Smacked Cucumber  \n (Korean)  \n[view recipe](https://drive.google.com/file/d/1bYXra2YLgPNHpicqFlTA7bSHacX8nrYO/view?usp=sharing)")

with st.sidebar:
        st.title('Settings:')
        st.text("User: " + str(st.experimental_user['email']))
        st.divider()
        st.title('Allergies:')
        allergy_nuts = st.checkbox("Nuts")
        allergy_fish = st.checkbox("Seafood")
        st.divider()
        meals_count = st.slider('How Many Meals?', 1, 5, 5)


# Import Meal Directory and Ingredient Directory
df_meal_directory_pre_allergy = pd.read_csv("meal_directory.csv")
df_ingredient_directory = pd.read_csv("ingredient_directory.csv")



#Allergy Filter
df_meal_directory_buffer = df_meal_directory_pre_allergy

if allergy_nuts:
  df_meal_directory_buffer = df_meal_directory_buffer[df_meal_directory_buffer['allergy'].str.contains('nut') == False]
if allergy_fish:
  meals_count = 3
  df_meal_directory_buffer = df_meal_directory_buffer[df_meal_directory_buffer['allergy'].str.contains('fish') == False]
  df_meal_directory_buffer = df_meal_directory_buffer[df_meal_directory_buffer['allergy'].str.contains('prawn') == False]



df_meal_directory = df_meal_directory_buffer

# Generate Meals
if st.button('Inspire Me'):

  df_menu = pd.DataFrame()
  
  while len(df_menu) < 1:
    df_prospective_meal = df_meal_directory.sample()
    if True:
      df_menu = pd.concat([df_menu, df_prospective_meal])

        
  # Additional Meals
  while len(df_menu) < meals_count:
          
    df_prospective_meal = df_meal_directory.sample()
    if True:
            
      if (df_prospective_meal.iloc[0]['dish_name'] not in set(df_menu['dish_name'].values)):
        if (df_prospective_meal.iloc[0]['style'] not in set(df_menu['style'].values)):
          if (df_prospective_meal.iloc[0]['main_ingredient'] not in set(df_menu['main_ingredient'].values)):
            if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
              df_menu = pd.concat([df_menu, df_prospective_meal])

  st.subheader("Meal Selection")
  #df_menu_display = df_menu[['dish_name','dish_sub_name','style','link']].copy()
  #st.dataframe(df_menu_display, column_config={"dish_name": "Dish", "dish_sub_name": "Accompaniments", "style": "Cuisine",}, hide_index=True)


  #meal_number = 0
  for index, row in df_menu.iterrows():
    st.image("img/" + str(row['id']) + ". " + row['dish_name'] + ".jpg")
    st.write(str(row['id']) + ". " + row['dish_name'] + "  \n " + row['dish_sub_name'] + "  \n (" + row['style'] + ") - " + "[view]("+ row['link'] +")")
    st.write(" ")

  # Extrapolate Ingredients and Attach Category

  string_list = ''

  for row in df_menu.itertuples():

    string_list = string_list + row.ingredients
    string_list = string_list + ','
    split_list = string_list.split(",")

  df = pd.DataFrame(columns=['item','category','quantity'])

  for each in split_list:
    if each not in set(df['item'].values):
      df3 = df_ingredient_directory.loc[df_ingredient_directory['ingredient'] == each]
      try:
        category = df3.iloc[0]['category']
      except:
        category = 'Unknown'
      df.loc[len(df)] = [each,category,1]
    else:
      df2 = df.loc[df['item'] == each]
      value = df2.iloc[0]['quantity']
      value = value + 1
      df.loc[df['item'] == each, 'quantity'] = value



  my_int = int(len(df))
  my_int = my_int - 1


  df_sorted = df.sort_values(by=['category','item'], inplace=False, ascending=True)
  df_sorted.drop([my_int], axis=0, inplace=True)

        
  st.subheader("Shopping List")
  st.dataframe(df_sorted, column_config={"item": "Ingredient", "category": "Section", "quantity": "Quantity",}, hide_index=True)
  #st.write(df_sorted)


  # Create Menu Export

  df_menu_meal_only = df_menu[['id','dish_name','dish_sub_name','link']].copy()

  menu_data_as_csv = df_menu_meal_only.to_csv(index=False).encode("utf-8")

  # Create Shopping List Export

  shopping_list_as_csv = df_sorted.to_csv(index=False).encode("utf-8")
        
  files = [menu_data_as_csv, shopping_list_as_csv]
        
  zipped_file = io.BytesIO()
  with zipfile.ZipFile(zipped_file, 'w') as f:
    f.writestr("Menu.csv", menu_data_as_csv)
    f.writestr("Shopping List.csv", shopping_list_as_csv)

  zipped_file.seek(0)

  count = supabase.table('GormetGuruLogs').insert({"user_name": userName}).execute()

  st.download_button(label="Download",data=zipped_file,file_name="meal_menu.zip")
