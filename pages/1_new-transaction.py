import pandas as pd
import streamlit as st
import utils

st.title('Enter a New Transaction')

# Transaction input forms
with st.form('transaction_entry'):
    date        = st.date_input('Date')
    amount      = st.number_input('Amount', min_value = 0.00, format = '%0.2f')
    category    = st.selectbox('Category', ['Groceries', 'Take-out', 'Property', 'Entertainment', 'Transport', 'Other'])
    description = st.text_input('Description: ')
    submitted   = st.form_submit_button('Enter Transaction')

    if submitted:
        st.balloons()
        utils.add_transaction(date, amount, category, description)

