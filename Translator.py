from googletrans import LANGUAGES
 
for Lang in LANGUAGES:
	print(f'{Lang} - {LANGUAGES[Lang]}')


print("Now choose your language support name and enter acc to it :-)")

from googletrans import Translator

sentence=str(input("say something re: "))

translator=Translator()

translated_sentence=translator.translate(sentence,src='en',des='tl')

print(translated_sentence.text)