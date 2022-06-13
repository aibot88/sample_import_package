import sys
print('解释器导包路径',sys.path[0], sys.path[-1])

from test_package_name.fp.m2 import _subfp

# 该函数不能执行, 因为在第一行导入_subfp时出错
# 出错原因时在当前的__path__下, 解释器的导包路径中查找不到fp包. 
# 我们在本文件中使用test_package_name文件指定到fp包, 但是在m2.py文件中我们仅仅指定了fp包名, 不包含具体路径
print('fp 包上一层目录', _subfp)