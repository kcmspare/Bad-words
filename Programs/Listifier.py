BadWordsList = open("words.txt")

with open('newlist.txt', 'w') as handle:
    for x in BadWordsList:
        for item in x.split(', '):
            handle.write(f'{item}\n')

###########################################

import re
pwdlist = open("list.txt")

with open("newlist", "w") as newlist:
    for x in pwdlist:
        x = re.search(r"(^\s\")(\w+)(\":\s+true,)", x).group(2)
        newlist.write(f"{x}\n")
        print(x)
