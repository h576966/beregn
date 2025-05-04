import streamlit as st

def calculate_bmi():
    st.title("BMI Calculator")

    # Collect user input for weight, height, age, and activity factor
    weight = st.number_input("Vekt (kg)", min_value=1.0, value=70.0)
    height = st.number_input("Høyde (cm)", min_value=50.0, value=170.0)
    age = st.number_input("Alder (år)", min_value=0, value=30)
    activity_factor = st.number_input("Aktivitetsfaktor (1.2 - 2.5)", min_value=1.2, max_value=2.5, value=1.5)

    gender = st.selectbox("Kjønn", options=["Mann", "Kvinne"])

    if st.button("Beregn BMI"):
        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)

        # Calculate BMR using Mifflin-St Jeor formula
        if gender == "Mann":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        # Calculate Total Daily Energy Expenditure (TDEE)
        tdee = bmr * activity_factor

        # Display results
        st.subheader("Resultater:")
        st.write(f"BMI: {bmi:.2f}")
        st.write(f"BMR (Mifflin-St Jeor): {bmr:.2f} kcal/dag")
        st.write(f"TDEE: {tdee:.2f} kcal/dag")

# Call the function to run the BMI calculator
calculate_bmi()
