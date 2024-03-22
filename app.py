import streamlit as st
import psycopg2

def main():
    st.title('Crop Recommendation')

    n = st.number_input('Nitrogen', key="Nitrogen", format="%f", step=1)
    n = (n-0)/120
    p = st.number_input('Phosphorus', key="phosphrous", format="%f", step=1)
    p = (p-5)/140
    k = st.number_input('Potassium', key="potassium", format="%f", step=1)
    k = (k-5)/200
    Temperature = st.number_input('Temperature', key="temp", format="%f", step=1)
    Temperature = (Temperature-8.825674745)/34.84981831
    Humidity = st.number_input('Humidity', key="humidity", format="%f", step=1)
    Humidity = (Humidity-45.02236377)/54.95951224
    ph = st.number_input('pH', key="ph", format="%f", step=0.1)
    ph = (ph-4.507523551)/3.488325426
    Rainfall = st.number_input('Rainfall', key="rainfall", format="%f", step=1)
    Rainfall = (Rainfall-20.21126747)/228.6480311

    predict_button = st.button('Predict', key="predict_button")

    if predict_button:
        # Connect to the database
        conn = psycopg2.connect(
            database="pgml_9mrdvtwlup0tw77",
            user="u_r4i5xrjkii5eqag",
            password="rinkeoaj2qaptx5",
            host="02f7e6f1-1adb-4347-835a-02c74fcccb0e.db.cloud.postgresml.org",
            port="6432"
        )

        try:
            # Get a cursor
            cursor = conn.cursor()

            # Execute prediction query
            cursor.execute(
                "SELECT pgml.predict('Crop Recommendation'::text, "
                "ARRAY[%s, %s, %s, %s, %s, %s, %s]::FLOAT[])",
                (n, p, k, Temperature, Humidity, ph, Rainfall)
            )

            # Fetch the predicted value
            result = cursor.fetchone()[0]

            # Determine recommended fruit crop based on prediction result
            if result == 0:
                recommended_crop = 'Pomegranate'
            elif result == 1:
                recommended_crop = 'Banana'
            elif result == 2:
                recommended_crop = 'Mango'
            elif result == 3:
                recommended_crop = 'Grapes'
            elif result == 4:
                recommended_crop = 'Watermelon'
            elif result == 5:
                recommended_crop = 'Muskmelon'
            elif result == 6:
                recommended_crop = 'Apple'
            elif result == 7:
                recommended_crop = 'Orange'
            elif result == 8:
                recommended_crop = 'Papaya'
            elif result == 9:
                recommended_crop = 'Coconut'
            else:
                recommended_crop = result

            # Display the recommended fruit crop
            st.write(f'<div style="color: Green; font-weight: bold; font-size: 24px;">The recommended fruit crop is : {recommended_crop} </div>', unsafe_allow_html=True)

        except psycopg2.Error as e:
            st.error(f"An error occurred during prediction: {e}")
        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

if __name__ == '__main__':
    st.set_page_config(page_title="Crop Recommendation", page_icon="🌾")
    main()
