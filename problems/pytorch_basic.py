# pytorch 可以说是目前最流行的深度学习框架之一，本练习题主要是为了熟悉 pytorch 的基本操作。
import torch


# 随机生成一个 m*n，n*p 的矩阵，计算两个矩阵的乘积，要求数据类型为 double
def problem_1(m, n, p):
    A = torch.rand(m, n, dtype=torch.double)
    B = torch.rand(n, p, dtype=torch.double)
    C = torch.randn(m, p, dtype=torch.double)
    return A, B, C


# 利用最小二乘法给出 f(x) = ||Ax - y||^2 的最优解
# 其中 A 是一个 m*n 的矩阵，y 是一个 m*1 的向量，x 是一个 n*1 的向量
def problem_2(A, y):
    x = torch.zeros((A.shape[1], 1))
    return x


# 利用梯度下降法求 f(x) = ||Ax - y||^2 的最优解
# 梯度为 f'(x) = 2 * A.T @ (Ax - y)
# x = x - lr * f'(x)
def problem_3(A, y):
    lr = 1e-1
    x = torch.randn((A.shape[1], 1))
    for _ in range(2000):
        # write your code here
        pass
    return x


# 利用梯度下降法求 f(x) = ||Ax - y||^2 的最小值
# 使用 torch 的自动微分功能
# 本题直接给出答案，供参考，不计分
def problem_4(A, y):
    lr = 1e-1
    x = torch.randn((A.shape[1], 1), requires_grad=True)
    for _ in range(2000):
        f = torch.norm(A @ x - y) ** 2
        f.backward()
        with torch.no_grad():
            x.sub_(lr * x.grad)
            x.grad.zero_()
    return x.detach()


if __name__ == "__main__":
    A, B, C = problem_1(3, 4, 5)
    print(f"A={A}")
    print(f"B={B}")
    print(f"C={C}")

    A = torch.randn(200, 3) / 10
    y = A @ torch.tensor([1, 1, 1], dtype=torch.float32).reshape(-1, 1)
    print(f"least squares: {problem_2(A, y).T}")
    print(f"gradient descent: {problem_3(A, y).T}")
    print(f"gradient descent with autograd: {problem_4(A, y).T}")
