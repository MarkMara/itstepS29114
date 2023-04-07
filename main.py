"""my_list = [1,2,3]
itertator = iter(my_list)
print(itertator)
print(next(itertator))
print(next(itertator))
print(next(itertator))
print(next(itertator))"""
# spysok = [1,2,3, 'hello']
# itertator = iter(spysok)
# while True:
#    try:
#        t = next(itertator)
#        print(t)
#    except:
#        StopIteration
#        break

'''spysok = [1,2,3, 'hello']
itrator = iter(spysok)
for elem in itrator:
        print(elem)
for elem in itrator:
    print(elem)'''
#class Counter:
#    def __init__(self, max_number):
#        self.i = 0
#        self.max_number = max_number
#
#    def __iter__(self):
#        self.i = 0
#        return self
#    def __next__(self):
#        self.i +=1
#        if self.i > self.max_number:
#            raise StopIteration
#        return self.i

#count = Counter(5)
#for elem in count:
#    print(elem)

'''
L = [1,4,12,34,57]
res_L=[x*x for x in L]
print(res_L)

T = (11,23,45,13,78)
res_T=[x**2 for x in T]
print(res_T)

s = {2,4,6,1,2,4,9}
res_S=[5*t for t in s]
print(res_S)'''
#def Power3(value):
#    for i in range(value):
#        yield i*i*i
#
#for i in Power3(10):
#    print(i)
'''def getfloatvalues(value):
    t = 0
    while t<value:
        t=t+0.2
        yield t

for i in getfloatvalues(2):
    print(i)'''
#import random
#
#def getRandomValue(a,b,c):
#    for t in range(c):
#        yield random.randint(a,b)
#
#c = int(input('c = '))
#a = int(input('a = '))
#b = int(input('b = '))
#
#L=[]
#for i in getRandomValue(a, b ,c):
#    L = L +[i]
#
#print(L)

'''def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems {exc}')
        else:
            print(f'No problems')
    return checker

@checker
def calculate(expression):
    return eval(expression)

calculate('2+2')'''
#def cheker(*exc_types):
#    def checker(function):
#        def checker(*args, **kwargs):
#            try:
#                result = function(*args, **kwargs)
#            except (exc_types) as exc:
#                print(f'We have problems {exc}')
#            else:
#                print(f'No problems. Results - {result}')
#        return checker
#    return cheker
#
#@cheker(NameError, TypeError, SyntaxError)
#def calculate(expression):
#    return eval(expression)
#
#calculate('2+2')

'''import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')'''
#import logging
#logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
#                    format='We have next logging message:%(asctime)s:%(levelname)s -'
#                           '$(message)s')
#try:
#    print(10/0)
#except Exception:
#    logging.exception('Exception')
'''if 2+2==4:
    print('in fact 2+2 equals 4')'''
#assert 2+2 == 5, 'не правильний вираз'
'''def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _

    return result'''
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_)==bool or type(_)==float:
            result += _
        else:
            try:
                result+=float(_)
                continue
            except(ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except(ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except(ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except(ValueError, TypeError):
                pass
    return result