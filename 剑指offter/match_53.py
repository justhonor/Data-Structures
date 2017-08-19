#!/usr/bin/python
# coding:utf-8
##
# Filename: FindGreatestSumOfSubArray_53.py
# Author  : aiapple
# Date    : 2017-08-18
# Describe: 剑指offter NO.53
#           
# 		请实现一个函数用来匹配包括'.'和'*'的正则表达式。
#   模式中的字符'.'表示任意一个字符，而'*'表示它前面的
#   字符可以出现任意次（包含0次）。 在本题中，匹配是指字
#   符串的所有字符匹配整个模式。
#  
#   例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
##
################################################
def match(s,pattern):
	if len(s)==0 and pattren==0:
		return True

	if len(s)>0 and len(pattern)==0:
		return False

	if len(pattern)>0 and pattern[1]=='*':
		# len(s)数组边界控制
		if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):
			# 匹配成功 s[0]==pattern[0] a-->a* s+1 pattern 不变
			# 匹配成功 pattern[0]=='.'  a-->.* 忽略
			return match(s[1:],pattern) or match(s,pattern[2:])
		else:
			# 匹配不成功 a-->b* 忽略 b*
			return match(s,pattern[2:])

	# 后面一位不是* 的匹配成功
	if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):
		return match(s[1:],p[1:])

	return False