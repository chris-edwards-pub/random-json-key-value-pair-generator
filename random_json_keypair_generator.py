import json
import random
import argparse

def load_words():
  with open('words_dictionary.json') as json_file:
     words = json.load(json_file)
  return words

def random_word(words):
  word = random.choice(list(words))
  return word

my_parser = argparse.ArgumentParser(description='Random Key:Pair Json Generator')

my_parser.add_argument('Pairs', metavar='pairs', type=int, help='number of key:value pairs to generate')
args = my_parser.parse_args()
pairs = args.Pairs

words = load_words()
key_value = dict()

for x in range(pairs):
  key = random_word(words)
  value = random_word(words)
  key_value.update({key: value})

jsonString = json.dumps(key_value)
print(jsonString)