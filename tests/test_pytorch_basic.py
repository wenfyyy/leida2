import os, sys
import torch

if os.path.exists("answers"):
    sys.path.append("answers")
else:
    sys.path.append("problems")
from pytorch_basic import problem_1, problem_2, problem_3


def test_problem_1():
    m, n, p = 100, 200, 500
    A, B, C = problem_1(m, n, p)
    assert torch.norm(A @ B - C) < 1e-3, "矩阵乘法不正确"


def test_problem_2():
    m, n = 100, 3
    A = torch.randn(m, n)
    x = torch.randn(n, 1)
    A = A / torch.norm(A, dim=0)
    y = A @ x
    x_hat = problem_2(A, y)
    assert torch.norm(x - x_hat) < 1e-3, "最小二乘解不正确"


def test_problem_3():
    m, n = 100, 3
    A = torch.randn(m, n)
    x = torch.randn(n, 1)
    A = A / torch.norm(A, dim=0)
    y = A @ x
    x_hat = problem_3(A, y)
    assert torch.norm(x - x_hat) < 1e-3, "最小二乘解不正确"
