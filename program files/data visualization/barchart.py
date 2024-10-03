import matplotlib.pyplot as plt
import random

x = [1,2,3,4,5]
y = [5,3,1,2,4]
l = []
for i in range(1,20):
    if i%2 == 0:
        l.append(6)
    else :
        l.append(4)
#plt.plot(l,marker ='H',ms=40)
# plt.scatter(x,y)


# l1=[]
# l2=[]
# for i in range(1,20,2):
#     l1.append(i)
# for i in range(1,20,3):
#     l2.append(i)
# plt.plot(l1,color="red")
# plt.plot(l2,color="green",marker="H",mec="blue")

l1=[]
l2 = []
for i in range(1,20,2):
    l1.append(i)
for i in range(20,-1,-1):
    l2.append(i)
plt.boxplot(l1,l2)

plt.show()
