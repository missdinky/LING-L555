import sys

#make a map to transcribe
transcriber = {}
#setting values and keys
transcriber['è'] = 'ɛ'
transcriber['an'] = 'ɑ̃'
transcriber['am'] = 'ɑ̃'
transcriber['on'] = 'ɔ̃'
transcriber['é'] = 'e'
transcriber['in'] = 'ɛ̃'
transcriber['im'] = 'ɛ̃'
transcriber['ï'] = 'j'
transcriber['qu'] = 'kw'
transcriber['q'] = 'k'
transcriber['en'] = 'œ̃'
transcriber['em'] = 'œ̃'
transcriber['j'] = 'ʒ'
transcriber['ch'] = 'ʃ'
transcriber['gn'] = 'ɲ'
transcriber['ç'] = 's'

# read input from tokeniser
# split lines and find words 
# print out line again

#tokeniser output
for line in sys.stdin.readlines():
	#split rows at tab and row[1] is word
	if '\t' not in line:
		print(line.strip())
		continue
	row = line.strip().split('\t')
	#print(row[1])
	
	token = row[1]
	#for character in TRANSCRIBER DICT
	for ch in transcriber:
		#replace tokens in row[1] 
		#from value to key
		token = token.replace(ch, transcriber[ch])
		if ch in "',.":
			token = token.replace(ch, " ")			

	#print(token)
	print('\t'.join(row[:9]) + '\tIPA=' + token)
		
#else:
#print('\t'.join(row) + 'IPA=')	
"""	
	for x in line.split('\t'):
		if x != ('%d') or ("\t_"):
			words.append(x)
			for x in words:
				print(x + '\n')
"""

			
			
	
	




		

	
	