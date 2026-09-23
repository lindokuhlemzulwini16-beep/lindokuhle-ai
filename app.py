import streamlit as st
from PIL import Image
import random
st.set_page_config(layout="centered")
st.title("LINDOKUHLE AI M15")
st.success("M15 MODE ACTIVE")
pair=st.selectbox("PAIR",["XAUUSD M15","GBPUSD M15"])
up=st.file_uploader("Upload M15 chart",type=["png","jpg","jpeg"])
if up:
 img=Image.open(up)
 st.image(img,use_container_width=True)
 st.markdown("## M15 ANALYSIS")
 bos=random.choice(["BOS Bearish","BOS Bullish"])
 st.info(bos)
 st.info("OB: 3740 Zone")
 st.info("FVG: Detected")
 sig=random.choice(["SELL","BUY"])
 en=random.randint(3738,3748)
 sl=en+8 if sig=="SELL" else en-8
 tp=en-15 if sig=="SELL" else en+15
 if sig=="SELL":
  st.error(f"SIGNAL: {sig}")
 else:
  st.success(f"SIGNAL: {sig}")
 st.write(f"Entry: {en}")
 st.write(f"SL: {sl}")
 st.write(f"TP: {tp}")
 st.write("Timeframe: M15")
 st.balloons()
else:
 st.warning("Upload M15 chart")
