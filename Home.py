import os
import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

!wget "https://drive.google.com/uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8"
!wget "https://drive.google.com/uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a"
!wget "https://drive.google.com/uc?export=download&id=1lplwJcZ4a6bWpUGj9D7gNoHjqOyB5Zo-"

df_meal_directory = pd.read_csv('uc?export=download&id=1yi4afzO20LqU2qdRrtK_g04H7juTzUT8')
df_ingredient_directory = pd.read_csv('uc?export=download&id=1EOxvPrpOn3NMwmYg5XegtyXdgjq09A9a')
df_exclude_list = pd.read_csv('uc?export=download&id=1lplwJcZ4a6bWpUGj9D7gNoHjqOyB5Zo-')





st.title('Meal Generator')


