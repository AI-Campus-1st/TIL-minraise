## 도전! 최대 & 최소 찾기(min & max 쓰지 않고!)

### 정답
```py
my_list = [3, 2, 10, 2, 4]

max_num = my_list[0]
min_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print('최대:', max_num)
print('최소:', min_num)
```