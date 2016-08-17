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
    </body>\n\
</html>")
fo.close()

fo = open(script, "w")
fo.write("$(document).ready ( function(){\n\n\})")
fo = open(stylesheet, "w")
fo.close()







