from get_book_info import gbi_yes as gy

url_list = 'http://www.yes24.com/Product/Goods/75187118' #.split('\n') #이건 도서 개별 url
rd = gy(url_list)
rd.to_csv('getinfo.csv', header=True, index=True, encoding='ms949')
