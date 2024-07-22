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

# 应用：图片_功能判断开关
ch = st.toggle('反色滤镜')
bw = st.toggle('黑白滤镜')
co = st.toggle('增强对比度')

message = ''
if ch:
    enhancer = ImageEnhance.Contrast(img)
    message += '反色' + ','
if bw:
    message += '黑白' + ','
if co:
    message += '增强对比度'
st.write('你将会得到一张', message, '的图片')