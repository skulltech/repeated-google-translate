import argparse
import re
from googletrans import Translator



def rgt(text, langs, times):
	translator = Translator()

	translation = text
	for i in range(times):
		for lang in langs:
			translation = translator.translate(translation, dest=lang).text
		translation = translator.translate(translation, dest='en').text

	return translation


print(rgt('This food is very nice!', ['de', 'ko', 'la', 'ja', 'eo'], 5))
