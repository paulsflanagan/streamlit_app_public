import os
import streamlit as st
#import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

st.title('Meal Generator')


with st.sidebar:
        st.title('Settings:')
        st.text("User: " + str(st.experimental_user['email']))
        st.divider()
        meals_count = st.slider('How Many Meals?', 1, 7, 5)




import wget

'''
Move CSV Repo to GitHub
Google Drive being in consistent with HTTPErrors
'''
#if st.button('Update Data'):
url_meal_directory = "https://drive.google.com/uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8"
url_ingredients_directory = "https://drive.google.com/uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a"
filename_meal_directory = wget.download(url_meal_directory)
filename_ingredients_directory = wget.download(url_ingredients_directory)
df_meal_directory = pd.read_csv(filename_meal_directory)
df_ingredient_directory = pd.read_csv(filename_ingredients_directory)


# DISPLAY ALL MEALS
#st.write(df_meal_directory)


#st.write(df_ingredient_directory)

if st.button('Generate Meals'):

  df_menu = pd.DataFrame()
  
  #st.download_button('Download Output', data=data_as_csv, file_name=export_file_name)
  
  while len(df_menu) < 1:
    df_prospective_meal = df_meal_directory.sample()
    #if (df_prospective_meal.iloc[0]['dish_name'] not in set (df_exclude_list['dish_name'].values)):
    if True:
      df_menu = pd.concat([df_menu, df_prospective_meal])
  
  # Additional Meals
  
  while len(df_menu) < meals_count:
    df_prospective_meal = df_meal_directory.sample()
  
    #if (df_prospective_meal.iloc[0]['dish_name'] not in set (df_exclude_list['dish_name'].values)):
    if True:
      if (df_prospective_meal.iloc[0]['dish_name'] not in set(df_menu['dish_name'].values)):
        if (df_prospective_meal.iloc[0]['style'] not in set(df_menu['style'].values)):
          if (df_prospective_meal.iloc[0]['main_ingredient'] not in set(df_menu['main_ingredient'].values)):
            if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
              df_menu = pd.concat([df_menu, df_prospective_meal])
  
  st.write(df_menu)

  # Extrapolate Ingredients and Attach Category

  string_list = ''

  for row in df_menu.itertuples():

    string_list = string_list + row.ingredients
    string_list = string_list + ','
    split_list = string_list.split(",")

  df = pd.DataFrame(columns=['item','category','quantity'])

  for each in split_list:
    if each not in set(df['item'].values):
      #print(each)
      df3 = df_ingredient_directory.loc[df_ingredient_directory['ingredient'] == each]
      #print(df3)
      try:
        category = df3.iloc[0]['category']
        #print(category)
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

  #df.drop([my_int], axis=0, inplace=True)

  df_sorted = df.sort_values(by=['category','item'], inplace=False, ascending=True)
  df_sorted.drop([my_int], axis=0, inplace=True)


  st.write(df_sorted)
  #st.write(len(df_menu))



  # Create Menu List PDF

  df_menu_meal_only = df_menu[['dish_name','dish_sub_name','link']].copy()


  fig, ax =plt.subplots(figsize=(12,4))
  ax.axis('tight')
  ax.axis('off')
  the_table = ax.table(cellText=df_menu_meal_only.values,colLabels=df_menu_meal_only.columns,loc='center')

  pp = PdfPages("menu_export.pdf")
  pp.savefig(fig, bbox_inches='tight')
  pp.close()
