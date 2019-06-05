password = 'a123456'
i = 3
while True:
    p = input('請輸入最多三次密碼:')
    if p == password:
        print('登入成功')
        break  # 逃出迴圈
    else:
        i = i-1
        print('請重新輸入密碼', i, '次機會')
    if i == 0:
        break
