str1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str2=""
i=0
str2+=str1[i-1]+str1[i+1:i-1]+str1[i]
print(str2)