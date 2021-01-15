import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt


@st.cache
def read_data() -> pd.DataFrame:
    data = pd.read_csv('titanic.csv')
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    st.sidebar.title("Streamlit Demo")
    st.sidebar.markdown("Das ist eine Demo der WepApp Library Streamlit")
    st.header("Das ist ein Streamlit Header")
    st.markdown('> Und das ist ein Beispiel für Markdown-Formattierung in Streamlit')

    st.markdown('___')
    st.header('Displaying pandas dataframes (Titanic Dataset):')
    df = read_data()
    cols = df.columns.to_list()
    selected_cols = st.multiselect("Columns to show", cols, default=cols[0:-1])
    st.dataframe(df[selected_cols])

    st.markdown('___')
    st.header('Lets display a histogram using a streamlit.selectbox')
    selectbox_options = df.select_dtypes('number').columns.to_list()
    selectbox = st.selectbox(label='Select column', options=selectbox_options)

    fig, ax = plt.subplots(1, 1)
    bins = min([20, len(df[selectbox].unique())])
    hist_ax = df.hist([selectbox], ax=ax, bins=bins, grid=False)
    plot = st.pyplot(fig)

    st.markdown('___')
    st.header('Lets try buttons and radios')

    col1, col2 = st.beta_columns(2)

    with col1:
        radio = st.radio('Choose greeting:', options=['Hi', 'Hello', 'Hola'])

    with col2:
        button = st.button('Greeting')
        if button:
            st.markdown(radio)

    st.markdown('___')
    st.header('Celebrate!')

    button = st.button('Cheer!')
    if button:
        st.balloons()
