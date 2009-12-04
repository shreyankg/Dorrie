#!/usr/bin/python
import sys

file = sys.argv[1]
f = open(file)
print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
  xmlns:py="http://genshi.edgewall.org/"
  xmlns:xi="http://www.w3.org/2001/XInclude"
  py:strip="">
  '''
try:
    for lang in f:
        lang = lang.strip()
        if lang and not lang.startswith('#'):
            print '    <option value="' + lang + '" py:attrs="{\'selected\': lang == \'' + lang + '\' and \'selected\' or None}">' + lang + '</option>'
finally:
    f.close()
print '''</html>
'''
