'''单选框_应用'''
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

# 应用：游戏_数据模拟器
st.write('----')
level = st.radio(
    '选择游戏难度：',
    ['普通', '困难', '地狱'],
    captions=['怪物血量为100%,攻击力为100%', '怪物血量为200%,攻击力为150%', '怪物血量为300%,攻击力为200%']
)
hp = 100
damage = 10
if level == '困难':
    hp = 200
    damage = 15
elif level == '地狱':
    hp = 300
    damage = 20
st.write('怪物血量：', hp, '，怪物攻击力：', damage)