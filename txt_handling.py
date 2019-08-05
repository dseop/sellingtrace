import re

f = open("G:/공유 드라이브/비즈(팀만사용)/#세금재테크상식사전(2020)분권/원고_ver.d7_표X.txt", 'r')
d = f.read()
f.close()

len(re.findall('\n',d))
len(re.findall('\n\n',d))
len(re.findall('\n\n\n',d))
len(re.findall('\n\n\n\n',d))

wannafindword = '\n사례'
len(re.findall(wannafindword, d))

d2 = d.replace('','')

d2 = d2.replace('\n\n\n\n','#4줄바꿈')
d2 = d2.replace('\n\n\n','#3줄바꿈')
d2 = d2.replace('\n\n','#2줄바꿈')
d2 = d2.replace('\n','#줄바꿈')

d = d.replace('#4줄바꿈','\n\n\n\n')
d = d.replace('#3줄바꿈','\n\n\n')
d = d.replace('#2줄바꿈','\n\n')

f2 = open("G:/공유 드라이브/비즈(팀만사용)/#세금재테크상식사전(2020)분권/원고_ver.d7.txt", 'w')
f2.write(d2)
f2.close()