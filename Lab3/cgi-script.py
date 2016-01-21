#!/usr/bin/env python

import os, json, cgi

print "Content-type: text/html"
print "Location: http://google.com/"
print
print "<HTML><BODY><h1>Hello world!</h1>"
print "<FORM method='POST'><INPUT name='x'></FORM>"

form = cgi.FieldStorage()
 
print "<P>X was: " + cgi.escape(str(form.getvalue('x')))

print "<P>"
print json.dumps(dict(os.environ), indent=4)
print "</P>"

print "</BODY></HTML>"