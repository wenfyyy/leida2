# 作业 1

## 1. 准备工作

### 1.1. 注册 GitHub 账号

前往[GitHub](https://github.com)注册账号，如果已有账号则跳过此步骤。

### 1.2. 安装并配置 VSCode

前往[下载](https://code.visualstudio.com/download)页面下载安装包，并安装，然后打开 VSCode。安装如下插件：

-   Python
-   Black Formatter
-   indent-rainbow
-   Jupyter
-   Markdown All in One
-   Pylance

最后，在 VSCode 中登录 GitHub 账号。

### 1.3. 安装并配置 Python

首先从[官网](https://docs.anaconda.com/free/miniconda/miniconda-install/)下载 miniconda 安装包，然后执行安装命令。

在终端运行`python`命令，如果出现类似下方的提示，则说明安装成功。

```shell
Python 3.12.2 | packaged by conda-forge | (main, Feb 16 2024, 20:54:21) [Clang 16.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

接着输入`quit()`退出 Python 环境，然后在命令行中输入

```shell
conda config --set show_channel_urls yes

cat <<'EOF' > ~/.condarc
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirror.nju.edu.cn/anaconda/pkgs/main
  - https://mirror.nju.edu.cn/anaconda/pkgs/r
  - https://mirror.nju.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirror.nju.edu.cn/anaconda/cloud
  pytorch: https://mirror.nju.edu.cn/anaconda/cloud
EOF
```

将 conda 镜像源设置为南大的镜像源，以加速下载。如有问题，请参考[Anaconda 软件仓库镜像使用帮助](https://mirror.nju.edu.cn/anaconda/)。

然后输入下方的命令安装本课程所需的包。

```shell
conda install pytest numpy pandas plotly nbformat
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

## 2. 学习 Git 基本操作

学会在 VSCode 中使用 Git 进行版本控制，从而提交作业，并在网页中查看得分情况。

## 3. 完成作业

本次作业包含的具体文件位于`problems`文件夹中，具体要求请查看对应的文件。

1.  `hello.py` 检验 Git 的基本操作学习情况
1.  `python_basic.py` 检验 Python 基础知识学习情况
1.  `pytorch_basic.py` 检验 PyTorch 基础知识学习情况
