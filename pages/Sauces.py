import streamlit as st
from supabase import create_client, Client

spb_url = st.secrets["spb_url"]
spb_key = st.secrets["spb_key"]
supabase: Client = create_client(spb_url, spb_key)
userName = st.experimental_user.email

st.title('Gourmet Guru')

with st.sidebar:
        st.title('Settings:')
        st.text("User: " + str(st.experimental_user['email']))
        st.divider()


st.subheader("Bulgogi Sauce")
st.write("""
* 		brown sugar
* 		seasame oil
* 		soy sauce
* 		red pepper flakes
* 		garlic
* 		ginger
* 		gochijang - (korean chilli pepper sauce)

""")
