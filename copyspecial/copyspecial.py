#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands



def get_special_paths(dir):
  filenames = os.listdir(dir)
  filepaths = []
  for filename in filenames:
    match = re.search(r'__(\w+)__' , filename)
    if match:
      full_path  = os.path.join(dir, filename)
      abs_path = os.path.abspath(full_path) 
      filepaths.append(abs_path)
  #print filepaths  
  return filepaths

def copy_to(paths, dir) :
  for source_path in paths :
    shutil.copy(source_path, dir)  
  

def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print "Command to run:", cmd   
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


   
def main():
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
   
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  paths = [] 
  for directory_name in args :
    paths.extend(get_special_paths(directory_name))
    if todir:
      copy_to(paths,todir)
    elif tozip:
      zip_to(paths,tozip)  
    else :
      print '\n'.join(paths)  
    

  
if __name__ == "__main__":
  main()
