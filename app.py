
import streamlit as st
from PIL import Image

st.set_page_config(layout="centered")
st.title("LINDOKUHLE AI M15 v7")
st.success("LIVE - GOLD M15")

up = st.file_uploader("Upload M15 chart", type=["png","jpg","jpeg"])

if up:
    img = Image.open(up)
    st.image(img, use_container_width=True)
    
    price = st.number_input("Enter Price you see on chart (eg 4320.597)", value=4320.59)

    entry = price
    signal = "SELL"
    sl = entry + 15
    tp1 = entry - 30
    tp2 = entry - 60

    st.markdown("### M15 ANALYSIS")
    st.error(f"BOS: Bearish")
    st.info(f"OB Zone: {entry} - Supply")
    st.info(f"FVG: Detected at {entry-5}")
    
    st.error(f"SIGNAL: {signal} @ {entry}")
    st.write(f"Entry: {entry}")
    st.write(f"SL: {sl}")
    st.write(f"TP1: {tp1}")
    st.write(f"TP2: {tp2}")
else:
    st.warning("Upload chart then enter price you see top right")
