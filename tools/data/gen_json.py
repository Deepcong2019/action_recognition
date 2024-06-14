import json
import os

import decord


def write_json(path_train, jsonpath):
    output_list = []
    train_file_list = os.listdir(path_train)
    for train_name in train_file_list:
        train_dict = {}
        sp = train_name.split('_')
        train_dict['vid_name'] = train_name.replace('.avi', '')
        train_dict['label'] = int(sp[1].replace('.avi', ''))
        train_dict['start_frame'] = 0

        video_path = os.path.join(path_train, train_name)
        vid = decord.VideoReader(video_path)
        train_dict['end_frame'] = len(vid)
        output_list.append(train_dict.copy())
    with open(jsonpath, 'w') as outfile:
        json.dump(output_list, outfile)


write_json('../../data/Weizmann/train', '../../data/Weizmann/train.json')
write_json('../../data/Weizmann/test', '../../data/Weizmann/test.json')

