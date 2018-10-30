# arihmetic progression

n = int(input())
f = open('t.txt')
i = 0
res = []
for i in range(n) :
    string = f.readline()

    arr = []
    for elem in string.split() :
        arr.append(int(elem))

    a0 = arr[0]
    d  = arr[1]
    m = arr[2]

    j = 0
    sum = 0
    for j in range(m) :
        sum = sum + (a0 + j * d)

    res.append(sum)

f.close()
i = 0
for i in range(n) : 
    print(res[i], end = " ")

#--------------------------------------------   
#Body Mass Index

n = int(input())
#f = open('t.txt')
i = 0
res = []
for i in range(n) :
    string = input()#f.readline()

    arr = []
    for elem in string.split() :
        arr.append(float(elem))

    weight = arr[0]
    height = arr[1]
    
    BMI = weight / (height*height)

    if BMI < 18.5 : 
        res.append("under")
    elif (BMI >= 18.5 and BMI < 25.0) :
        res.append("normal")
    elif (BMI >= 25.0 and BMI < 30.0) :
        res.append("over")
    elif BMI >= 30.0 :
        res.append("obese")

#f.close()
i = 0
for i in range(n) : 
    print(res[i], end = " ")

#--------------------------------------------  
#Triangles or not

n = int(input())
f = open('t.txt')
i = 0
res = []
for i in range(n) :
    string = f.readline()

    arr = []
    for elem in string.split() :
        arr.append(float(elem))

    if ((arr[0] + arr[1] > arr[2]) and 
        (arr[0] + arr[2] > arr[1]) and 
        (arr[1] + arr[2] > arr[0]) and 
        arr[0] > 0 and  arr[1] > 0 and arr[2] > 0) :
        res.append(1)
    else :
        res.append(0)

f.close()
i = 0
for i in range(n) : 
    print(res[i], end = " ")

#-------------------------------------------- 
# Count 1776 : 1*1 + 7*2 + 7*3 + 6*4 = 60

# better practice : (in C/C++ it looks like ch -'0' for example).

n = int(input())
string = input()

res = []

j = 1

for elem in string.split() :
    num = int(elem)

    arr = []
    counter = 0
    digits = []
    while num > 0 :
        arr.append(num % 10)
        num = num // 10
        counter += 1
    
    i = 0
    j = 1
    sum = 0
    for i in range(counter) : 
        sum += arr[i] * counter
        counter -= 1
    
    res.append(sum)

i = 0
for i in range(n) : 
    print(res[i], end = " ")
 
#--------------------------------------------   
# Dice Rolling
# generate random integer between A and B with random x 
#between 0 and 1, which is useful in many games : 
# floor(x * (B - A) + A)

n = int(input())

res = []

j = 1

for i in range(n) :
    number = float(input()) #
    transformation1 = number * 6
    transformation2 = int(transformation1)
    transformation3 = transformation2 + 1

    res.append(transformation3)

i = 0
for i in range(n) : 
    print(res[i], end = " ")

#-------------------------------------------- 
# Average of an array

n = int(input())
f = open('t.txt')

res = []

j = 1

for i in range(n) :
    string = f.readline()#input()
    
    counter = 0
    arr = []
    for elem in string.split() :
        if int(elem) != 0 :
            arr.append(int(elem))
            counter += 1

    j = 0
    avg = 0.0
    for j in range(counter) :
        avg += arr[j] / counter
        
    if avg - int(avg) >= 0.5 :
        res.append(int(avg)+1)
    else :
        res.append(int(avg))

f.close()
i = 0
for i in range(n) : 
    print(res[i], end = " ")
    
#-------------------------------------------- 
# checksum - seed 113 limit 1000007

n = int(input())
#f = open('t.txt')

res = []

string = input()

arr =[]
for elem in string.split() :
    arr.append(int(elem))

seed = 113
limit = 10000007

result = 0
j = 0
for j in range(n) :
    result = (result + arr[j]) * seed 
    if result > limit :
        result = result % limit

print(result)

#-------------------------------------------- 
# reverse string

string = input()
i = 0
for i in range(len(string)) :
    print(string[len(string)-1-i], end = "")

