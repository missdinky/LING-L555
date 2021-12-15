import sys
import statistics

import epitran as ep
import re
epi = ep.Epitran('fra-Latn')

column_1 = [] #word
column_2 = [] #t
column_3 = [] #final_pho
column_4 = [] #guess
column_5 = [] #gender

#USE sed 199q fr_lieux2.txt 
#or USE sed 1000q real_nouns.txt

for line in sys.stdin.readlines(): 
	row = line.split('\t')
	row[1] = epi.transliterate(row[0])
	column_2.append(row[1])
	column_1.append(row[0])
	column_5.append(row[4].strip())
#print(new_lines)


#gender map
gender = {}
#setting values and keys
#masculine endings
gender['\u0303'] = 'un'
#^all nasal vowels
gender['ø'] = 'un'
gender['o'] = 'un'
gender['ɛ'] = 'un'
gender['u'] = 'un'
gender['a'] = 'un'
gender['y'] = 'un'
for v in ['a', 'u', 'i', 'e', 'ɛ', 'ɑ', 'o', 'œ']:
	gender[v+'\u0303'] = 'un'
gender['ʒ'] = 'un'
gender['m'] = 'un'
gender['f'] = 'un'
gender['ʀ'] = 'un'
gender['g'] = 'un'
gender['k'] = 'un'
gender['b'] = 'un'

#feminine endings
gender['i'] = 'une'
gender['z'] = 'une'
gender['n'] = 'une'
gender['v'] = 'une'
gender['j'] = 'une'
gender['d'] = 'une'
gender['s'] = 'une'
gender['ɲ'] = 'une'
gender['ɔ̃'] = 'une'
gender['ʃ'] = 'une'

#ambiguous endings
gender['p'] = 'amb'
gender['e'] = 'amb'
gender['t'] = 'amb'
gender['l'] = 'amb'


column_3 = []
for word in column_2:
	#make transcribed word into list of tokens
	#tokens = word.split()
	#find last character in x
	if word == '':
		column_3.append(word)
		continue
	final_pho = word[-1]
	if final_pho == '\u0303':
		final_pho = word[-2:]
	column_3.append(final_pho)
#print(final_phonemes)

for (noun, t, pho, real_gender) in zip(column_1, column_2, column_3, column_5):
	guess = '_'
	if noun.isupper() == True:
		guess = 'un'
	elif pho in gender:
		guess = gender[pho]
	column_4.append(guess)
	print('%s\t%s\t%s\t%s\t%s'%(noun, t, pho, guess, real_gender))


#check accuracy	
true = 0
total = 0
for (guess, real_gender) in zip(column_4, column_5):
	if guess == real_gender:
		true += 1
	total += 1

#print(total)
#print(true)

percentage = 100 * float(true)/float(total)
print('Accuracy:' + str(percentage) + '%')

 


