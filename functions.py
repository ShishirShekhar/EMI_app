import streamlit as st

def calculate_emi(p, n, r):
    rv = r/100
    emi = p * rv * (1 + rv)**n / ((1 + rv)**n - 1)
    return emi

def calculate_outsanding_balance(p, n, r, m):
    rv = r/100
    balance = (p * (1 + rv)**n - (1 + rv)**m) / ((1 + rv)**n - 1)
    return balance

def get_value(e_type):
    if e_type == 'Fixed monthly repayment':
        p = st.sidebar.slider('Pricipal', 1000, 1000000)
        r = st.sidebar.slider('Rate of Intereset', 1, 15)
        n = st.sidebar.slider('Tenure', 1, 30)
        a = calculate_emi(p, n, r)
        f = 'p * r/100 * (1 + r/100)**n, ((1 + r/100)**n - 1)'
    else:
        p = st.sidebar.slider('Pricipal', 1000, 1000000)
        r = st.sidebar.slider('Rate of Intereset', 1, 15)
        n = st.sidebar.slider('Tenure(in yrs.)', 1, 30)
        m = st.sidebar.slider('Period after Outstanding is calculated(in mns.)', 1, n*12)
        a = calculate_outsanding_balance(p, n, r, m)
        f = 'p * (1 + r/100)**n - (1 + r/100)**m) / ((1 + r/100)**n - 1'
    return a, f
