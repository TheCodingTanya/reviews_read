import time


data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:  
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')


# 文字計數
start_time = time.time()
wc = {}  # word_count字典功能
for d in data: # 清單中每個留言
    words = d.split() # 這樣split就不會出現空字串, split('')就會出現空字串
    for word in words: # 讀取清單中一個一個字
        if word in wc: #如果這字有在字典出現過
            wc[word] += 1
        else:
            wc[word] = 1  # 新增新key進字典裡    

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Tanya'])

while True:
    word = input('請問你想查甚麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')




# good = [1 for d in data if 'good' in d]
# print(good)


# bad = ['bad' in d for d in data]
# print(bad)

# bad = []
# for d in data:
#     bad.append('bad' in d)