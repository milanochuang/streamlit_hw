# from bixin import predict

# if __name__ == '__main__':
#     from snownlp import SnowNLP
# # 文本
#     text = u'有夠令人討厭！'
# # 分析
#     s = SnowNLP(text)
# # 输出情绪为积极的概率
#     print(s.sentiments)

import streamlit as st
from snownlp import SnowNLP

st.title('中文情感分類器')
st.write('這是中文情感分類器，請在下方輸入任意文字')
st.image("dora.png")
test_str = st.text_input('請在這裡打上任意文字')
result = SnowNLP(test_str)
st.markdown('你的分數是 **{}**'.format(result.sentiments))
