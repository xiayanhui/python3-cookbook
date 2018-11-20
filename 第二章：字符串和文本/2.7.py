#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import re

# 最短匹配模式，这个问题一般出现在需要匹配一对分隔符之间的文本的时候(比如引号包含的字符串)
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# 当在模式中的*操作符后面加上?修饰符这样就使得匹配变成非贪婪模式，从而得到最短的匹配
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
"""
这一节展示了在写包含点(.)字符的正则表达式的时候遇到的一些常见问题。
在一个模式字符串中，点(.)匹配除了换行外的任何字符。
然而，如果你将点(.)号放在开始与结束符(比如引号)之间的时候，
那么匹配操作会查找符合模式的最长可能匹配。
这样通常会导致很多中间的被开始与结束符包含的文本被忽略掉，并最终被包含在匹配结果字符串中返回。
通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
"""
