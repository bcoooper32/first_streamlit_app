import streamlit

streamlit.title('Health Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Smoothie Builder')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#put pick list here so users can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

