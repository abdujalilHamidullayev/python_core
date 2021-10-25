'''def ekranga_chiqar(xabar):
    print(xabar)

ekranga_chiqar(7**7)



def kvadrat_son(a):
    kvadrat=a**2
    return kvadrat
b=89
print(kvadrat_son(b))
'''
def sum_list(list1):
    yigindi=0
    for n in list1:
        yigindi+=n
    return yigindi


def mull_list(list2):
    kopaytma=1
    for n in list2:
        kopaytma*=n
    return kopaytma


sonlar=[5,1,4,2,3]
yigindi=sum_list(sonlar)
kopaytma=mull_list(sonlar)
print(yigindi)
print(kopaytma)
