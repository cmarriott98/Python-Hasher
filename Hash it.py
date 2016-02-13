
## import the hash libraries & set block size to save memory ##
## sha-3 hash is notnative to hashlib so has to be added manually using pysha3##

import hashlib, sha3
BLOCKSIZE = 65536

## set for each hash type ##

md5_hasher = hashlib.md5()
sha1_hasher = hashlib.sha1()
sha256_hasher = hashlib.sha256()
sha512_hasher = hashlib.sha512()
sha3_hasher = hashlib.sha3_512()

## simple main meny and loop to allow for multiple passes ##
## program can do strings or files ##

class main():   
    def home_screen():
        print(
    '''
    ---------------------------------
            +-+-+-+-+-+-+-+
            |H|A|S|H| |I|T|
            +-+-+-+-+-+-+-+
    ---------------------------------
      Please select an option:
    ---------------------------------
      1 = HASH A STRING
      2 = HASH A FILE
      3 = QUIT
    ---------------------------------''')
        return

## the menu options have error control built in ##

    def menu_choice():
        global menu_choice
        valid = True
        while valid:
            menu_choice = input('''
    PLEASE SELECT AN OPTION: ''').lower()
            if len(menu_choice) != 1 or menu_choice not in '1234':
                print('''
    ERROR - PLEASE ENTER A VALID CHOICE''')  
            else:
                valid = False
        return

    def goodbye():
        print('''
    ---------------------------------
            +-+-+-+-+-+-+-+
            |G|O|O|D|B|Y|E|
            +-+-+-+-+-+-+-+
    ---------------------------------
    ''')
        return

## seperate class for hashing strings, called from the main program ##
## runs in a simple while loop to facilitate multiple passes ##

class hash_string():
    def go():
        run = 'y'
        while run != 'n':
            mystring = input('''
    PLEASE ENTER A STRING TO HASH:  ''')
            md5_hash_object = hashlib.md5(mystring.encode())
            print('''   
    MD5 HASH:
    -----------------------------------
    ''',md5_hash_object.hexdigest())
            sha1_hash_object = hashlib.sha1(mystring.encode())
            print('''
    SHA-1 HASH:
    -----------------------------------
    ''',sha1_hash_object.hexdigest())
            sha256_hash_object = hashlib.sha256(mystring.encode())
            print('''
    SHA-256 HASH:
    -----------------------------------
    ''',sha256_hash_object.hexdigest())
            sha512_hash_object = hashlib.sha512(mystring.encode())
            print('''
    SHA-512 HASH:
    -----------------------------------
    ''',sha512_hash_object.hexdigest())
            sha3_hash_object = hashlib.sha3_512(mystring.encode())
            print('''
    SHA-3 HASH:
    -----------------------------------
    ''',sha3_hash_object.hexdigest())                           
            run = input('''
    ------------------
    RUN ANOTHER? (y/n) ''')
        return

## likewise with the file hashing loop ##

class hash_file():
    def go():
        run = 'y'
        while run != 'n':
            input_file = input('''
    PLEASE ENTER A FILE TO HASH:  ''')
            with open(input_file, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    md5_hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
                print('''   
    MD5 HASH:
    -----------------------------------
    ''',md5_hasher.hexdigest())
            
            with open(input_file, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    sha1_hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
                print('''
    SHA-1 HASH:
    -----------------------------------
    ''',sha1_hasher.hexdigest())

            with open(input_file, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    sha256_hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
                print('''
    SHA-256 HASH:
    -----------------------------------
    ''',sha256_hasher.hexdigest())

            with open(input_file, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    sha512_hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
                print('''
    SHA-512 HASH:
    -----------------------------------
    ''',sha512_hasher.hexdigest())

            with open(input_file, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    sha3_hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            print('''
    SHA-3 HASH:
    -----------------------------------
    ''',sha3_hasher.hexdigest())

            run = input('''
    ------------------
    RUN ANOTHER? (y/n) ''')        
        return

## running the program ##
     
menu_choice = ""
while menu_choice != "3":    
    main.home_screen()
    main.menu_choice()
    if menu_choice == "1":
        hash_string.go()
    if menu_choice == "2":
        hash_file.go()
main.goodbye()                
                       
                       
## Charlie Marriott, D14123014 - Mobile Device Forensics Lab II ##
## 09.02.2016 ##
