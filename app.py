import streamlit as st

def largest_number(a,b,c):
  if a > b:
    if a > c:
      return a
    else:
      return c
  else:
    if b < c:
      return c
    else:
      return b

st.title("Largest Number")
a = st.number_input("Input first number")
b = st.number_input("Input second number")
c = st.number_input("Input third number")
answer = largest_number(a,b,c)
st.write('Largest number is',answer)
