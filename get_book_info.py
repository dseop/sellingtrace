from pandas import DataFrame as df
import crawling as cr

# 서지 정보만 빨리 뽑아내고 싶을 때, url만 입력해서 뽑아낼 때 사용!

### URL 정보 ###
t_list = []
t2_list = []
a_list = []
pu_list = []
d_list = []
pr_list = []
sp_list = []
info_list = []
page_list = []
weight_list = []
size_list = []
cate_list = []
review_list=[]

def mak_url_list(code_list) :
    url_list = []
    for code in code_list :
        url_list.append("http://www.yes24.com/Product/Goods/"+code)
    return url_list

def yes24(url_list) :
    for url in url_list :
    #url = url_list[0]
        print('present url: %s' %url)
        tmp_par = cr.makepar(url)
        t_list.append(tmp_par.find('h2', 'gd_name').text) # 도서명
        if tmp_par.find('h3', 'gd_nameE') is None : # 부제
            t2_list.append('')
        else :
            t2_list.append(tmp_par.find('h3', 'gd_nameE').text)
        #a_list.append(tmp_par.find('span', 'gd_auth').find_all('a')[0].text) #공저자 다 포함시킬 수 있는걸로 변경?
        a_list.append(tmp_par.find('span', 'gd_auth').get_text(' ', strip=True)) #.replace(' 저','')
        pu_list.append(tmp_par.find('span', 'gd_pub').text) #출판사
        d_list.append(tmp_par.find('span', 'gd_date').text.replace('년 ','-').replace('월 ','-').replace('일','')) #출간일
        pr_list.append(int(tmp_par.find_all('em', 'yes_m')[0].text.replace('원','').replace(',',''))) #tmp_par.find_all('em', 'yes_m') = 정가 할인가 전부 찾을때
        if tmp_par.find('span','gd_sellNum') is None : sp_list.append(0)
        else : sp_list.append(tmp_par.find('span','gd_sellNum').get_text(' ',strip=True).split(' ')[2]) #셀링포인트
        tmp_info = " ".join(tmp_par.find('tbody','b_size').find_all('td')[1].text.split(' | '))
        a = tmp_info.replace('쪽','').replace('g','').replace('mm','').split(' ') #쪽무게판형
        page_list.append(a[0])
        # print(len(a))
        if len(a) < 3:
            weight_list.append('')
            size_list.append(a[1])
        else :
            weight_list.append(a[1])
            size_list.append(a[2])
        # get cate
        tmp_list = []
        for tmp in tmp_par.find('div','gd_infoSet infoSet_txtCont').find_all('li') :
            cate = tmp.get_text(strip=True).split('>') # 전체 카테
            #de_cate = cate[2]+'>'+cate[3]
            tmp_list.append(cate[-1])
        cate_list.append(", ".join(tmp_list))
        #
        if tmp_par.find('span','gd_reviewCount').find('em') is None :
            review_list.append('0')
        else :
            review_list.append(int(tmp_par.find('span','gd_reviewCount').find('em').text)) #리뷰수

    raw_data = df({'제목': t_list,
                   '부제' : t2_list,
                   '저자': a_list,
                   '출판사': pu_list,
                   '출간일': d_list,
                   '가격': pr_list,
                   '지수': sp_list,
                   '쪽': page_list,
                   '무게': weight_list,
                   '판형': size_list,
                   '분류': cate_list,
                   '리뷰수': review_list,
                   'URL': url_list})
    return raw_data

# 부제
# 지음 | 쪽 | 원 from 알라딘
def aladin() :
    url_list = """https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=117994090
https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=116524331
https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=118873240&start=slayer
https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=116048223&start=slayer""".split('\n')
    for url in url_list :
        tmp_par = cr.makepar(url)
        t = tmp_par.find('a','Ere_bo_title').text
        if tmp_par.find('span','Ere_sub1_title') is None : t2 = ''
        else : t2 = tmp_par.find('span','Ere_sub1_title').text.replace('- ','')
        a = tmp_par.find('li','Ere_sub2_title').a.text+' 지음'
        n = tmp_par.find('div','conts_info_list1').find_all('li')[1].text
        p = tmp_par.find('div','Ritem').text
        print(t)
        print(t2+'\n'+a+' | '+n+' | '+p)

# main
