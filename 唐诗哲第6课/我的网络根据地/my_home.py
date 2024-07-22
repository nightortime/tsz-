'''我的主页'''
import streamlit as st
from PIL import Image
import os
import datetime
import time

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '我的图片格式转换'])
info = """
工作室名字：夜暗time\n
根据地用户：个人使用、分享后所有人可见\n
根据地用途：工具分享、单词收集、综合主站\n
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区、图片格式转换\n
现有模块改进灵感：智慧词典进度条\n
原创模块：图片格式转换\n
原创模块一句话功能介绍：将图片格式转为GIF格式\n
"""
    
def page_1():
    '''我的兴趣推荐'''
    st.write('### :blue[网络根据地]')
    st.write(info)
    st.image('aduan_天象奇景.jpg')
    tab1, tab2, tab3 = st.tabs(["起风了", "告白气球", "童话"])
    with tab1:
        st.audio('起风了.mp3')
    with tab2:
        st.audio('告白气球.mp3')
    with tab3:
        st.audio('童话.mp3')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 2, 0, 1))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
    
def page_3():
    '''我的智能词典'''
    st.write('## 智能词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
        
    with open('check_out_times.txt', 'r', encoding='utf_8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    word = st.text_input('## :red[请输入要查询的单词]')
    if word in words_dict:
        roading = st.progress(0, '开始查询')
        for i in range(1, 101, 1):
            time.sleep(0.01)
            roading.progress(i, '正在查询中'+str(i)+'%')
        roading.progress(100, '查询完毕！')
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            '''字典键值对遍历'''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
            
        st.write('查询次数:', times_dict[n])
        if word == 'balloon':
            st.audio('告白气球.mp3')
            st.balloons()
        elif word == 'snow':
            st.snow()
        elif word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')
                    ''')
     
def page_4():
    '''我的留言区'''
    d = datetime.datetime.now()
    year, month, day, week = d.year, d.month, d.day, d.weekday()
    weeks = ["一", "二", "三", "四", "五", "六", "天"]
    date = f"{year}年{month}月{day}日 星期{weeks[week]}"
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf_8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☔'):
                st.write(i[1]+date+': '+i[2])
        elif i[1] == '编程猫':
            with st.chat_message('✨'):
                st.text(i[1]+date+': '+i[2])
    '''新增留言内容'''
    name = st.selectbox('我是......',['阿短', '编程猫'])
    new_message = st.text_input('想要说的话......')
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2]  + '\n'
            message = message[:-1]
            f.write(message)
    
def page_5():
    '''我的图片格式转换'''
    st.write(":sunglasses:图片格式转换小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        convert_to_gif(file_name, file_name.split(".")[0]+".gif")

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    
def convert_to_gif(input_file, output_file,size = (0,0)):
    # 打开并加载图像文件
    image = Image.open(input_file)
    gif_image = Image.new("RGBA", image.size)
    gif_image.paste(image)
    if size != (0,0):
        gif_image = gif_image.resize(size)
    # 保存GIF图像
    gif_image.save(output_file, "GIF")



if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的图片格式转换':
    page_5()
