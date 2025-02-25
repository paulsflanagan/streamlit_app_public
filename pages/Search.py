
from datetime import datetime, timedelta, timezone
from supabase import create_client, Client
import time
import streamlit as st
import pandas as pd
import re


spb_url = st.secrets["spb_url"]
spb_key = st.secrets["spb_key"]
supabase: Client = create_client(spb_url, spb_key)
userName = "Unknown" #st.experimental_user.email

st.title('Gourmet Guru')

with st.sidebar:
        st.title('Settings:')
        #st.text("User: " + str(st.experimental_user['email']))
        st.divider()


# Import Meal Directory and Ingredient Directory
df_meal_directory = pd.read_csv('meal_directory.csv')
df_ingredient_directory = pd.read_csv('ingredient_directory.csv')
df_display = pd.DataFrame()


## Filter Key words from dish names
dish_name_list = list(df_meal_directory['dish_name'])
dish_sub_name_list = list(df_meal_directory['dish_sub_name'])
ingredients_list = list(df_meal_directory['ingredients'])
search_key_words = []

stop_words = ['and', 'in', '\'n\'', 'a', 'la', '&', 'with', 'style', 'ultimate', 'quick', 'pan', 'on', 'mine', 'de']

for each in dish_name_list:
   dish_name_list_split = each.split(" ")
   for word in dish_name_list_split:
     word = word.lower().replace(',', '')
     if word not in stop_words:
       if word not in search_key_words:
         search_key_words.append(word)
               
for each in dish_sub_name_list:
   dish_sub_name_list_split = each.split(" ")
   for word in dish_sub_name_list_split:
     word = word.lower().replace(',', '')
     if word not in stop_words:
       if word not in search_key_words:
         search_key_words.append(word)
               
for each in ingredients_list:
   ingredients_list_split = re.split(',| ', each)
   for word in ingredients_list_split:
     word = word.lower().replace(',', '')
     if word not in stop_words:
       if word not in search_key_words:
         search_key_words.append(word)
               
#st.write(search_key_words)
##

result_dictionary = {}

search_string = st.chat_input('meal id or ingredients')
# Generate Meals
if search_string:
  #st.write(df_meal_directory.loc[df_meal_directory['id'] == int(meal_id)])

  try:
    df_display = df_meal_directory.loc[df_meal_directory['id'] == int(search_string)]
  except:
    search_string_list = search_string.split(" ")
    for each in search_string_list:
      if each in search_key_words:
        #st.write(each)
        df_search_name_rows = df_meal_directory.loc[df_meal_directory['dish_name'].str.contains(each, case=False)]
        df_search_sub_name_rows = df_meal_directory.loc[df_meal_directory['dish_sub_name'].str.contains(each, case=False)]
        df_ingredients_rows = df_meal_directory.loc[df_meal_directory['ingredients'].str.contains(each, case=False)]
        df_search_rows = pd.concat([df_search_name_rows, df_search_sub_name_rows, df_ingredients_rows])
        search_rows = list(df_search_rows['id'])
        for row in search_rows:
          #st.write(row)
          try:
            counter = result_dictionary[row]
            counter = counter + 1
            result_dictionary[row] = counter
          except:
            result_dictionary[row] = 1
    #here
    df_results = pd.DataFrame(result_dictionary.items(), columns=list('ab'))
    df_results = df_results.sort_values(by='b', ascending=False)
    if len(df_results.index) <= 5:
      pass
    else:
      df_results_try = df_results[df_results.b > 1]
      if len(df_results_try.index) <= 5:
        pass
      else:
        df_results = df_results[df_results.b > 1]
    results = list(df_results['a'])
    x = 0
    for each in results:
      if x < 5:
        #here
        df_buffer = df_meal_directory.loc[df_meal_directory['id'] == int(results[x])]
        df_display = pd.concat([df_display, df_buffer])
        x = x+1

        
  for index, row in df_display.iterrows():
    st.image("img/" + str(row['id']) + ". " + row['dish_name'] + ".jpg")
    st.write(str(row['id']) + ". " + row['dish_name'] + "  \n " + row['dish_sub_name'] + "  \n (" + row['style'] + ") - " + "[view]("+ row['link'] +")")
    st.write(" ")
