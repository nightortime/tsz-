'''勾选框_应用'''
import streamlit as st

# 滑动条st.slider()
cb = st.checkbox('勾选选项')
if cb:
    st.write('选项被勾选', cb)

# 如何创建勾选框？
# 勾选框更适合单选还是多选？
# 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？

# 应用：宣传_互联网知识
st.write('----')
st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
cb1 = st.checkbox('易于管理')
cb2 = st.checkbox('效率高')
cb3 = st.checkbox('网速快')
cb4 = st.checkbox('安全性好')
l = [cb1, cb2, cb3, cb4]
if st.button('确认答案'):
    if True in l:
        st.write('其实都不对，答案是“历史问题，不得已而为之”')
    else:
        st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧！')