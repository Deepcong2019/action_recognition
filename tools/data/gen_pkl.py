import os
from mmcv import load, dump

def traintest(dirpath,pklname,newpklname):
    os.chdir(dirpath)
    train = load('train.json')
    test = load('test.json')
    annotations = load(pklname)
    print(annotations)
    split = dict()
    split['xsub_train'] = [x['vid_name'] for x in train]
    split['xsub_val'] = [x['vid_name'] for x in test]
    dump(dict(split=split, annotations=annotations), newpklname)

traintest('../../data/Weizmann', 'train.pkl', 'Wei_xsub_stgn++.pkl')