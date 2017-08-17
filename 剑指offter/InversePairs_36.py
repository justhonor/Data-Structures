#!/usr/bin/python
# coding:utf-8
##
# Filename: InversePairs_36.py
# Author  : aiapple
# Date    : 2017-08-16
# Describe: 剑指offter NO.36
#
#		   在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#      输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
#      即输出P%1000000007
##
################################################

global Pnums
Pnums = 0
def CountPairs(leftdata, rightdata):
	global Pnums
	merged = []
	left = right = 0

	while left < len(leftdata) and right < len(rightdata):
		if leftdata[left] < rightdata[right]:
			merged.append(leftdata[left])
			left += 1
		else:
			Pnums += len(leftdata) - left
			merged.append(rightdata[right])
			right += 1

	if left == len(leftdata):
		for i in rightdata[right:]:
			merged.append(i)
	else:
		for i in leftdata[left:]:
			merged.append(i)

	return merged

def InversePairs(data):
	if len(data) <= 1:
		return data

	midle = len(data) / 2
	leftdata = InversePairs(data[:midle])
	rightdata = InversePairs(data[midle:])

	return CountPairs(leftdata,rightdata)

if __name__ == '__main__':
		
	d = [1,2,3,4,5,6,7,0]
	d = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
	InversePairs(d)
	# print Pnums

	m = [1,2,3,3,4,5,5,5,5,6,6,7,8,8,8,9]
	print m.count(8)
