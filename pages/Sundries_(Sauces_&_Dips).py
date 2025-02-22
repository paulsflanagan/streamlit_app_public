import streamlit as st
from supabase import create_client, Client

spb_url = st.secrets["spb_url"]
spb_key = st.secrets["spb_key"]
supabase: Client = create_client(spb_url, spb_key)
userName = "Unknown" #st.experimental_user.email

st.title('Gourmet Guru')

with st.sidebar:
        st.title('Settings:')
        #st.text("User: " + str(st.experimental_user['email']))
        st.divider()
        
st.subheader("")
st.header("Sauces")
st.subheader("")
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

st.subheader("")
st.subheader("Ketjap Manis - (substitution)")
st.write("""
* 		3 parts honey
* 		1 parts soy sauce
                or
* 		2 parts honey
* 		1 parts oyster sauce
                or
* 		brown or palm sugar
* 		soy sauce
""")
st.subheader("")
st.header("Dips")
st.subheader("")
st.subheader("Tabbouleh")
st.write("""
* 		1 cup diced cucumber (salted and drained)
* 		1 cup diced tomato (salted and drained)
* 		3 medium bunches curly parsley
* 		½ cup bulgur (cooked)
* 		⅓ cup chopped fresh mint (optional)
* 		⅓ cup thinly sliced green onion
* 		⅓ cup extra-virgin olive oil
* 		3 to 4 tablespoons lemon juice, to taste)
* 		1 teaspoon fine salt
* 		1 medium clove garlic (pressed or minced)

""")