#-------------------------------------------- 
# Array Counters
# how many such or another numbers in array

string = input()
arr = []
for elem in string.split() :
    arr.append(int(elem))
M = arr[0]
N = arr[1]

arr = []
string = input()
for elem in string.split() :
    arr.append(int(elem))

counter = []
i = 0
for i in range(N) :
    counter.append(0)

i = 0
for i in range(M) :
    counter[arr[i]-1] += 1


i = 0
for i in range(N) :
    print(counter[i], end = " ")

#-------------------------------------------- 
# Collatz Sequence
# если X четное (т.е. X mod 2 = 0) тогда
#    Xследующее = X / 2
# иначе
#    Xследующее = 3 * X + 1
# 15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 -> cycle 1 4 2 1 4 2 ...
# для заданного исходного X посчитать сколько шагов требуется чтобы дойти до 1.

n = input()
string = input()
res = []

counter = 0
arr = []
for elem in string.split() : 
    arr.append(int(elem))
    counter += 1

i = 0
for i in range(counter) :

    count = 0
    eggs = arr[i]
    while eggs > 1 :
        if eggs % 2 == 0 :
            eggs = eggs / 2
        else : 
            eggs = 3 * eggs + 1
        count += 1

    res.append(count)

i = 0 
for i in range(counter) : 
    print(res[i], end = " ")

#-------------------------------------------- 
# Linear Function
# find a b, knowing x1 y1 x2 y2
n = int(input())
f = open('t.txt')
res = []
i = 0 
for i in range(n) :
    string = f.readline() #input()
    arr = []
    for elem in string.split() :
        arr.append(int(elem))
    
    x1 = arr[0]
    y1 = arr[1]
    x2 = arr[2]
    y2 = arr[3]

    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1

    res.append([a,b])

f.close()
i = 0
for i in range(n) : 
    print('(', int(res[i][0]), ' ', int(res[i][1]), ')', sep="", end = " ")

#--------------------------------------------
# Modulo and time difference
# отправление: 3 Мая 17:08:30 - 1 0 0 4 
# прибытие:    8 Мая 12:54:15 - 2 4 34 43

n = int(input())
f = open('t.txt')
res = []
i = 0 
for i in range(n) :
    string = f.readline()#input()
    arr = []
    for elem in string.split() :
        arr.append(int(elem))

    date1 = 24*60*60*arr[0] + 60*60*arr[1] + 60*arr[2] + arr[3]
    date2 = 24*60*60*arr[4] + 60*60*arr[5] + 60*arr[6] + arr[7]

    result = date2 - date1

    s = result % 60
    result = result // 60
    m = result  % 60
    result = result // 60
    h = result % 24
    d = (result / 24)

    res.append([d,h,m,s])

f.close()
i = 0
for i in range(n) : 
    print('(', int(res[i][0]), ' ', int(res[i][1]), ' ', int(res[i][2]), ' ', int(res[i][3]), ')', sep="", end = " ")

#--------------------------------------------
# Modular Calculator
init = int(input())
f = open('t.txt')
i = 0 

string = f.readline()#input()
while string != "" :
    arr = []
    for elem in string.split() :
        if elem not in "+*%" :
            arr.append(int(elem))
        else :
            arr.append(elem)

    if arr[0] == "+" :
        init += arr[1]
    elif arr[0] == "*" :
        init *= arr[1]
    elif arr[0] == "%" :
        init = init % arr[1]
    string = f.readline()#input()

#--------------------------------------------
# Bubble Sort
# количество проходов по массиву
# суммарное количество обменов элементов

n = int(input())
string = input()

arr = []
for elem in string.split() :
    arr.append(int(elem)) 

change_counter = 0
count = 0
i = 1
j = 0

while i < n :
    count += 1
    exit_flag = 0
    for j in range(n-i) : 
        if arr[j] > arr[j+1] :
            t = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = t
            change_counter += 1
            exit_flag += 1

    if exit_flag == 0 : 
        break
    i += 1

print(count, change_counter)

#--------------------------------------------
#Greatest Common Divisor
#lcm(a, b) = a * b / gcd(a, b)

