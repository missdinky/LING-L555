import sys

nouns = []
tags = []
w_list = []
for line in sys.stdin.readlines():
	if '\t' not in line:
		continue
	row = line.strip().split('\t')
	pos = row[3]
	tags.append(pos)
	w = row[2]
	w_list.append(w)

#aligning tags and words 
#isolating the words whose tag is NC 
#(common noun)
#making a list of the nouns 	
for (pos, w) in zip(tags, w_list):
	if pos == 'NC':
		nouns.append(w)

real_nouns = []
#need a way to delete the numbers
for x in nouns:
	skip = False
	for c in x:
		if c in '0123456789':
			skip = True
	if skip:
		continue
	real_nouns.append(x)

#deleting duplicates of nouns
real_nouns = list(set(real_nouns))


#format with column for ipa
#and column for gender
print(*real_nouns, sep="\t_"*4 + "\n")
#print(len(real_nouns)) #2888

	