#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0



import sys
import codecs

# For the --count flag, function that counts how often each word appears in the text and prints:
# word1 count1
# word2 count2
# Print the above list in order sorted by word (python will sort punctuation to come before letters 
#	-- that's fine). Store all the words as lowercase, so 'The' and 'the' count as the same word.
def print_words(filename):
	my_dict = count_words(filename)
	for key in sorted(my_dict):
		print "%s, %s" % (key,my_dict[key])	
	return


# For the --topcount flag, implement a print_top(filename) which is similar to print_words() but which prints
# just the top 20 most common words sorted so the most common word is first, then the next most common, and so on.
def print_top(filename):
	mydict = count_words(filename)
	items = sorted(mydict.items())
	print 'top items'
  	for item in items[:20]:
  		print item[0], item[1] 	
  	sys.exit(0)	
  	return	

def count_words(filename):
	f = open(filename, 'r')
	mydict = {}
	for line in f:
		for word in line.split():
			word = word.lower()
			if word in mydict.keys():
				mydict[word] = mydict[word] + 1
			else :
				mydict[word] = 1
	return mydict			


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
