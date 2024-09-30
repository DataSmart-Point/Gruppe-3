s = "pokemon"  # -> ["p", "o", "k" , ....]
s_arr = s.split()
print(s_arr)

for idx in range(len(s)):
    print(idx, s[idx])
