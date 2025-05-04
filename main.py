import streamlit as st
from bmi_calculator import calculate_bmi
from food_log import food_log_input

# Load custom CSS
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
def main():
    st.title("Beregn.no version 0.2")
    
    # Create tabs for different sections
    tabs = st.sidebar.radio("Select a section", ["Food Log", "BMI Calculator"])

    if tabs == "Food Log":
        food_log_input()
    elif tabs == "BMI Calculator":
        calculate_bmi()

if __name__ == "__main__":
    main()
