'''勾选框_应用'''
import streamlit as st

# 滑动条st.slider()
cb = st.checkbox('勾选选项')
if cb:
    st.write('选项被勾选', cb)

# 如何创建勾选框？
# 勾选框更适合单选还是多选？
# 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？

# 挑战：多选题结构实现，前两项为正确选项，后两项为错误选项
st.write('----')
st.write('这道题选什么？')
cb1 = st.checkbox('1正确答案')
cb2 = st.checkbox('2正确答案')
cb3 = st.checkbox('3错误答案')
cb4 = st.checkbox('4错误答案')
l = [cb1, cb2, cb3, cb4]
if st.button('确认答案'):
    if cb1 == True and cb2 == True and cb3 == False and cb4 == False:
        st.write('回答正确')
    else:
        st.write('回答错误')