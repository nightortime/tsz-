'''单选框_挑战'''
import streamlit as st

# 单项选择框st.radio()
choice = st.radio(
    '选择：',
    ['选项1', '选项2', '选项3'],
    captions=['这是第一个选项', '这是第二个选项', '这是第三个选项']
)

# 如何创建单选框？
# 单选框中的两个必填参数分别是？都有什么作用？
# captions参数的作用是？

# 挑战：根据选项显示对应的颜色
st.write('----')
color = st.radio(
    '选择：',
    ['red', 'green', 'blue'],
    captions=['红色', '绿色', '蓝色']
)
message = ''
if color == 'red':
    message = '选择了红色'
elif color == 'green':
    message = '选择了绿色'
elif color == 'blue':
    message = '选择了蓝色'
st.write(message)