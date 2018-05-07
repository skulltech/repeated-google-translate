# repeated-google-translate
A script to translate a text repeatedly using Google Translate. For the keks and memes.

## Installation

Clone or download the `rgt.py` script.
The only requirement of this script is the `googletrans` library. Install it as follows

```console
$ pip3 install googletrans
```

## Usage

```console
sumit@HAL9000:~/repeated-google-translate$ python3 rgt.py -h
usage: rgt.py [-h] (-t TEXT | -f FILE) [-n NUM] [-l LANGS [LANGS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Input text.
  -f FILE, --file FILE  File containing input text.
  -n NUM, --num NUM     Number of time to go through the languages.
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
