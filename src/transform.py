enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"
flag = ""
raw = enc.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# first char is unicode shifted by 8 bits
# second char is unicode shifted by 8 bits + unicode of index + 1

# reverse
for i in range(len(enc)):
  flag += chr(ord(enc[i]) >> 8) # 
  flag += chr(ord(enc[i]) - (ord(flag[-1]) << 8))

print(flag)