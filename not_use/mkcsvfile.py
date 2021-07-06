def add(fn, rd) : # 추가할 때
    rd.to_csv(fn, header=False, index=True, encoding='ms949', mode='a')

def mk(fn, rd) :
    rd.to_csv(fn, header=True, index=True, encoding='ms949')

def tag(fn, rd) :
    rd.to_csv(fn.replace('.csv','tag.csv'), header=['tag','count'], index=False, encoding='ms949')