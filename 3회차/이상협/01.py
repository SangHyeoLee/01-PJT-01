with open('data/fruits.txt', 'r' , encoding='utf-8') as f:
    lines = f.readlines()
    cnt = 0
    for i in lines:
        cnt += 1
    print(cnt)