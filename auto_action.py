# import sell_tracing
import best_analysis

# url = "economy", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&FetchSize=80&PageNumber=" # 경제경영
# url = "humanities", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001019&sumgb=06&FetchSize=80&PageNumber=" # 인문
url = "ebiz", "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025011&sumgb=06&FetchSize=80&PageNumber=" # 인터넷 비즈니스
best_analysis.yes24(url)
