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

st.subheader("")
st.subheader("All American Spice Blend")
st.write("""
* 		2 part garlic powder
* 		1 part ground cumin
* 		1 part cayenne
* 		1 part onion powder
* 		1 part smoked paprika
* 		1 part ground coriander
* 		1 part salt
* 		1 part dried parsley
* 		1/2 part black pepper
* 		1/2 part dried mustard
* 		1/2 part red pepper flakes
* 		1/4 part ground allspice
* 		1/8 part ground cloves
""")

st.subheader("")
st.subheader("Berbere Spice Blend")
st.write("""
* 		3 part paprika
* 		1 part cayenne
* 		.5 part ground coriander
* 		.25 part ground ginger
* 		.125 part ground cardamom
* 		.125 part ground fenugreek
""")

st.subheader("")
st.subheader("Bold and Savory Steak Spice Blend")
st.write("""
* 		4 parts garlic powder
* 		4 parts ground black pepper
* 		3 parts crushed mustard seed
* 		2 parts crushed dill seed
* 		1 part red chili flake
* 		1 part crushed coriander seed
""")

st.subheader("")
st.subheader("Blackening Spice Blend")
st.write("""
* 		3 parts smoked paprika
* 		2 parts garlic powder
* 		1/2 part white pepper
* 		1/2 part black pepper
* 		1/4 part thyme
* 		1/4 part oregano
* 		1/4 part low heat cayenne
""")

st.subheader("")
st.subheader("Burger Spice Blend")
st.write("""
* 		2 parts paprika
* 		1 part salt
* 		1 part ground black pepper
* 		1/2 part garlic powder
* 		1/2 part brown sugar
* 		1/2 part onion powder
* 		1/4 part cayenne
""")

st.subheader("")
st.subheader("Cajun Spice Blend")
st.write("""
* 		2 parts paprika
* 		2 parts onion powder
* 		1 part garlic powder
* 		1 part dried oregano
* 		1 part dried thyme
* 		1/2 part dried basil
* 		1/2 part cayenne
""")

st.subheader("")
st.subheader("Enchilada Spice Blend")
st.write("""
* 		2 parts chili powder
* 		2 parts paprika
* 		2 parts cumin
* 		2 parts light brown sugar
* 		2 parts kosher salt
* 		1.5 parts onion powder
* 		1.5 parts garlic powder
* 		1.5 parts Mexican oregano
* 		1 part chipotle chili powder
* 		1 part ground coriander
* 		1 part black pepper
* 		1/2 part cayenne pepper
""")

st.subheader("")
st.subheader("Fall Spice Blend")
st.write("""
* 		3 parts dried thyme
* 		3 parts ground sage
* 		2 parts garlic powder
* 		1 part onion powder
""")

st.subheader("")
st.subheader("Fry Seasoning")
st.write("""
* 		1 part garlic powder
* 		1 part onion powder
* 		1 part paprika
""")

st.subheader("")
st.subheader("Herbes de Provence Blend")
st.write("""
* 		1 part savory
* 		1 part thyme
* 		1 part rosemary
* 		1 part basil
* 		1 part tarragon
* 		1 part lavender flowers
""")

st.subheader("")
st.subheader("Italian Seasoning Blend")
st.write("""
* 		1 part garlic powder
* 		1 part oregano
* 		1 part basil
* 		1 part black pepper
* 		1 part parsley
""")

st.subheader("")
st.subheader("Indonesian Spice Mix")
st.write("""
* 		2 parts coriander
* 		1 part cumin
* 		1 part fennel seeds
* 		1/2 part cayenne pepper
* 		1/2 part turmeric powder
* 		1/2 part  cinnamon
* 		1/2 part cardamom
* 		1/2 part black pepper
* 		1/2 part ground cloves (optional)
""")

st.subheader("")
st.subheader("Kasaba Spice Blend")
st.write("""
* 		1 part saffron (alternative: 1/2 part paprika and 1/2 part turmeric)
* 		1 part ground cinnamon
* 		1 part allspice
* 		1 part dried whole lime powder
* 		1 part ground cardamom
* 		1 part ground white pepper
""")

st.subheader("")
st.subheader("Meatloaf Seasoning")
st.write("""
* 		2 parts onion powder
* 		2 parts garlic powder
""")

