'''参考示例write_text'''
import streamlit as st
import pandas as pd

# 字符串
msg1 = '将要被打印的信息'
# 字符串改色 :颜色[内容]
msg2 = ':green[将要被打印的信息]'
# 使用pandas将字典转化为表格[表格页面daraFrame]
d = {
    '姓名': ['阿短', '编程猫', '同学A'],   # 第一列数据
    '学号': [1, 2, 3]
}
d = pd.DataFrame(d)
d.to_string(index=False)
# 数字
number = 12345


st.write(msg1)
st.write(msg2)
st.write(d)
st.write(number)