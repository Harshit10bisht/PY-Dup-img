import os
import pandas as pd
import numpy as np


import imagehash
from PIL import Image
def img_hash(file, hash_size):
    return imagehash.phash(Image.open(file),hash_size=hash_size)

def get_hashes(directory, hash_size):
    hash_file = 'img_hashes_%s.csv' % hash_size
    if not os.path.isfile(hash_file):
        hashes = pd.DataFrame()
    else:
        hashes = pd.read_csv(hash_file)
    new_hashes_calculated = 0
    num_of_files = len(os.listdir(directory))
    for file in os.listdir(directory):
        if 'file' not in hashes.columns or file not in list(hashes['file']):                                               
            new_hashes_calculated = new_hashes_calculated + 1
            result = {'file': file,'hash':img_hash(directory + '/' + file,hash_size)}
            hashes = hashes.append(result,ignore_index=True)
            if (new_hashes_calculated % 200 == 199):
                hashes[['file','hash']].to_csv(hash_file,index=False) 
    if new_hashes_calculated:
        hashes[['file','hash']].to_csv(hash_file,index=False)    
    return read_hashes(hash_size)

def read_hashes(hash_size):
    hash_file = 'img_hashes_%s.csv' % hash_size
    hashes = pd.read_csv(hash_file)[['file','hash']]
    lambdafunc = lambda x: pd.Series([int(i,16) for key,i in zip(range(0,len(x['hash'])),x['hash'])])
    newcols = hashes.apply(lambdafunc, axis=1)
    newcols.columns = [str(i) for i in range(0,len(hashes.iloc[0]['hash']))]
    return hashes.join(newcols)

hashes_16_lag = get_hashes('C:/Users/user/AppData/Local/Programs/Python/Python36/opencv/images_1',16)

hashes_16_lag.head()

print("%s out of %s" % (len(hashes_16_lag[hashes_16_lag.duplicated(subset='hash',keep=False)]),len(hashes_16_lag)))

