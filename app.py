import streamlit as st

def largest_number(num1,num2,num3):
  if num1 > mum2:
    if num1 > num3:
      return num1
    else:
      return num3
  else:
    if num3 > num2:
      return num3
    else:
      return num2

def main():
    st.title("Largest Number")

    num1 = st.number_input("Input first number")
    num2 = st.number_input("Input second number")
    num3 = st.number_input("Input third number")

    if st.button("Find Largest Number"):
        largest = largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
