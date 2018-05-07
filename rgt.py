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

def main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-t', '--text', type=str, help='Input text.')
	group.add_argument('-f', '--file', type=str, help='File containing input text.')
	text = parser.add_argument('-l', '--langs', type=str, nargs='+', help='Languages to use.')
	args = parser.parse_args()


print(rgt('This food is very nice!', ['de', 'ko', 'la', 'ja', 'eo'], 5))
