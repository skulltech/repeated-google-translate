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
	parser = argparse.ArgumentParser(description='Translate text repeatedly using Google Translate. For the keks and memes.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-t', '--text', type=str, help='Input text.')
	group.add_argument('-f', '--file', type=str, help='File containing input text.')
	parser.add_argument('-n', '--num', type=int, help='Number of time to go through the languages.', default=10)
	parser.add_argument('-o', '--out', type=str, help='File to write output text into.')
	parser.add_argument('-l', '--langs', type=str, nargs='+', help='ISO 639-1 codes of the languages to use.', default=['de', 'ko', 'la', 'ja', 'eo'])
	args = parser.parse_args()

	if args.file:
		with open(args.file) as f:
			text = f.read()
	else:
		text = args.text


	print('[*] "{}..." but translated {} times!'.format(text[:10].strip(), args.num*len(args.langs)))
	result = rgt(text, args.langs, args.num)
	if args.out:
		with open(args.out, mode='w') as f:
			f.write(result)
		print('[*] Wrote output to {}'.format(args.out))
	else:
		print()
		print(result)



if __name__=='__main__':
	main()
