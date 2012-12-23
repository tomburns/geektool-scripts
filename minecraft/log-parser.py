#!/usr/bin/env python

import optparse
import sys
import re

def filter_logins():
  for line in sys.stdin:
    match = re.search('^(20..-..-.. ..:..:..) \[INFO\] ([A-Za-z0-9]+)\[?.*(logged in|lost.*$)', line)
    if match:
      raw = re.sub('[()\',]', '', str(match.group(1,2,3)))
      print raw

def filter_chat():
  for line in sys.stdin:
    match = re.search('^(20..-..-.. ..:..:..) \[INFO\] <([A-Za-z0-9]+)>.*$', line)
    if match:
      print match.group(0)

def main():
  p = optparse.OptionParser()
  p.add_option('--filter', '-f', default="logins")
  options, arguments = p.parse_args()
  
  if options.filter == "logins":
    filter_logins()
  elif options.filter == "chat":
    filter_chat()
  

if __name__ == '__main__':
  main()
