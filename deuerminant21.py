a = [[5,8,5],[3,7,4],[1,8,9]]
for i in range(3):
	print(*a[i])
m = a[0][0]
print()
print('i j a m')
for i in range(3):
	for j in range(3):
		if a[i][j] > m:
			m = a[i][j]
			print(i, j, a[i][j], m)
