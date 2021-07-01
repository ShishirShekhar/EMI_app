from functions import *

st.title('EMI Calculator')
e_type = st.sidebar.selectbox('EMI Type', ['Fixed monthly repayment', 'Outstanding Loan Balance'])
value, formula = get_value(e_type)
st.subheader(e_type)
st.markdown('## Formula used')
st.latex(formula)
st.write(f'Amount= {round(value, 2)}')
