with open('check_out_times.txt', 'r', encoding='utf_8') as f:
        time_list = f.read().split('\n')
for i in range(len(time_list)):
    time_list[i] = time_list[i].split('#')
times_dict = {}
for i in time_list:
    time_list[i[0]] = [int(i[1])]
        