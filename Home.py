import os
import streamlit as st
#import requests
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages

st.title('Meal Generator')

import wget


url_meal_directory = "https://drive.google.com/uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8"
url_ingredients_directory = "https://drive.google.com/uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a"
filename_meal_directory = wget.download(url_meal_directory)
filename_ingredients_directory = wget.download(url_ingredients_directory)
df_meal_directory = pd.read_csv(filename_meal_directory)
df_ingredient_directory = pd.read_csv(filename_ingredients_directory)


st.write(df_meal_directory)

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
  
  while len(df_menu) < 5:
    df_prospective_meal = df_meal_directory.sample()
  
    #if (df_prospective_meal.iloc[0]['dish_name'] not in set (df_exclude_list['dish_name'].values)):
    if True:
      if (df_prospective_meal.iloc[0]['dish_name'] not in set(df_menu['dish_name'].values)):
        if (df_prospective_meal.iloc[0]['style'] not in set(df_menu['style'].values)):
          if (df_prospective_meal.iloc[0]['main_ingredient'] not in set(df_menu['main_ingredient'].values)):
            if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
              df_menu = pd.concat([df_menu, df_prospective_meal])
  
  st.write(df_menu)
#st.write(len(df_menu))
