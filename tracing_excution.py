from wannatrace import tracing_sellingpoint
from wannatrace import tracing_sellingpoint_col

num = int(input('1 : all, 2 : 주식, : 3 : 세금, 4 : new excel, 5: 주식2, 6: 새 주소 추적\n'))

if num==1 :
    #tracing_sellingpoint(filename = 'wannatrace.xlsx')
    tracing_sellingpoint('주식시장조사용_yes.xlsx', '주식시장조사용_yes.txt')
    tracing_sellingpoint('세금 재테크 상식사전_tracing.xlsx', '세금_yes.txt')
    tracing_sellingpoint('세금_al.xlsx', '세금_al.txt')

if num==2 :
    tracing_sellingpoint('주식시장조사용_yes.xlsx', '주식시장조사용_yes.txt')

if num==3 :
    tracing_sellingpoint('세금 재테크 상식사전_tracing.xlsx', '세금_yes.txt')
    tracing_sellingpoint('세금_al.xlsx', '세금_al.txt')

if num == 4 :
    print("""규칙1 .xlsx 를 제외,\n규칙2  yes 또는 al을 집어넣어야 해당 사이트에서 크롤링""")
    #yes 또는 al을 알아서 판단할 수 있도록 만들어야 겠다
    yo = input()

if num == 5 :
    tracing_sellingpoint_col('주식시장조사용_yes_2.xlsx')

if num == 6 :
    input('새 주소 입력\n')


input()