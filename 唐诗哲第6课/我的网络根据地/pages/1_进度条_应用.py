'''进度条_应用'''
import streamlit as st
import time

# 进度条st.progress()
roading = st.progress(0, '开始加载')
for i in range(1, 101, 1):
    time.sleep(0.02)
    roading.progress(i, '正在加载'+str(i)+'%')
roading.progress(100, '加载完毕！')

# 如何创建组件？
# 创建组件之后如何调用组件实现效果？
# 两个参数的作用分别是？

# 应用：词典_单词记忆挑战
words_lst = ['fruit：水果', 'apple：苹果', 'banana：香蕉', 'orange：橘子']

words = st.progress(0, '准备开始单词记忆挑战！')
for i in range(4, 0, -1):
    time.sleep(3)
    words.progress(i*25, words_lst[-i])
time.sleep(3)
words.progress(0, '开始猜词吧！')
st.write('刚才出现的单词是？他们的意思是？')