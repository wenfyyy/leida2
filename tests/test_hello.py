import os, sys

if os.path.exists("answers"):
    sys.path.append("answers")
else:
    sys.path.append("problems")
import hello


def test_hello():
    assert hello.hello_world() == "Hello, world!", "应当输出 'Hello, world!'"
