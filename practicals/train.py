import sys

tags = []
words = []
a = 0
#read file line by line
for line in sys.stdin.readlines():
	if '\t' not in line:
		continue
	row = line.strip().split('\t')
	pos = row[3]
	tags.append(pos)
#print(tags) 
	
#counter for total number of tokens
	ws = row[1] 
	words.append(ws)
	a = a + 1
	
#matrix for words and tags
m_words = {}
#matrix for tags and frequency
m_tags = {}


#word -> tag
#this is just initializing so we are just setting everything to 0 
for (pos, word) in zip(tags, words):
	#if word is not in matrix
	if pos not in m_tags:	#if pos is not in tags, then the frequency is 0
		m_tags[pos] = 0
	if word not in m_words:
		m_words[word] = {}
	if pos not in m_words[word]:	#initialise tags to 0 
		m_words[word][pos] = 0
	m_tags[pos] += 1
	m_words[word][pos] += 1
print(m_tags, m_words)
	


