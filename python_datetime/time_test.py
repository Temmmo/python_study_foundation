#! python3
import time
def calcProd():
    product = 1
    for i in range(1,50000):
        product = product* i
    return product
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate' % (endTime - startTime))

for i in range(3):
    print('Tick')
   # time.sleep(2)
    print('Tock')
   # time.sleep(2)

now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))








