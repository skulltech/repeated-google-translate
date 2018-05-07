# repeated-google-translate
A script to translate a text repeatedly using Google Translate. For the keks and memes.

## What is this and how is this useful?!
This script uses the advanced mind of Google Translate to figure out the hidden meanings behind ordinary english text.
Inspired by the following _meme_-videos.

- [Gucci Gang but it's been Google translated over 500 times](https://youtu.be/HMReGXCtTiM)
- [Pumped Up Kicks but it's been Google translated](https://youtu.be/ZMR395zmT1k)

## Installation

Clone or download the `rgt.py` script.
The only requirement of this script is the `googletrans` library. Install it as follows

```console
$ pip3 install googletrans
```

## Usage

```console
sumit@HAL9000:~/repeated-google-translate$ python3 rgt.py -h
usage: rgt.py [-h] (-t TEXT | -f FILE) [-n NUM] [-o OUT]
              [-l LANGS [LANGS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Input text.
  -f FILE, --file FILE  File containing input text.
  -n NUM, --num NUM     Number of time to go through the languages.
  -o OUT, --out OUT     File to write output text into.
  -l LANGS [LANGS ...], --langs LANGS [LANGS ...]
                        ISO 639-1 codes of the languages to use.
```

A simple use-case can be as follows
```console
sumit@HAL9000:~/repeated-google-translate$ python3 rgt.py -t "There's vomit on his sweater already, mom's spaghetti"
[*] "There's vo..." but translated 50 times!

Nikel-spaghete water (water spaghetti nickel) is solved.
```

A more involved use-case which uses all the available CLI arguments.
```console
sumit@HAL9000:~/repeated-google-translate$ python3 rgt.py -t "There's vomit on his sweater already, mom's spaghetti" -n 10 -l de ko hi
[*] "There's vo..." but translated 30 times!

Your sweater is already spaghetti to celebrate your mother.
```
