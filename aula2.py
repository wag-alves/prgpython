import os
meuhome = 'C:\\Users\\20221014050009'
for rootdir, dirs, files in os.walk(meuhome):
    print(rootdir)
    for d in dirs:
        print(d)
    for f in files:
        print(f)