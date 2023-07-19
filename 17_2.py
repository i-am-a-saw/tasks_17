f = open('17.txt')
s = [int(x) for x in f]

summ, count = 0, 0

for i in range(len(s)):
    if s[i] % 2 == 0:
        count += 1
        summ += s[i]

sr_ar = summ / count

for j in range(len(s)):
    s[j] = abs(s[j])

k, mins = 0, 10**10

for i in range(len(s) - 1):
    if (len(str(s[i]))==4 and len(str(s[i+1]))!= 4) or (len(str(s[i]))!=4 and len(str(s[i+1]))== 4):
        k += 1
        if (s[i] + s[i+1]) < mins and (s[i] + s[i+1]) > sr_ar:
            mins = s[i] + s[i+1]

print(k, mins)
