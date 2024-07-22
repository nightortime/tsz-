'''跳转按钮_应用'''
import streamlit as st

# 跳转按钮link_button()
st.link_button('百度首页', 'https://www.baidu.com/')

# 如何创建跳转按钮
# 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？

# 应用：兴趣推广_分享链接指引
st.write('----')
st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
if go == '我的贴吧':
    st.link_button('帮我盖楼', 'https://www.baidu.com/')
elif go == '我的bilibili':
    st.link_button('帮我一键三连', 'https://www.bilibili.com/')