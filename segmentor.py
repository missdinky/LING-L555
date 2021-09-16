#segmentor
import sys
#input text 
text = sys.stdin.read().lower()
text2 = text.replace('. ', '.\n')
print(text2)

