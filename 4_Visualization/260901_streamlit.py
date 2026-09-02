import pandas as pd
import streamlit as st

st.set_page_config(page_title="자동차 데이터", layout="centered")

@st.cache_data
def get_data():
    data = pd.read_csv("cars.csv")
    return data

cars_df = get_data()

st.title("자동차 데이터")
st.markdown(
    "<p style='color:green; font-weight:bold;'>자동차 데이터 테이블</p>",
    unsafe_allow_html=True,
)

maker_list = sorted(cars_df["Manufacturer"].unique())
selected_maker = st.selectbox("제조사 선택", maker_list)

result_df = cars_df[cars_df["Manufacturer"] == selected_maker]

col_list = list(cars_df.columns)
selected_col = st.selectbox("정렬할 컬럼 선택", col_list)

order_choice = st.radio("정렬 순서 선택", ["오름차순", "내림차순"])
is_ascending = order_choice == "오름차순"

result_df = result_df.sort_values(selected_col, ascending=is_ascending)

st.dataframe(result_df, use_container_width=True)