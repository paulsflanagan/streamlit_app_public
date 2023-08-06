import os
import streamlit as st
#import requests
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages

st.title('Meal Generator')

import wget
url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
filename = wget.download(url)

st.write(filename)






#!wget "https://drive.google.com/uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8"
#!wget "https://drive.google.com/uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a"
#!wget "https://drive.google.com/uc?export=download&id=1lplwJcZ4a6bWpUGj9D7gNoHjqOyB5Zo-"

#df_meal_directory = pd.read_csv('uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8')
#df_ingredient_directory = pd.read_csv('uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a')
#df_exclude_list = pd.read_csv('uc?export=download&id=1lplwJcZ4a6bWpUGj9D7gNoHjqOyB5Zo-')


st.write('Test 123')

#df_menu = pd.DataFrame()

#st.download_button('Download Output', data=data_as_csv, file_name=export_file_name)

#while len(df_menu) < 1:
  #df_prospective_meal = df_meal_directory.sample()
  #if (df_prospective_meal.iloc[0]['dish_name'] not in set (df_exclude_list['dish_name'].values)):
    #df_menu = pd.concat([df_menu, df_prospective_meal])

# Additional Meals

#while len(df_menu) < 5:
  #df_prospective_meal = df_meal_directory.sample()

  #if (df_prospective_meal.iloc[0]['dish_name'] not in set (df_exclude_list['dish_name'].values)):
   # if (df_prospective_meal.iloc[0]['dish_name'] not in set(df_menu['dish_name'].values)):
     # if (df_prospective_meal.iloc[0]['style'] not in set(df_menu['style'].values)):
      #  if (df_prospective_meal.iloc[0]['main_ingredient'] not in set(df_menu['main_ingredient'].values)):
       #   if (df_prospective_meal.iloc[0]['base_ingredient'] not in set(df_menu['base_ingredient'].values)):
        #    df_menu = pd.concat([df_menu, df_prospective_meal])

#st.write(df_menu)
#st.write(len(df_menu))
