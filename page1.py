import streamlit as st
st.title("ページ1です")
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 100,(20, 5)), columns = ("国語", "数学", "社会", "理科", "英語"))
st.write(df)

#棒グラフ
st.title("国語の成績")
st.bar_chart(df["国語"])

#棒グラフ
st.title("国語の成績")
st.line_chart(df["国語"])

#散布図
df["総合得点"] = df["国語"] + df["数学"] + df["理科"] + df["社会"] + df["英語"]
st.title("理科と数学の関係")
st.scatter_chart(df, x = "理科", y = "数学", size = "総合得点")

#散布図をMAP表示
st.title("東京都付近の散布図")
map_df = pd.DataFrame(
    np.random.rand(50,2)/(50, 50) + (35.68, 139.76),
    columns = ["lat", "lon"]
)
st.map(map_df)
st.write(map_df)

