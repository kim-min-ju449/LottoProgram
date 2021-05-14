from random import sample

winnum = set()


def buyautolotto():
    '''정렬된 6개의 로또 번호 5개 조합을 생성'''
    lotto = []
    for i in range(5):
        num6 = set(sample(list(range(1, 46)), 6))
        lotto.append(num6)
    return lotto


def printnums(nums):
    '''시퀀스 수를 정렬해 출력'''
    for num in sorted(nums):
        print('%02d' % num, end=' ')
    print()


def printlotto(lotto):
    '''로또 복권 표와 같이 출력'''
    for i, item in enumerate(lotto):
        printnums(item)
    print()


def setwinlotto():
    '''전역 변수  winnum에 당첨 번호 정하기'''
    global winnum
    winnum = set(sample(list(range(1, 46)), 6))


def getwinner(lotto):
    '''5개의 로또 번호에서 각각 당첨번호 개수와 수를 출력'''
    for i, item in enumerate(lotto):
        print('%c' % (ord('A') + i), end=' ')
        win = winnum.intersection(set(item))
        if win:
            wincnt = len(win)
            print('당첨 번호 개수 %d, ' % wincnt, end=' ')
            printnums(win)
        else:
            print('꽝')

lotto = buyautolotto()
printlotto(lotto)
setwinlotto()
print('당첨 번호:', end = ' ')
printnums(winnum)
getwinner(lotto)