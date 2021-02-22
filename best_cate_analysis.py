from datetime import datetime
import crawling as cr
import connect_sheet as cs

today = datetime.today().date()
url = ("부동산_{0}".format(today),"http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06&FetchSize=80")
print(url)

# for i in [1, 2, 3, 4, 5] :
#     url+('&PageNumber=%s' %i)
#     par_url = cr.makepar(tmp_url)


# doc = cs.open_sheet("https://docs.google.com/spreadsheets/d/1RHrnaXg636ARmBnwzEVmTsgp721lMvqWZMyOKg3hnTA")
# doc.add_worksheet(title=url[0], rows="400", cols="10")
# worksheet = doc.worksheet(url[0]) # select sheet