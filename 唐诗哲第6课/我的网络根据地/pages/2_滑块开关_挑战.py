'''滑块开关_挑战'''
import streamlit as st

# 滑块开关st.toggle()
my_open = st.toggle('开关')
if my_open:
    st.write('开启')
else:
    st.write('关闭')

# 如何创建组件？
# 创建组件之后如何通过判断实现效果？

# 挑战：创建两个开关，在两个开关下方显示开启情况
my_open1 = st.toggle('开关1')
my_open2 = st.toggle('开关2')
message = '打开开关：'
if my_open1:
    message += '开关1'
if my_open2:
    message += '开关2'
st.write(message)