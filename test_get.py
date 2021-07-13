import crawling as cr
import pyperclip

isbn_list = [
    9791160507386, 9791160507171, 9791165211387, 9791160500233, 9791160505177, 9791160502114, 9791160509182, 9791160505290, 9791160505627, 9791165214234, 9791160503975, 9791160508772, 9791160509557, 9791165211530, 9791160504620, 9791160504934, 9791165210557, 9791160506563, 9791160503395, 9791160502923, 9791165213077, 9791165212384, 9791160504316, 9791160501575, 9791165215798, 9791165215699, 9791165215347, 9791165215170, 9791165214487, 9791165213701, 9791165212629, 9791165210694, 9791160509625, 9791160508147, 9791160507836, 9791160507270, 9791160506952, 9791160505931, 9791160504422, 9791160501773
    ]

isbn_list = [9791160507171]
result_list = []
i = 0

for isbn in isbn_list:
    url = "http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode={0}&orderClick=LEa&Kc=".format(isbn)
    par_html = cr.makepar(url)
    title = par_html.find('h1', 'title').get_text(' ', strip=True)
    author = par_html.find('div', 'author').get_text(' ', strip=True)
    price = par_html.find('span', 'org_price').get_text(' ', strip=True)

    result_text = """
        {0}\n\n{1} | {2}\n\n{3}
    """.format(title, author, price, url)
    result_list.append(result_text)
    print(title+" ok! ({0}/{1})".format(i, len(isbn_list)))

join_text= "\n\n".join(result_list)
pyperclip.copy(join_text)