url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber="
for i in [1,2,3,4] :
    tmp_url = url+('%s' %i)
    print(tmp_url)