# -*- coding: utf-8 -*-
# @Author: FFF
# @Date:   2017-09-12 21:31:32
# @Last Modified by:   FFF
# @Last Modified time: 2017-09-12 21:58:36
# for循环打印1-100
# 
# for i in range(1,101):
# 	print(i);


# for循环打印1-100的和
# sum = 0;
# for i in range(1,101):
# 	sum+=i;
# print(sum);

# for循环输出矩形
# 

# for i in range(1,10):
# 	str = '☆';
# 	for j in range(1,10):
# 		str += '☆';
# 	print(str);	
# 	print('\n');
# 	
# 	
# 	for循环输出三角形
for i in range(1,10):
	str = '☆';
	for j in range(1,10):
		if j<i:
			str +='☆'
	print(str);		