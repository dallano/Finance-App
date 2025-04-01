import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Transaction Storage file
TRANSACTION_CSV_FILE = 'transactions.csv'
TRANSACTION_COLUMNS  = ['Date', 'Amount', 'Category', 'Description']
# Profile Storage File
PROFILE_CSV_FILE = 'profile.csv'
PROFILE_COLUMNS = ['Name', 'Income', 'Budget', 'Spending']


def load_transaction_data():
    try:
        return pd.read_csv(TRANSACTION_CSV_FILE)
    except FileNotFoundError as error:
        print(f'Error occured: {error}')
        return pd.DataFrame(columns = TRANSACTION_COLUMNS)


def load_profile_data():
    try:
        return pd.read_csv(PROFILE_CSV_FILE)
    except FileNotFoundError as error:
        print(f'Error occured: {error}')
        return pd.DataFrame(columns = PROFILE_COLUMNS)


def add_transaction(date, amount, category, description = ''):
    df = load_transaction_data()
    new_transaction = pd.DataFrame([[date, amount, category, description]],
                                  columns = TRANSACTION_COLUMNS)
    df = pd.concat([df, new_transaction], ignore_index = True)
    save_data(df, TRANSACTION_CSV_FILE)


def add_profile(name, income, budget, spending = 0):
    df = load_profile_data()
    new_profile = pd.DataFrame([[name, income, budget, spending]],
                               columns = PROFILE_COLUMNS)
    df = pd.concat([df, new_profile], ignore_index = True)
    save_data(df, PROFILE_CSV_FILE)


def save_data(df, file):
    df.to_csv(file, index = False)
