# 國立政治大學語言所 110555010 莊昊耘
# https://milanochuang-streamlit-hw-app-mokxk9.streamlitapp.com

import streamlit as st
from snownlp import SnowNLP

st.title('中文分數評分')
st.write('我會幫你判斷這段中文的情感分數，請在下方輸入任意文字')
st.image("dora.png")
test_str = st.text_input('請在這裡打上任意文字')
if test_str:
    result = SnowNLP(test_str)
    st.markdown('你的分數是**{}** 分'.format(result.sentiments))
