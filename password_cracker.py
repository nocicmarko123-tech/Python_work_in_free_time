import time
import pathlib

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "
password = input("as")

print("Cracking process started...")
start = time.time()
for i in characters:
    if i == password:
        break
    elif str(password[0]) == i:
        
    for j in characters:
        if i + j == password:
            break
        for k in characters:
            if i + j + k == password:
                break
            for l in characters:
                if i + j + k + l == password:
                    break
                for m in characters:
                    if i + j + k + l + m == password:
                        break
                    for n in characters:
                        if i + j + k + l + m + n == password:
                            break
                        for o in characters:
                            if i + j + k + l + m + n + o == password:
                                break
                            for p in characters:
                                if i + j + k + l + m + n + o + p == password:
                                    break
                                for q in characters:
                                    if i + j + k + l + m + n + o + p + q == password:
                                        break
                                    for r in characters:
                                        if i + j + k + l + m + n + o + p + q + r == password:
                                            break
                                        for s in characters:
                                            if i + j + k + l + m + n + o + p + q + r + s == password:
                                                break
                                            for t in characters:
                                                if i + j + k + l + m + n + o + p + q + r + s + t == password:
                                                    break
                                                for u in characters:
                                                    if i + j + k + l + m + n + o + p + q + r + s + t + u == password:
                                                        break
                                                    for v in characters:
                                                        if i + j + k + l + m + n + o + p + q + r + s + t + u + v == password:
                                                            break
                                                        for w in characters:
                                                            if i + j + k + l + m + n + o + p + q + r + s + t + u + v + w == password:
                                                                break
                                                            for x in characters:
                                                                if i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x == password:
                                                                    break
                                                                for y in characters:
                                                                    if i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y == password:
                                                                        break
                                                                    for z in characters:
                                                                        if i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z == password:
                                                                            break

print("Password cracked")
end = time.time()
print("Time for cracking: " + str(round(end - start)))
#first version of the password cracking, today doing only input passwords
#educational purposes only, do not use this for illegal activities
#see how good is your password
#stop AI
