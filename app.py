import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df=pd.read_csv('latlong.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title('India Household')
selected_state=st.sidebar.selectbox('Select a state',list_of_state)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary ,zoom=3,size_max=20,color_continuous_scale='Inferno',hover_name='District',
                                mapbox_style="carto-positron",width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3, size_max=20,
                                color_continuous_scale='Inferno', hover_name='District',
                                mapbox_style="carto-positron", width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True)
