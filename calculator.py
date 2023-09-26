import streamlit as st
# Take user input
num1 = st.text_input("Enter the first number:")
num2 = st.text_input("Enter the second number:")
operation = st.radio("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# if (num1!="" and num2!=""):

if(num1!="" and num2!=""):
  # Perform the calculation
  if st.button("Calculate"):
      if operation == "Add":
          result = float(num1) + float(num2)
      elif operation == "Subtract":
          result = float(num1) - float(num2)
      elif operation == "Multiply":
          result = float(num1) * float(num2)
      elif operation == "Divide":
          result = float(num1) / float(num2)
      st.write("Result:", result)
