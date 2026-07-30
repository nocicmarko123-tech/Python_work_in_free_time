import time
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "
#first version of the password cracking, today doing only input passwords
#educational purposes only, do not use this for illegal activities
#see how good is your password
#stop AI
password = len(str(input("Enter the password to see if it can be cracked and at what time:")))

print("Cracking process started...")
start = time.time()
while True:
    for i in characters:
        if i == password:
            False
        for j in characters:
            if i+j == password:
                False
            for k in characters:
                if i+j+k == password:
                    False
                for l in characters:
                    if i+j+k+l == password:
                        False
                    for m in characters:
                        if i+j+k+l+m == password:
                            False
                        for n in characters:
                            if i+j+k+l+m+n == password:
                                False
                            for o in characters:
                                if i+j+k+l+m+n+o == password:
                                    False
                                for p in characters:
                                    if i+j+k+l+m+n+o+p == password:
                                        False
                                    for q in characters:
                                        if i+j+k+l+m+n+o+p+q == password:
                                            False
                                        for r in characters:
                                            if i+j+k+l+m+n+o+p+q+r == password:
                                                False
                                            for s in characters:
                                                if i+j+k+l+m+n+o+p+q+r+s == password:
                                                    False
                                                for t in characters:
                                                    if i+j+k+l+m+n+o+p+q+r+s+t == password:
                                                        False
                                                    for u in characters:
                                                        if i+j+k+l+m+n+o+p+q+r+s+t+u == password:
                                                            False
                                                        for v in characters:
                                                            if i+j+k+l+m+n+o+p+q+r+s+t+u+v == password:
                                                                False
                                                            for w in characters:
                                                                if i+j+k+l+m+n+o+p+q+r+s+t+u+v+w == password:
                                                                    False
                                                                for x in characters:
                                                                    if i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x == password:
                                                                        False
                                                                    for y in characters:
                                                                        if i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y == password:
                                                                            False
                                                                        for z in characters:
                                                                            if i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z == password:
                                                                                False
print("Password cracked")
end = time.time()
print("Time for cracking: " + str(round(end - start)))
