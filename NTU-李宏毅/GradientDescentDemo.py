import matplotlib.pyplot as plt

# y_data = b + w * x_data
# L(w,b) = Σ(𝑦𝑛 - (b+w*𝑥𝑛))^2 n=1..10
x_data = [338., 333., 328. , 207. , 226. , 25. , 179. , 60. , 208., 606.]
y_data = [ 640. , 633. , 619. , 393. , 428. , 27. , 193. , 66. , 226. , 1591.]

# 1. (Randomly) Pick an initial value w0,b0
# 2. 𝑤1 ← 𝑤0 − 𝜂 * 𝜕𝐿/𝜕𝑤|𝑤=𝑤0,𝑏=𝑏0 ; 𝑏1 ← ...
b = -120
w = -4
lr = 0.000001  # learning rate
iteration = 100000

b_hist = [b]
w_hist = [w]
for i in range(iteration):
    w_grad = 0.0
    b_grad = 0.0
    for n in range(len(x_data)):
        w_grad += 2.0 * (y_data[n] - (b + w*x_data[n])) * (-x_data[n])
        b_grad += 2.0 * (y_data[n] - (b + w*x_data[n])) * -1.0
    b = b - lr * b_grad
    w = w - lr * w_grad

    b_hist.append(b)
    w_hist.append(w)
print(b, w)
plt.plot(b_hist, w_hist)
plt.show()
