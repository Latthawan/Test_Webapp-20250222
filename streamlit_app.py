import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.sidebar.subheader('Input')
Url_input = st.sidebar.text_input("GitHub CSV URL", "")

def convert_github_url(url):
    """แปลง GitHub URL ให้เป็น Raw URL"""
    if "github.com" in url and "blob" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")
    return url

if Url_input:
    st.subheader('Output')
    raw_url = convert_github_url(Url_input)
    st.warning(f'Converted Raw URL: {raw_url}') 

    try:
        df = pd.read_csv(raw_url, sep=None, engine='python', on_bad_lines='skip')
        st.write(df)

        # ใช้คอลัมน์สุดท้ายเป็นค่าที่จะ Groupby
        column_names = df.columns[-1]

        # ตรวจสอบว่า column_name เป็นประเภทข้อมูลที่สามารถใช้ groupby ได้
        if df[column_names].dtype == "object":
            df2 = df.groupby(column_names).mean()
            st.bar_chart(df2)
        else:
            st.warning("Column used for grouping must be categorical (not numerical).")

    except Exception as e:
        st.error(f"Error loading CSV: {e}")

else:
    st.subheader('Enter your input')
    st.error('👈 Awaiting your input!')

st.header('Sandbox')

# ใช้ .drop() อย่างถูกต้อง
if Url_input:
    try:
        # ดรอปคอลัมน์สุดท้าย (แต่ต้องเช็คก่อนว่ามีมากกว่า 1 คอลัมน์)
        if len(df.columns) > 1:
            x = df.drop(columns=[df.columns[-1]])
            st.write(x)
        else:
            st.warning("Not enough columns to drop.")
    except Exception as e:
        st.error(f"Error processing dataframe: {e}")

# `st.radio()` ต้องมีตัวเลือกที่ถูกต้อง
genre = st.radio(
    "Select a class value",
    ("Class A", "Class B", "Class C")  # ตัวเลือกตัวอย่าง
)

if genre == "Class A":
    st.write("You selected Class A.")
else:
    st.write(f"You selected {genre}.")
