#!/usr/bin/python

import sys, re
neighbors = 1

def mapper(argv):

  line = sys.stdin.readline()
  pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
  while line:
      list_line = [each.lower() for each in pattern.findall(line)]
      for i in range(len(list_line)):
          start = max(i - neighbors, 0)
          end = min(i + neighbors, len(list_line) - 1)
          for j in range(start, end+1):
              if j == i:
                  continue
              else:
                  print("%s\t%s\t%d" % (list_line[i], list_line[j], 1))
      line = sys.stdin.readline()


if __name__ == "__main__":
  mapper(sys.argv)