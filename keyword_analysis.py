from konlpy.tag import Kkma
from konlpy.tag import Okt

from collections import Counter


def tag_counter(newpos, ntags=50) :
    count = Counter(newpos)
    # Counter객체를 생성하고 참조변수 pos할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    return return_list

kkma = Kkma()
def get_tags_kkma(text, ntags=100):  # ntags 50 = top 50
    pos = kkma.pos(text)
    # pos = twit(text)
    # pos = kkma.nouns(text) # 명사 분리 성능 떨어짐

    # pos 함수를 통해서 text에서 명사만 분리/추출 12.13
    newpos = []
    for temp in pos :
        if temp[1]=='NNG' : # NNG 항목만 분리
            newpos.append(temp)

    count = Counter(newpos)
    # Counter객체를 생성하고 참조변수 pos할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.

    print(return_list)
    return return_list

okt = Okt()
def get_tags_okt(text, ntags=500):  # ntags 50 = top 50

    # newpos = okt.nouns(text) # 아래를 요약
    pos = okt.pos(text)

    # pos 함수를 통해서 text에서 명사만 분리/추출 12.13
    newpos = []
    for temp in pos:
        if temp[1] == 'Noun':  # NNG 항목만 분리
            newpos.append(temp)
    count = Counter(newpos).most_common(ntags) # most_common 을 걸면 리스트와 된다!

    c_list = []
    for i in count:
        c_list.append([i[0][0], i[1]])

    #for n, c in count.most_common(ntags):
    #    temp = {'tag': n, 'count': c}
    #    return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return c_list

text=input('한글 입력\n')
get_tags_kkma(text)