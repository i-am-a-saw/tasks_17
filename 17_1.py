f = open('17.txt')
s = [int(x) for x in f]

k, maxs = 0,0

for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if (s[i] <= 150 and s[j] <= 150):
            k += 1
            maxs = max(maxs, s[i] + s[j])
print(k, maxs)
