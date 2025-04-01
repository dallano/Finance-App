## ***************************************************************************************
# The following program was written for Python version: 3.12.7 and Pandas version: 2.2.2
#   The purpose of this file is to demonstrate the capability of both the author, as well
#   as pandas and streamlit.
#   Author: Dallan Atwood
## ***************************************************************************************
import streamlit as st
import matplotlib.pyplot as plt
import utils

transactionDF = utils.load_transaction_data()
profileDF     = utils.load_profile_data()

if not profileDF.empty:
    st.title('Home Page')

    # Create variables for values from dataframe
    income = profileDF['Income'][0]
    budget = profileDF['Budget'][0]
    spending = transactionDF["Amount"].sum()
    savings = income - spending

    st.write(f'Welcome back, {profileDF['Name'][0]}!')
    st.write('### Monthly spending stats:')

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label = 'Income', value = income)
    col2.metric(label = 'Budget', value = budget)
    col3.metric(label = 'Spending', value = spending)
    col4.metric(label = 'Projected Savings', value = savings)

    # Draw graph if user has entered transactional data
    if spending:
        # Savings Graph
        fig, ax = plt.subplots()
        categories = ['Income', 'Budget', 'Spending', 'Savings']
        values = [income, budget, spending, savings]
        ax.bar(categories, values, color = ['green', 'orange', 'red', 'blue'])
        st.pyplot(fig)
    else:
        st.write('No spending history recorded.')
else:
    st.write('###Welcome to your new financial tracker!')
    st.write('##Let\'s setup your profile')

    with st.form('profile_entry'):
        name = st.text_input('Name:')
        income = st.number_input ('Monthly Income', min_value = 0.00, format = '%0.2f')
        budget = st.number_input('Budget', min_value = income, format = '%0.2f')
        submitted   = st.form_submit_button('Create User')

        if budget > income:
            print('Budget cannot be higher than your income.')
        elif submitted:
            utils.add_profile(name, income, budget)
            st.rerun()