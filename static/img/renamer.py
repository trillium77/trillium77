import os
#ps=['bar','closet','commercial','fireplace','modern','other','traditional','transitional','vanities']
for p in ps:
    os.chdir(p)
    n=1
    fs=os.listdir()
    for f in fs:
        nn="i_"+str(n)+".jpeg"
        os.rename(f,nn)
        n+=1
    os.chdir('../..')
