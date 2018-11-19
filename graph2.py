import matplotlib.pyplot as plt

left=[1,2,3,4,5]

height=[10,24,36,7,50]

label=['one','2','3','4','5']

plt.bar(left,height, tick_label = label, width=0.5,color=['red','green','yellow','blue','black'])

plt.xlabel("X Axis")
plt.ylabel("y Axis")
plt.title("my first graph")
plt.show()