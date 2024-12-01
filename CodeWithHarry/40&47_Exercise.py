
# Write a python program to translate a message into secret code language. use the rules below to translate normal english into secret code language.

# Coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end 
# Now append three random character at the starting and the end 
# else:
# Simply reverse the staring 

# Decoding:
# If the word contains less then 3 character, revers it
# else:
# Remove 3 random character from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to cade or decode


st = input("Enter the message: ")
words = st.split(" ")
coding = input("1for Coding and 2 for Decoding")
coding = True if (coding=="1") else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "abc"
            r2 = "xyz"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
            

else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3] 
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))












