# -*- coding: utf-8 -*-
import re
mixFile = open('from.txt', 'r')
mix = mixFile.read()
mixFile.close()
words = re.findall(r'[a-zA-Z]+', mix)
# print (words)
# print (words)
words.sort(key=str.lower)
A = open('to.txt', 'w')
A.write('\n'.join(words))
A.close()