st.subheader("")
st.subheader("Mediterranean Spice Blend")
st.write("""
* 		2 parts dried oregano
* 		1 part dried mint
* 		1 part sumac
* 		1 part ground coriander
""")

st.subheader("")
st.subheader("Mexican Spice Blend")
st.write("""
* 		2 parts chili powder
* 		1 part oregano
* 		1 part smoked paprika
* 		1 part cumin.
""")

st.subheader("")
st.subheader("Moo Shu Spice Blend")
st.write("""
* 		1 part ground ginger
* 		1 part garlic powder
""")

st.subheader("")
st.subheader("Ranch Spice Blend")
st.write("""
* 		2 part dried parsley
* 		1 1/2 parts dried dill weed
* 		2 parts dried garlic powder
* 		2 parts onion powder
* 		2 parts dried onion flakes
* 		1 part ground black pepper
* 		1 dried chives
""")

st.subheader("")
st.subheader("Shawarma Spice Blend")
st.write("""
* 		2 part tumeric
* 		2 part cumin
* 		1 part dried coriander
* 		1 part garlic powder
* 		1 part paprika
* 		1/2 part ground allspice
* 		1/2 part black pepper
""")

st.subheader("")
st.subheader("Southwest Spice Blend")
st.write("""
* 		4 part garlic powder
* 		2 part cumin
* 		2 part chili powder
""")

st.subheader("")
st.subheader("Smoky BBQ Seasoning")
st.write("""
* 		8 parts smoked paprika
* 		6 parts granulated sugar
* 		2 parts garlic powder
* 		1 part dry mustard
* 		1 part ground cumin
* 		1 part ground ginger
* 		1/2 part black pepper
""")

st.subheader("")
st.subheader("Smoky Cinnamon Paprika Spice Blend")
st.write("""
* 		6 parts sweet paprika
* 		6 parts sugar
* 		4 parts mustard powder
* 		2 parts onion powder
* 		2 parts ground cinnamon
* 		1 parts smoked paprika
* 		1/4 part ground cloves
""")

st.subheader("")
st.subheader("Steak Spice Blend")
st.write("""
* 		4 parts dried minced garlic
* 		4 parts crushed black pepper
* 		3 parts kosher salt
* 		3 parts crushed mustard seed
* 		2 parts crushed dill seed
* 		1 part red chili flakes
* 		1 part crushed coriander seed
""")

st.subheader("")
st.subheader("Sweet Smoky BBQ Spice Blend")
st.write("""
* 		8 parts smoked paprika
* 		6 parts sugar
* 		2 parts garlic powder
* 		1 part dry mustard
* 		1 part cumin
* 		1 part ground ginger
* 		1/2 part black pepper
""")

st.subheader("")
st.subheader("Thai Seven Spice Blend")
st.write("""
* 		2.5 parts white sesame seeds
* 		1 part chili flakes
* 		1 part ground coriander
* 		1 part onion powder
* 		1/2 part garlic powder
* 		1/2 part shrimp extract powder
* 		1/2 part cinnamon
* 		1/3 part low heat cayenne
""")

st.subheader("")
st.subheader("Tunisian Spice Blend")
st.write("""
* 		4 parts ground caraway seed
* 		4 parts ground coriander
* 		4 parts smoked paprika
* 		4 parts turmeric
* 		4 parts chili powder
* 		4 parts garlic powder
* 		1 part cayenne pepper
* 		1 part cinnamon
* 		1 part ground black pepper
""")

st.subheader("")
st.subheader("Turkish Spice Blend")
st.write("""
* 		2 part cumin
* 		2 part garlic powder
* 		1 part ground coriander
* 		.25 part ground allspice
* 		.25 part chili flakes
""")

st.subheader("")
st.subheader("Tuscan Heat Spice Blend")
st.write("""
* 		4 parts dried basil
* 		2 parts dried rosemary
* 		2 parts dried oregano
* 		2 parts garlic powder
* 		1 part cayenne pepper [7.5 k (hu)]
* 		1 part ground fennel
""")

st.subheader("")
st.subheader("Za’atar Spice Blend")
st.write("""
* 		2 part dried oregano
* 		2 parts sumac
* 		2 parts sesame seeds
* 		1 part dried marjoram (or additional oregano)
* 		1 part dried thyme
* 		1/2 part fine sea salt
""")
