#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import SimpleHTTPServer
import SocketServer

fo = open("index.html", "w")

project = "projectName here"
stylesheet = "styles.css"
script = "functions.js"

fo.write("<!DOCTYPE html>\n\
<html>\n\
    <head>\n\
        <meta charset=\"UTF-8\">\n\
        <title>"+project+"</title>\n\
        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n\
        <script src="+script+"></script>\n\
        <link rel=\"stylesheet\" type=\"text/css\" href=\""+stylesheet+"\">\n\
    </head>\n\
    <body>\n\
      <h2>Big Text</h2>\
      <div class=\"myClass\"</div>\
    </body>\n\
</html>")
fo.close()

fo = open(script, "w")
fo.write("$(document).ready ( function(){    \n//logic goes here\nconsole.log(\"Hello World!\");\n})")
fo = open(stylesheet, "w")
fo.write("h2 {\ncolor: red}\n.myClass {\nbackground-color: blue;\nheight: 100px;\nwidth: 100px;\nposition: absolute;\nleft: 50%;\nright: 50%\n}")
fo.close()







