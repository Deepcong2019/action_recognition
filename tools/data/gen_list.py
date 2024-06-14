import os

from pyskl.smp import mwlines


def write_list(dir_path, name):
    path_train = os.path.join(dir_path, 'train')
    path_test = os.path.join(dir_path, 'test')
    train_file_list = os.listdir(path_train)
    test_file_list = os.listdir(path_test)

    train = []
    for train_name in train_file_list:
        train_dict = {}
        sp = train_name.split('_')

        train_dict['vid_name'] = train_name
        train_dict['label'] = sp[1].replace('.avi', '')
        train.append(train_dict)
    test = []
    for test_name in test_file_list:
        test_dict = {}
        sp = test_name.split('_')
        test_dict['vid_name'] = test_name
        test_dict['label'] = sp[1].replace('.avi', '')
        test.append(test_dict)

    tmpl1 = os.path.join(path_train, '{}')
    lines1 = [(tmpl1 + ' {}').format(x['vid_name'], x['label']) for x in train]

    tmpl2 = os.path.join(path_test, '{}')
    lines2 = [(tmpl2 + ' {}').format(x['vid_name'], x['label']) for x in test]
    lines = lines1 + lines2
    mwlines(lines, os.path.join(dir_path, name))


write_list('C:\\Users\\Administrator\\Desktop\\pyspace\\pyskl-main\\data\\Weizmann', 'Weizmann.list')