n = int(input())
f = open("t.txt")
res = []

for i in range(n) :
    string = f.readline()#input()
    arr = [int(elem) for elem in string.split() ]

    a = arr[0]
    b = arr[1]
    while a != b : 
        if a > b :
            a -= b
        else : 
            b -= a
    gcd = a
    lcm = arr[0] * arr[1] / gcd

    res.append([gcd, int(lcm)])
f.close()
for i in range(n) :
    print("(", res[i][0], " ", res[i][1], ")", sep = "", end = " ")

#--------------------------------------------
# Sort with Indexes

n = int(input())

string = input()

arr = [int(elem) for elem in string.split()]
ind = [k+1 for k in range(n)]

i = 1
while i < n :
    for j in range(n - i) : 
        if arr[j] > arr[j+1] :
            t = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = t
            tt = ind[j]
            ind[j] = ind[j+1]
            ind[j+1] = tt
    i += 1
 
for i in range(n) :
    print(ind[i], end = " ")

#------------------------------------------
# Square Root

n_tests = int(input())
f = open("t.txt")
res = []
for i in range(n_tests) :
    string = f.readline()
    arr = [int(elem) for elem in string.split() ]

    X = arr[0]
    N = arr[1]
    r = 1

    for i in range(N) :
        r = (r + X/r) / 2

    res.append(r)
    
f.close()
for i in range(n_tests) :    
    print(res[i], end = " ")

#------------------------------------------
# Bubble in Array

string = input()
arr = [int(elem) for elem in string.split()]

seed = 113
limit = 10000007

swip = 0
i = 0
while arr[i+1] != -1 :

    if arr[i] > arr[i+1] :
        t = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = t
        swip += 1
    i += 1
arr.pop()

result = 0
for i in range(len(arr)) :
        result = (result + arr[i]) * seed 
        if result > limit :
                result = result % limit

print(swip, " ", result, end = " ")

#-------------------------------------------
# Palindromes
n = int(input())
f = open('t.txt')
alph_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_low = "abcdefghijklmnopqrstuvwxyz"

res = []
for i in range(n) : 
    arr = []
    string = f.readline()#input()
    for j in range(len(string)) :
        if string[j] in alph_low or string[j] in alph_up :
            arr.append(string[j].lower())
    k = 0
    flag = 0
    while k < int(len(arr) / 2):   
        if arr[k] == arr[len(arr)-1-k] :
            flag += 1
        else :
            flag = 0
        k += 1
    if flag == int(len(arr) / 2) :
        res.append("Y")
    else :
        res.append("N")
for i in range(len(res)) : 
    print(res[i], end = " ")

#-------------------------------------------
# Rotate String
n = int(input())

# 3 forwhomthebelltolls -> whomthebelltollsfor
res = []
for i in range(n) : 
        s = input()
        arr = [elem for elem in s.split()]
        rotate_num = int(arr[0])
        string = arr[1]
        
        new_string = string[rotate_num:] + string[:rotate_num]
        res.append(new_string)

for i in range(len(res)) : 
        print(res[i], end = " ")

#------------------------------------------
# Neumann's Random Generator
# 4100 -> 8100 -> 6100 -> 2100 -> 4100

n = int(input())
string = input()
arr = [int(elem) for elem in string.split()]

res = []
for i in range(n) :
        iter_num = 0
        # 0
        num = arr[i]
        check_arr = [num]
        while 1 : 
                iter_num += 1
                num = num ** 2
                if num >= 1000 :
                        num = num // 100
                        num = num % 10000
                        if num in check_arr :
                                break
                        else : 
                                check_arr.append(num)
                elif num < 1000 and num >= 10 :
                        num = num // 100
                        if num in check_arr :
                                break
                        else : 
                                check_arr.append(num)
                elif num < 10 :
                        num = 0
                        if num in check_arr :
                                break
                        else : 
                                check_arr.append(num)
        res.append(iter_num)

for i in range(n) : 
        print(res[i], end = " ")

#------------------------------------------------------
# Fibonacci Sequence 
# find indexes of fibonacci numbers

