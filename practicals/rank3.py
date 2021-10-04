import sys

#reads in a freq list from a file 
freq = []
fd = open('freq.txt', 'r')

for line in fd.readlines():
	line = line.strip('\n')

	(f, w) = line.split('\t')
	freq.append((int(f), w))

rank = 1
min = freq[0][0]
ranks = []

#output a ranked frequency list
for i in range(0, len(freq)):
	if freq[i][0] < min:
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))
	#to a stdout
#wondering which print function is preferable? I thought it was len(ranks) because its a list but idk
for i in ranks:
	print(i)
	#for i in range(len(ranks)):
		#print(ranks[i])



