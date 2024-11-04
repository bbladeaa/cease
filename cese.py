#!/usr/bin/python 
def open_file(): 
lines = [] 
with open("file.txt", "r") as f: 
for line in f.readlines() 
lines.append(line.strip("\n")) 
return lines