n = int(input())
f = open('t.txt')
res = []
for i in range(n) :
        fib_num = int(f.readline())
        if fib_num == 0 :
                res.append(0)
        elif fib_num == 1 :
                res.append(1)
        else :
                fib0 = 0
                fib1 = 1
                fib_ind = 1
                while 1 : 
                        t = fib0
                        fib0 = fib1
                        fib1 = t + fib1
                        fib_ind += 1
                        if fib1 == fib_num :
                                res.append(fib_ind)
                                break
f.close()
for i in range(n) :
        print(res[i], end = " ")

#----------------------------------------------------
# Pythagorean Theorem

n = int(input())
res = []
for i in range(n) :
        string = input()
        arr = [int(elem) for elem in string.split()]
        c = arr[2]
        b = arr[1]
        a = arr[0]

        count = (arr[0] ** 2 + arr[1] ** 2) ** (1/2)
        print(count, c)

        if count == c :
                res.append("R")
        elif count > c :
                res.append("A")
        else :
                res.append("O")

for i in range(n) :
        print(res[i], end = " ")

#----------------------------------------------------
# Smoothing the Weather

n = int(input())
f = open('t.txt')
string = f.readline()
f.close()
arr_old = [float(elem) for elem in string.split()]
arr_new = [arr_old[0]]
i = 1
while i < n - 1 :
        a = float('{:.10f}'.format((arr_old[i-1] + arr_old[i] + arr_old[i+1]) / 3))
        arr_new.append(a)
        i += 1
arr_new.append(arr_old[len(arr_old)-1])

for i in range(n) :
        print(arr_new[i], end = " ")

#----------------------------------------------------
# Bicycle Race - km from a

n = int(input())

res = []
for i in range(n) :
        string = input()
        arr = [int(elem) for elem in string.split()] 
        t = arr[0] / (arr[1] + arr[2])
        res.append(float('{:.10f}'.format(arr[1] * t)))

for i in range(n) :
        print(res[i], end = " ")

#----------------------------------------------------
#Josephus Problem
# killing every 3rd soldier in army of N people

string = input()
nums = [int(elem) for elem in string.split()]
N = nums[0]
k = nums[1]

arr = [(i+1) for i in range(N)]
i = 0
counter = 1
while len(arr) > 1 :
        if counter == k :
                arr.remove(arr[i])
                counter = 1
                i -= 1
        else : 
                counter += 1
        if i+1 == len(arr) : 
                i = 0
        else :
                i += 1

print(arr[0])

#----------------------------------------------------
# Counting Summ in the Bank
n = int(input())

res = []
for i in range(n) :
        string = input()
        arr = [int(elem) for elem in string.split()]
        S = arr[0]
        R = arr[1]
        P = arr[2]

        year_count = 0
        while S < R :
                S = float('{:.2f}'.format((100 + P) * S / 100))
                year_count += 1
        res.append(year_count)

for i in range(n) :
        print(res[i], end = " ")

#----------------------------------------------------
# Linear Congruential Generator

n = int(input())

res = []
for i in range(n) :
        string = input()
        arr = [int(elem) for elem in string.split()]
        A = arr[0]
        C = arr[1]
        M = arr[2]
        X0 = arr[3]
        N = arr[4] 

        Xcur = X0
        for j in range(N) : 
                Xnext = (A * Xcur + C) % M
                Xcur = Xnext

        res.append(Xnext)

for i in range(n) :
        print(res[i], end = " ")

#------------------------------------------------------
# Double Dice Roll

n = int(input())
N = 6

res = []
for i in range(n) :
        string = input()
        arr = [int(elem) for elem in string.split()]
        sum = 0
        
        arr[0] = arr[0] % N + 1
        arr[1] = arr[1] % N + 1

        sum = arr[0] + arr[1]
 
        res.append(sum)

for i in range(n) :
        print(res[i], end = " ")

#------------------------------------------------------
# Matching Brackets
# (a+[b*c] - {d/3}) - correct or not

n = int(input())

