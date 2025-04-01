import streamlit as st
import matplotlib.pyplot as plt
import utils

# Display previous transactions
df = utils.load_transaction_data()

# Pi Chart of all transactions displayed by category
if not df.empty:
    st.subheader('Transaction History:')
    st.dataframe(df)
    st.write('Spending by category')

    fig, ax = plt.subplots()

    df.groupby('Category')['Amount'].sum().plot(kind = 'pie', autopct = '%1.1f%%', ax = ax)
    st.pyplot(fig)
else:
    st.write('No recorded transactions.')
