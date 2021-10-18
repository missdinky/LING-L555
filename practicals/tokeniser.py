import sys

text2 = sys.stdin.readlines()
sent_id = 1
#separate punctuation from the text with spaces
for line in text2:
	if line.strip() == '':
		continue
	print('# sent_id = %d'%(sent_id))
	print('# text = %s'%(line.strip()))
	a = 1
	for c in "',.:])(":
		line = line.replace(c, " " + c + " ")
	#split the spaces into new lines
	tokens = line.split(" ")
	#print each item in the tokens list on separate line
	for item in tokens:
		if item.strip() == '':
			continue
		print("%d\t%s"%(a, item) + "\t_"*8)
		a = a + 1
	sent_id += 1
	print()
		