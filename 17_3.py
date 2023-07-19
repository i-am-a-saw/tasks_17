f = open('17.txt')
s = [int(x) for x in f]

def check(a):
    ch = 0
    nch = 0
    for numb in str(a):
        if numb in '13579':
            nch += 1
        else:
            ch += 1
    if nch == ch:
        return True
    return False
            

count, summ = 0, 0

for i in range(len(s)):
    if s[i] % 5 == 3:
        count += 1
        summ += s[i]

sr_ar = summ / count

k, minnumb = 0, 10**10

for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        numb1 = s[i] * 1000 + s[j] # 1 вариант номера: сначала 1-ое число, затем 2-ое
        if check(numb1) == True:
            k += 1
            if numb1 < minnumb and numb1 > sr_ar:
                minnumb = numb1
        
        numb2 = s[j] * 1000 + s[i]  # 2 вариант номера: сначала 2-ое число, затем 1-ое
        if check(numb2) == True:
            k += 1
            if numb2 < minnumb and numb2 > sr_ar:
                minnumb = numb2
            
print(k, minnumb)
