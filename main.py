#file_path = 'Matvaretabellen.csv'

#df = pd.read_csv(file_path)

#print(df.columns)


import pandas as pd
import streamlit as st


from openai import OpenAI
client = OpenAI()

st.markdown("Skriv inn hva du har spist, så estimerer vi kalorier og proteiner.")
# Multiline input — each line = one meal
meals_input = st.text_area("Måltider", height=200) #food_input = st.text_area("")

if st.button("Beregn"):
    meals = [line.strip() for line in meals_input.splitlines() if line.strip()]

    if not meals:
        st.warning("Skriv inn minst ett måltid.")
        st.stop()

    # Compose GPT prompt
    formatted_meals = "\n".join(f"{i+1}. {meal}" for i, meal in enumerate(meals))
    prompt = f"""
        Du er en ernæringsassistent og skal beregne kalori- og proteininntak per måltid basert på informasjon fra Matvaretabellen.no.  
        Hvert måltid er på én linje nedenfor. Gi separate estimater for hvert måltid.  
        Oppsummer også totalen til slutt. Vær så presis som mulig.

        Svar på norsk, og bruk følgende format:

        Måltid 1: <antall> kcal, <antall> g protein  
        Måltid 2: ...  
        ...  
        Totalt: <antall> kcal, <antall> g protein

        Måltider:
        {formatted_meals}
        """
    try:
        

        response = client.responses.create(
            model="gpt-4.1",  
            input=prompt
            
        )
        #output = response.choices[0].message.content
        st.subheader("Estimert næringsinnhold:")
        st.write(response.output_text)
    except Exception as e:
        st.error(f"An error occurred: {e}")


