#https://www.hackerrank.com/challenges/sparse-arrays/problem
n =int(input())
x=[]
for i in range(n):
	x.append(raw_input().strip())
m= int(input())
Q=[]
for i in range(m):
	Q.append(raw_input().strip())
for i in Q:
	print x.count(i)		
