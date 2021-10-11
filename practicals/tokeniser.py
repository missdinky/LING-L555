import sys

text2 = sys.stdin.readlines()

#separate punctuation from the text with spaces
for line in text2:
	a = 0
	for c in "',.:])(":
		line = line.replace(c, " " + c + " ")
	#split the spaces into new lines
	tokens = line.split(" ")
	#print each item in the tokens list on separate line
	for item in tokens:
		if item.strip() == '':
			continue
		print("%d\t%s"%(a, item) + "\t"*8)
		a = a + 1




			

