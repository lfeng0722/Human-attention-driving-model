from Json_to_speed import get_interpolated_speed
# from speed_predictor import speed_reader
# speed = speed_reader('BDDA/training/gps_jsons')
# print(speed)

import json
import pprint
import os
# filename = 'BDDA/training/gps_jsons/2.json'
# with open(filename) as f:
#     speed = json.load(f)
# print(speed)

json_path = 'BDDA/training/gps_jsons'
filename = os.listdir(json_path)
speed = []
for file in filename:
    idx=file.split('.')[0]
    target_speed = get_interpolated_speed(json_path+'/'+file, '', 3)
    if target_speed is None:
        continue
    else:
        for i, item in enumerate(target_speed):
            front = str(idx)+'_'+str(i)
            speed[front]=item
print(speed)
