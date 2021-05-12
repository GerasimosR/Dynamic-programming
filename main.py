import time
from editDistanceTopDown import editDistanceTD
from editDIstanceBottomUp import editDistanceBU

str1 = "cacdbd"
str2 = "ltcabbdb"
start = time.time()
d = editDistanceTD(str1, str2, len(str1), len(str2))
end = time.time()
print("Time consumed in working: ", end - start)
print(d)

start = time.time()
d = editDistanceBU(str1, str2, len(str1), len(str2))
end = time.time()
print("Time consumed in working: ", end - start)
print(d[len(str1)][len(str2)])
