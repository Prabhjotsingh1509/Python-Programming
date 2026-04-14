import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[1,2,3,4,5]

plt.plot(x,y) #Line plot
plt.title("Line chart")
plt.xlabel("X Values")
plt.ylabel("Y values")
plt.show()


plt.bar(x,y) #bar chart
plt.title("Bar chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

plt.hist(x)
plt.title("Histogram")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()