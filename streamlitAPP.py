# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Config functions
st.set_page_config(page_title='Grp 3: The NFT-alyzer', page_icon=':dollar')

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

st.markdown(hide_menu_style, unsafe_allow_html=True)

# Page layout
first = st.container()
dataset = st.container()
interactive_viz = st.container()
last = st.container()


# First bin
with first:
    st.title('The NFT-alyzer')
    NFT_header_image = Image.open('images/NFTgw.jpg')
    st.image(NFT_header_image)

# Dataset bin
with dataset:
    # Red Green Highlighting Function
    def color_df(val):
        if val > 0.145:
            color = 'green'
        else:
            color = 'red'
        return f'background-color: {color}'
    st.header('The Dataset')
    df = pd.read_csv('final_nft_data_v2.csv', index_col=0)
    st.dataframe(df.style.applymap(color_df, subset=['Compound Score']))
    st.markdown('* **VADER Sentiment Analysis:** Using VADER we analyze all the #NFT tweets and extract the Compuond Score, Positive Score, Neutral Score, and Negative Score.')

    
# Interactive Visualization bin
with interactive_viz:
    st.header('The Top and the Not')
    st.subheader('Top NFT Collections based on Compound Score')
    st.text('La creme de la creme')
    
    sel_col, disp_col = st.columns(2)

    comp_score_value = sel_col.slider('How many collections with top Compound Scores would you like to see?', min_value=0, max_value=100, value=5, step=5)

    comp_score = pd.DataFrame(df['Compound Score']).head(comp_score_value)
    st.bar_chart(comp_score)


    st.subheader('NFT Collections with the highest Negative Score')
    st.text('Likely best to steer clear of these projects...')
    
    sel_col, disp_col = st.columns(2)

    neg_score_value = sel_col.slider('How many of the collections with the highest Negative Scores would you like to see?', min_value=3, max_value=25, value=1, step=1)

    neg_score = pd.DataFrame(df['Negative Score'].sort_values(ascending=True).head(neg_score_value))
    st.bar_chart(neg_score)



    st.subheader('NFT Collections with the largest Volume in the past 7 days')
    st.text('#wagmi')
    
    sel_col, disp_col = st.columns(2)

    volume_value = sel_col.slider('How many of the collections with top Volume would you like to see?', min_value=3, max_value=25, value=3, step=1)

    volume_score = pd.DataFrame(df['Negative Score'].sort_values(ascending=False).head(volume_value))
    st.bar_chart(volume_score)


    st.subheader('NFT Collections with the largest number of sales in the past 7 days')
    st.text('Selling like hot-cakes!')
    
    sel_col, disp_col = st.columns(2)

    sales_value = sel_col.slider('How many of the collections with top number of sales would you like to see?', min_value=3, max_value=25, value=3, step=1)

    sales_score = pd.DataFrame(df['Sales (7d)']).sort_values(by='Sales (7d)', ascending=False).head(sales_value)
    st.bar_chart(sales_score)

# Last bin
with last:
    NFT_footer_image = Image.open('images/NFTp.jpeg')
    st.image(NFT_footer_image)
