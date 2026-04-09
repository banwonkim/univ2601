import matplotlib.pyplot as plt
data_1D = np.array([0.5, 0.6, 1, 1.5, 2.1, 3.1, 3.7, 4.2, 4.5, 4.8, 5.3, 5.6, 6.1, 6.3], dtype=np.float32)
data_label = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1], dtype=np.int16)
data_Y=np.array([0] * len(data_1D))
plt.scatter(data_1D, data_Y)
print(data_1D)

fn=lambda x:x*0.16-0.65
sigmoid=lambda x:1/(1+np.exp(-x))
line=np.array([fn(x) for x in data_1D])

print('idx\tx\tfn(x)\tY\tsigmoid')
for i,x in enumerate(data_1D):
    print(i,x,fn(x), data_label[i], sigmoid(fn(x)), sep='\t')
    data_Y[i]=int(sigmoid(fn(x))>0.5)
plt.scatter(data_1D, data_Y)
plt.scatter(data_1D, data_label-0.5)
plt.plot(data_1D, line)
plt.show()
