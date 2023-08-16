# -*- coding:utf-8 -*-
# @Time      :2020/4/20
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='tmp_debug',
    ext_modules=cythonize("sum_int.py"),
)
