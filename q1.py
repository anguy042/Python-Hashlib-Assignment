#AnnieNguyen
#PID:5777067

import hashlib

file = open("meaningful_words.txt","r")
for word in file : 
    word = word.strip('\n')
    x = (hashlib.sha256(word.encode("ascii", "ignore")).hexdigest())
    y ="69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7"

    if x == y:
        print ("The meaningful english word is : ",word)