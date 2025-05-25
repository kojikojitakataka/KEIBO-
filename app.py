# app.py
import streamlit as st
from scraper import get_race_data
from predictor import predict_race

st.title("競艇 出走表 & 予想アプリ")

# 入力フォーム
with st.sidebar:
    st.header("レース条件")
    jcd = st.selectbox("開催場（コード）", {
        "唐津 (04)": "04", "大村 (24)": "24", "福岡 (21)": "21", "住之江 (12)": "12", "平和島 (05)": "05"
    })
    date = st.text_input("日付（例: 20250525）", value="20250525")
    race_no = st.number_input("レース番号", min_value=1, max_value=12, value=1)

# 出走表取得
df = get_race_data(jcd, date, race_no)

if df is not None:
    st.subheader("出走表")
    st.dataframe(df)

    st.subheader("予想買い目")
    prediction = predict_race(df)
    st.write(prediction)
else:
    st.warning("出走表が取得できませんでした。日付・場コードをご確認ください。")