res = []
for i in range(n) : 
        string = input()
        fl_1 = 0
        fl_2 = 0
        fl_3 = 0
        fl_4 = 0

        scobs = []
        for k in range(len(string)-1) :
                if string[k] in "(){[}]<>" :
                        scobs.append(string[k])

        help = scobs[0]
        j = 0
        while j < len(scobs) : 
                if scobs[j] == "{" :
                        fl_1 += 1
                elif scobs[j] == "(" :
                        fl_2 += 1
                elif scobs[j] == "[" :
                        fl_3 += 1
                elif scobs[j] == "<" :
                        fl_4 += 1
                elif scobs[j] == "}" :
                        if help in "<([" and j != 0 or fl_1 == 0 :
                                fl_1 += 100
                        else :
                                fl_1 -= 1
                elif scobs[j] == ")" :
                        if help in "{[<" and j != 0 or fl_2 == 0  :
                                fl_2 += 100
                        else :
                                fl_2 -= 1
                elif scobs[j] == "]" :
                        if help in "<{(" and j != 0 or fl_3 == 0  :
                                fl_3 += 100
                        else :
                                fl_3 -= 1
                elif scobs[j] == ">" :
                        if help in "{[(" and j != 0 or fl_4 == 0  :
                                fl_4 += 100
                        else :
                                fl_4 -= 1
                help = scobs[j]
                j += 1
                
        if fl_1 == 0 and fl_2 == 0 and fl_3 == 0 and fl_4 == 0 :
                res.append("1")
        else :
                res.append("0")
        
for i in range(n) :
        print(res[i], end = " ")

#------------------------------------------------------
# Bit Count

n = int(input())
string = input()

arr = [int(elem) for elem in string.split()]

res = []
for i in range(n) :
        
        y = arr[i]

        if y < 0 :
                flag = 1
        else : 
                flag = 0
        x = abs(y)
        bits1 = []
        while x >= 2 :
                bits1.append(x % 2)
                x = int(x / 2)
        bits1.append(x)
        
        j = 0
        sum = 0
        while j < len(bits1):
                if bits1[j] == 1 :
                        sum += 1
                j += 1
        
        if flag == 0 : 
                res.append(sum)
        else : 
                bits2 = []
                for j in  range(32-len(bits1)) :
                        bits2.append(0)
                for j in range(len(bits1)) :
                        bits2.append(bits1[len(bits1)-1-j])
                for j in range(len(bits2)) :
                        if bits2[j] > 0 :
                                bits2[j] = 0
                        else :
                                bits2[j] = 1
                if bits2[len(bits2)-1] == 0 : 
                        bits2[len(bits2)-1] = 1
                else :
                        j = 0
                        while bits2[len(bits2)-1-j] != 0 :
                                 bits2[len(bits2)-1-j] = 0
                                 j += 1
                        bits2[len(bits2)-1-j] = 1
                j = 0
                sum = 0
                while j < len(bits2):
                        if bits2[j] == 1 :
                                sum += 1
                        j += 1
                res.append(sum)

for i in range(n) :
        print(res[i], end = " ")

def count_bits(x):
    c = 0
    for i in range(32):
        c += (x & 1)
        x >>= 1
    return c

#------------------------------------------------------
# Caesar Shift Cipher
#The idea of the algorithm is simple. Each letter of the original text 
# is substituted by another, by the following rule:
#   - find the letter (which should be encrypted) in the alphabet;
#   - move K positions further (down the alphabet);
#   - take the new letter from here;
#   - if "shifting" encountered the end of the algorithm, continue from its start.

string = input()
n = int(string[0])
k = int(string[2])
m = 26 - k 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = []
for i in range(n) :
        string = input()
        s = ""
        for elem in string :
                if elem.isalpha() :
                        ind = alphabet.index(elem)
                        counter = 0
                        if ind > k - 1 : 
                                index1 = 25 - ind
                                index2 = m - index1
                                s = s + alphabet[index2-1]
                        else : 
                                s = s + alphabet[ind + m]
                else :
                        s = s + elem
                        if elem == "." :
                                break
        res.append(s)

for i in range(n) :
        print(res[i], end = " ")

#------------------------------------------------------
# Triangle Area


