from sys import argv
from hashlib import md5, sha1, sha224, sha256, sha384, sha512

import requests

program = int(input("Would you like to Hash[0] or Dehash [1] : "))

if program == 0:
    print("You're in Hashing Program")
    string_to_hash = input("Kindly type the text you would like to Hash: ")
    print("""Which of the Following Hashing scheme would you like to use:
        1. MD5
        2. SHA1
        3. SHA224
        4. SHA256
        5. SHA384
        6. SHA512
        0. All the Above
    """)
    scheme_hash = int(input(" Kindly type [1 - 6]: "))
    if scheme_hash == 1:
        print("The MD5 Hash for", string_to_hash, "is", md5(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 2:
        print("The SHA1 Hash for", string_to_hash, "is", sha1(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 3:
        print("The SHA224 Hash for", string_to_hash, "is", sha224(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 4:
        print("The SHA256 Hash for", string_to_hash, "is", sha256(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 5:
        print("The SHA384 Hash for", string_to_hash, "is", sha384(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 6:
        print("The SHA512 Hash for", string_to_hash, "is", sha512(str.encode(string_to_hash)).hexdigest())
    elif scheme_hash == 0:
        print("The MD5 Hash for", string_to_hash, "is", md5(str.encode(string_to_hash)).hexdigest())
        print("The SHA1 Hash for", string_to_hash, "is", sha1(str.encode(string_to_hash)).hexdigest())
        print("The SHA224 Hash for", string_to_hash, "is", sha224(str.encode(string_to_hash)).hexdigest())
        print("The SHA256 Hash for", string_to_hash, "is", sha256(str.encode(string_to_hash)).hexdigest())
        print("The SHA384 Hash for", string_to_hash, "is", sha384(str.encode(string_to_hash)).hexdigest())
        print("The SHA512 Hash for", string_to_hash, "is", sha512(str.encode(string_to_hash)).hexdigest())
    else:
        print("You've typed invalid number to enter the program")

elif program == 1:
    print("You're in Dehashing Program")
    print("""Which of the Following Hashing scheme would you like to use for Bruteforcing:
        1. MD5
        2. SHA1
        3. SHA224
        4. SHA256
        5. SHA384
        6. SHA512
        0. All the Above
    """)
    hash_scheme = int(input("Kindly type from [1 - 6] : "))
    string_to_dehash = input("Kindly type the string to dehash : ")
    web_service = int(input("Would you like to use [md5decrypt.net] webservice : [0 : Yes or 1 No] : "))
    if web_service == 0:
        hash_scheme_to_text = "hash_scheme"
        if hash_scheme == 1:
            hash_scheme_to_text = "md5"
        elif hash_scheme == 2:
            hash_scheme_to_text = "sha1"
        elif hash_scheme == 3:
            hash_scheme_to_text = "sha224"
        elif hash_scheme == 4:
            hash_scheme_to_text = "sha256"
        elif hash_scheme == 5:
            hash_scheme_to_text = "sha384"
        elif hash_scheme == 6:
            hash_scheme_to_text = "sha512"
        elif hash_scheme == 0:
            print("All the Above not supported with the web version")
        web_service_email = input("Kindly type your email: ")
        web_service_code = input("Kindly type your secret code: ")
        response = requests.get(
            'https://md5decrypt.net/en/Api/api.php?hash=' + string_to_dehash + '&hash_type=' + hash_scheme_to_text + '&email=' + web_service_email + '&code=' + web_service_code)
        print("Match Found : " + response.text)
        exit()
    elif web_service == 1:
        print("Sticking with the File one")
    file_name = input("Which password file would you like to use: ")

    file = open(file_name, 'rt')

    while True:
        a = file.readline().rstrip("\n")
        decoded_string = a
        a = str.encode(a)
        print(a)
        if hash_scheme == 1:
            temp = md5(a).hexdigest()
            print(temp)
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 2:
            temp = sha1(a).hexdigest()
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 3:
            temp = sha224(a).hexdigest()
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 4:
            temp = sha256(a).hexdigest()
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 5:
            temp = sha384(a).hexdigest()
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 6:
            temp = sha512(a).hexdigest()
            if temp == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + decoded_string)
                break
        elif hash_scheme == 0:
            temp_md5 = md5(a).hexdigest()
            temp_sha1 = sha1(a).hexdigest()
            temp_sha224 = sha224(a).hexdigest()
            temp_sha256 = sha256(a).hexdigest()
            temp_sha348 = sha384(a).hexdigest()
            temp_sha512 = sha512(a).hexdigest()
            if temp_md5 == string_to_dehash or temp_sha1 == string_to_dehash or temp_sha224 == string_to_dehash or temp_sha256 == string_to_dehash or temp_sha348 == string_to_dehash or temp_sha512 == string_to_dehash:
                print('\033[31m' + 'Match Found : ')
                print('\033[32m' + "\t " + temp + " is equal to " + a)
                break
        else:
            print("Kindly type from 1-6 or Match not found")
        if not a:
            break
    # Terminal Back to Normal
    print('\033[39m')
    file.close()
    exit()

