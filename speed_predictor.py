import torch.nn
import os
from network import FC
from Json_to_speed import get_interpolated_speed
# def speed_loader:
def speed_reader (json_path):
    filename = os.listdir(json_path)
    speed = []
    indix = []
    for file in filename:
        idx = file.split('.')[0]
        target_speed = get_interpolated_speed(json_path + '/' + file, '', 3)
        if target_speed is None:
            continue
        else:
            for i, item in enumerate(target_speed):
                front = str(idx) + '_' + str(i)
                speed.append(item)
                indix.append(front)
    return speed, indix

# def Speed_pre (attention_feature, speed_target):
#     # print(len(attention_feature))
#     speed_model = FC(16384, 10000, 2).cuda()
#     speed_output = speed_model(attention_feature)
#     # print(speed_output)
#     loss = abs(torch.sqrt(torch.square(speed_output[0]) + torch.square(speed_output[1]))-torch.sqrt(torch.square(speed_target[0]) + torch.square(speed_target[1])))
#     return loss
    # optimizers = torch.optim.Adam(speed_output.parameters(), lr=1e-4)
    # optimizers.zero_grad()
    # loss.backward()
    # optimizers.step()