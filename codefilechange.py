#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import os
import shutil
import re
import sys

def convert( filename, in_enc = "GBK", out_enc="UTF-8" ):
    shutil.copyfile(filename, filename + '.bak')

    # read the file
    try:
        content = open( filename ).read()
    except :
        print (filename)
    # convert the concent
    try:
        new_content = content.decode( in_enc ).encode( out_enc )
        #write to file
        open( filename, 'w' ).write( new_content )
    except :
        print(" error... ")
        
def explore( dir ):
    for root, dirs, files in os.walk( dir ):
        for file in files:
            if file.lower().endswith('.java'):
                path = os.path.join( root, file )
                print("convert " + path,
                convert( path ))
                print(" done")

def process_bak_files(action='restore'):
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith('.java.bak'):
                source = os.path.join(root, f)
                target = os.path.join(root, re.sub('\.java\.bak$', '.java', f, flags=re.IGNORECASE))
                try:
                    if action == 'restore':
                        shutil.move(source, target)
                    elif action == 'clear':
                        os.remove(source)
                except Exception as e:
                    print (source)

def main():
    if len( sys.argv ) > 1 :
        path = sys.argv[1]
        if os.path.isfile( path ):
            convert( path )
        elif os.path.isdir( path ):
            explore( path )

if __name__ == "__main__":
    #process_bak_files(action='clear')
    main() 