import hashlib

door_id = 'ffykfhsq'
num = 0
cnt = 0

while cnt < 8:
    m = hashlib.md5((door_id + str(num)).encode())
    digest = m.hexdigest()
    if digest[:5] == '00000':
        print(digest[5])
        cnt += 1
    num += 1

num = 0
password = list('XXXXXXXX')
print(password)
while 'X' in password:
    digest = hashlib.md5((door_id + str(num)).encode()).hexdigest()
    if digest[:5] == '00000':
        try:
            if int(digest[5]) in range(0, 8):
                print(digest)
                loc = int(digest[5])
                letter = digest[6]
                print(loc)
                print(letter)
                if password[loc] == 'X':
                    print('found a letter')
                    password[loc] = letter
                    print('Password is: ', password)
        except:

            pass
    num += 1

print(password)