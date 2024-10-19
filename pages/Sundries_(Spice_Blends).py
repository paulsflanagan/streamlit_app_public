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


st.subheader("All American Spice Blend")
st.write("""
* 		1 tbsp ground cumin
* 		1 tbsp cayenne
* 		1 tbsp onion powder
* 		1 tbsp smoked paprika
* 		2 tsp garlic powder
* 		1 tsp ground coriander
* 		1 tsp salt
* 		1 tsp dried parsley
* 		1/2 tsp black pepper
* 		1/2 tsp dried mustard
* 		1/2 tsp red pepper flakes
* 		1/4 tsp ground allspice
* 		1/8 tsp ground cloves
""")

st.subheader("Berbere Spice Blend")
st.write("""
* 		3 part paprika
* 		1 part cayenne
* 		.5 part ground coriander
* 		.25 part ground ginger
* 		.125 part ground cardamom
* 		.125 part ground fenugreek
""")

st.subheader("Bold and Savory Steak Spice Blend")
st.write("""
* 		1 part red chili flake
* 		1 part crushed coriander seed
* 		2 parts crushed dill seed
* 		3 parts crushed mustard seed
* 		4 parts dried minced garlic
* 		4 parts crushed black pepper
""")

st.subheader("Blackening Spice Blend")
st.write("""
* 		3 tsp smoked paprika
* 		1.5 tsp garlic powder
* 		.5 tsp white pepper
* 		.5 tsp black pepper
* 		.25 tsp thyme
* 		.25 tsp oregano
* 		.125 tsp low heat cayenne
""")


st.subheader("Burger Spice Blend")
st.write("""
* 		1 Tbsp paprika
* 		1 1/4 tsp salt
* 		1 tsp ground black pepper
* 		1/2 tsp garlic powder
* 		1/2 tsp brown sugar
* 		1/2 tsp onion powder
* 		1/4 tsp cayenne
""")

st.subheader("Cajun Spice Blend")
st.write("""
* 		2 part paprika
* 		2 part onion powder
* 		1 part garlic powder
* 		1 part dried oregano
* 		1 part dried thyme
* 		.5 part dried basil
* 		.5 part cayenne
""")

st.subheader("Enchilada Spice Blend")
st.write("""
* 		1 tbsp. chili powder
* 		1 tbsp. paprika
* 		2 tsp. cumin
* 		2 tsp. light brown sugar
* 		2 tsp. kosher salt
* 		1.5 tsp. onion powder
* 		1.5 tsp. garlic powder
* 		1.5 tsp. Mexican oregano
* 		1 tsp. chipotle chili powder
* 		1 tsp. ground coriander
* 		1 tsp. black pepper
* 		1/4 to .5 tsp. cayenne pepper
""")

st.subheader("Fall Spice Blend")
st.write("""
* 		3 parts dried thyme
* 		3 parts ground sage
* 		2 parts garlic powder
* 		1 part onion powder
""")

st.subheader("Fry Seasoning")
st.write("""
* 		1 part garlic powder
* 		1 part onion powder
* 		1 part paprika
""")


st.subheader("Herbes de Provence Blend")
st.write("""
* 		1 part savory
* 		1 part thyme
* 		1 part rosemary
* 		1 part basil
* 		1 part tarragon
* 		1 part lavender flowers
""")

st.subheader("Italian Seasoning Blend")
st.write("""
* 		1 part garlic powder
* 		1 part oregano
* 		1 part basil
* 		1 part black pepper
* 		1 part parsley
""")

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
* 		cloves (optional)
""")

st.subheader("Kasaba Spice Blend")
st.write("""
* 		1 part saffron (alternative: 1/2 part paprika and 1/2 part turmeric)
* 		1 part ground cinnamon
* 		1 part allspice
* 		1 part dried whole lime powder
* 		1 part ground cardamom
* 		1 part ground white pepper
""")

st.subheader("Meatloaf Seasoning")
st.write("""
* 		2 parts onion powder
* 		2 parts garlic powder
""")

st.subheader("Mediterranean Spice Blend")
st.write("""
* 		2 parts dried oregano
* 		1 part dried mint
* 		1 part sumac
* 		1 part ground coriander
""")

st.subheader("Mexican Spice Blend")
st.write("""
* 		2 parts chili powder
* 		1 part oregano
* 		1 part smoked paprika
* 		1 part cumin.
""")

st.subheader("Moo Shu Spice Blend")
st.write("""
* 		1 part ground ginger
* 		1 part garlic powder
""")

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

st.subheader("Shawarma Spice Blend")
st.write("""
* 		2 part tumeric
* 		2 part cumin
* 		1 part dried coriander
* 		1 part garlic powder
* 		1 part paprika
* 		.5 part ground allspice
* 		.5 part black pepper
""")

st.subheader("Southwest Spice Blend")
st.write("""
* 		4 part garlic powder
* 		2 part cumin
* 		2 part chili powder
""")

st.subheader("Smoky BBQ Seasoning")
st.write("""
* 		8 parts smoked paprika
* 		6 parts granulated sugar
* 		2 parts garlic powder
* 		1 part dry mustard
* 		1 part ground cumin
* 		1 part ground ginger
* 		.5 part black pepper
""")

st.subheader("Smoky Cinnamon Paprika Spice Blend")
st.write("""
* 		1 part ground cloves
* 		8 parts onion powder
* 		8 parts ground cinnamon
* 		6 parts smoked paprika
* 		16 parts mustard powder
* 		24 parts sweet paprika
* 		24 parts sugar
""")

st.subheader("Steak Spice Blend")
st.write("""
* 		1 part red chili flakes
* 		1 part crushed coriander seed
* 		2 parts crushed dill seed
* 		3 parts crushed mustard seed
* 		4 parts dried minced garlic
* 		4 parts crushed black pepper
* 		3 parts kosher salt
""")

st.subheader("Sweet Smoky BBQ Spice Blend")
st.write("""
* 		8 parts smoked paprika
* 		6 parts sugar
* 		2 parts garlic powder
* 		.5 part black pepper
* 		1 part dry mustard
* 		1 part cumin
* 		1 part ground ginger
""")

st.subheader("Thai Seven Spice Blend")
st.write("""
* 		2.5 tsp white sesame seeds
* 		1 tsp chili flakes
* 		1 tsp ground coriander
* 		1 tsp onion powder
* 		.5 tsp garlic powder
* 		.5 tsp shrimp extract powder
* 		.25 tsp cinnamon
* 		.125 tsp low heat cayenne
""")

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

st.subheader("Turkish Spice Blend")
st.write("""
* 		2 part cumin
* 		2 part garlic powder
* 		1 part ground coriander
* 		.25 part ground allspice
* 		.25 part chili flakes
""")

st.subheader("Tuscan Heat Spice Blend")
st.write("""
* 		4 parts dried basil
* 		2 parts dried rosemary
* 		2 parts dried oregano
* 		2 parts garlic powder
* 		1 part cayenne pepper [7.5 k (hu)]
* 		1 part ground fennel
""")
