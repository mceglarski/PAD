import streamlit as st
import pandas as pd
import time


def ankieta():
    first_name = st.text_input("Enter your name", "First name")
    last_name = st.text_input("Enter your last name", "Last name")
    if st.button("Submit"):
        st.success(f'Data saved, hello {first_name} {last_name}')


def staty():
    data = st.file_uploader("Upload a dataset", type=['csv'])

    with st.spinner("Loading"):
        if data is not None:
            progress_bar = st.progress(0)
            for p in range(100):
                time.sleep(0.1)
                progress_bar.progress(p + 1)

            df = pd.read_csv(data)
            st.dataframe(df.head(15))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            column_names = df.columns.to_list()
            selected_column = st.multiselect("Select your plot", column_names)
            plot = df[selected_column]
            st.bar_chart(plot)
            st.line_chart(plot)


page = st.sidebar.selectbox('Menu', ['Ankieta', 'Staty'])
if page == 'Ankieta':
    ankieta()
else:
    staty()
