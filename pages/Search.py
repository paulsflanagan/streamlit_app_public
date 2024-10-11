
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


## Filter Key words from dish names
dish_name_list = list(df_meal_directory['dish_name'])
dish_sub_name_list = list(df_meal_directory['dish_sub_name'])
dish_name_key_words = []
stop_words = ['and', 'in', '\'n\'', 'a', 'la', '&']

for each in dish_name_list:
   dish_name_list_split = each.split(" ")
   for word in dish_name_list_split:
     if word not in stop_words:
       if word not in dish_name_key_words:
         dish_name_key_words.append(word.lower())
               
for each in dish_sub_name_list:
   dish_name_list_split = each.split(" ")
   for word in dish_name_list_split:
     if word not in stop_words:
       if word not in dish_name_key_words:
         dish_name_key_words.append(word.lower())
##

result_dictionary = {}

search_string = st.chat_input('meal id')
# Generate Meals
if search_string:
  #st.write(df_meal_directory.loc[df_meal_directory['id'] == int(meal_id)])

  try:
    df_display = df_meal_directory.loc[df_meal_directory['id'] == int(search_string)]
  except:
    search_string_list = search_string.split(" ")
    for each in search_string_list:
      if each in dish_name_key_words:
        #st.write(each)
        df_search_name_rows = df_meal_directory.loc[df_meal_directory['dish_name'].str.contains(each, case=False)]
        df_search_sub_name_rows = df_meal_directory.loc[df_meal_directory['dish_sub_name'].str.contains(each, case=False)]
        df_search_rows = pd.concat([df_search_name_rows, df_search_sub_name_rows])
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
    df_results = pd.DataFrame(result_dictionary.items())
    df_results = df_results.drop(df_results.loc[df_results['1']==1].index, inplace=True)
    df_results = df_results.sort_values(by=1, ascending=False)
    results = list(df_results[0])
    st.write(results)
    x = 0
    while x < 5:
      #here
      df_buffer = df_meal_directory.loc[df_meal_directory['id'] == int(results[x])]
      df_display = pd.concat([df_display, df_buffer])
      x = x+1

  #st.write(result_dictionary)
          #counter = result_dictionary[rows]
        #st.write(df_search_rows)
        #df_prospective_meals = 
        #if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
        #df_menu = pd.concat([df_menu, df_prospective_meal])
        
      

        
  for index, row in df_display.iterrows():
    st.image("img/" + str(row['id']) + ". " + row['dish_name'] + ".jpg")
    st.write(str(row['id']) + ". " + row['dish_name'] + "  \n " + row['dish_sub_name'] + "  \n (" + row['style'] + ") - " + "[view]("+ row['link'] +")")
    st.write(" ")
