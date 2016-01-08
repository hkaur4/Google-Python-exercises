#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename,'rU') 
  name_data = f.read()
  year_data= re.search(r'Popularity\sin\s(\d\d\d\d)', name_data)
  if not year_data :
    print ' no year found '
    sys.exit(1)
  name_year=year_data.group(1)  
  #print 'year :'
  #print name_year
  tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',name_data)
  #print 'tuples'
  #print tuples
  dict_name = {}
  for a,b,c in tuples :
    #print a + ' boy name: ' + b + ' , girl name : ' +  c
    if b not in dict_name :
      dict_name[b] = a
    if c not in dict_name :
      dict_name[c] = a  
  #print dict_name   
  lst_names = sorted(dict_name.keys())  
  result_names_sorted = []
  result_names_sorted.append(name_year)
  for name in lst_names :
    #print name + " : " + dict_name[name]
    result_names_sorted.append(name + ' ' + dict_name[name])
  #print result_names_sorted  

  return result_names_sorted  
  

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary :
    f = open('summary_file.txt','w')
  for filename in args:
    name = extract_names(filename)
    if summary:
      f.write('\n'.join(name) + '\n')
    else :
      print '\n'.join(name) + '\n'  

  
if __name__ == '__main__':
  main()
