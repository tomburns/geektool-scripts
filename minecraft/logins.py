#!/usr/bin/env python

import optparse
import sys
import re

def main():
  p = optparse.OptionParser()
  p.add_option('--filter', '-f', default="logins")
  options, arguments = p.parse_args()
  
  print options("filter")

def logins():
  for line in sys.stdin:
    match = re.search('^(20..-..-.. ..:..:..) \[INFO\] ([A-Za-z0-9]+)\[?.*(logged in|lost.*$)', line)
    if match:
      raw = re.sub('[()\',]', '', str(match.group(1,2,3)))
      print raw

