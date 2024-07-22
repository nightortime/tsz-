'''跳转按钮_挑战'''
import streamlit as st

# 跳转按钮link_button()
st.link_button('百度首页', 'https://www.baidu.com/')

# 如何创建跳转按钮
# 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？

# 挑战：根据选项跳转到对应的网页
# https://www.baidu.com/
# https://www.bilibili.com/
st.write('----')
go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili'])
if go == '百度':
    st.link_button('跳转到'+go, 'https://www.baidu.com/')
elif go == 'bilibili':
    st.link_button('跳转到'+go, 'https://www.bilibili.com/')