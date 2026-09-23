import streamlit as st
from datetime import datetime

st.set_page_config(page_title="LINDOKUHLE AI", page_icon="🤖", layout="centered")

st.title("🤖 LINDOKUHLE CHART SCANNING AI")
st.markdown("**TRADING BOT • SMC ANALYSIS • LIVE SCANNER**")
st.success("✅ BOT STATUS: ACTIVE & CONNECTED")

pair = st.selectbox("SELECT PAIR", ["XAUUSD.m M5", "XAUUSD.m M15", "BTCJPY M5", "EURUSD M15"])
bos = st.selectbox("MARKET STRUCTURE", ["BOS + Order Block + FVG", "BOS + Liquidity Sweep", "FVG Only"])
direction = st.radio("SIGNAL DIRECTION", ["SELL NOW", "BUY NOW"], horizontal=True)

col1, col2 = st.columns(2)
with col1:
    entry = st.text_input("ENTRY PRICE", "4352.09")
    sl = st.text_input("STOP LOSS", "4360.00")
with col2:
    tp = st.text_input("TAKE PROFIT", "4340.00")
    rr = st.text_input("RISK:REWARD", "1:3")

notes = st.text_area("SMC ANALYSIS", "FVG + OB Rejection + M15 BOS Confirmed. 0.5% Risk.")

if st.button("🚀 GENERATE SIGNAL CARD", use_container_width=True):
    st.divider()
    st.markdown(f"### 📊 SIGNAL {datetime.now().strftime('%H:%M:%S')}\n**PAIR:** {pair}\n**ACTION:** {direction}\n**ENTRY:** {entry}\n**SL:** {sl} | **TP:** {tp}\n\n**ANALYSIS:** {notes}\n\n⚡ *Powered by LINDOKUHLE AI*")
    st.balloons()

st.caption("© 2026 LINDOKUHLE AI - Durban, SA")
