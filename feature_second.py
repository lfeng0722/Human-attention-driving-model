import os
import numpy as np
import cv2
import torch
import torch.nn
import torchvision.models as models
from torch.autograd import Variable
import torch.cuda
import torchvision.transforms as transforms

from PIL import Image

TARGET_IMG_SIZE = 640
img_to_tensor = transforms.ToTensor()


def make_model():
    model = models.vgg16(pretrained=True).features[:28]  # 其实就是定位到第28层，对照着上面的key看就可以理解
    model = model.eval()  # 一定要有这行，不然运算速度会变慢（要求梯度）而且会影响结果
    model.cuda()  # 将模型从CPU发送到GPU,如果没有GPU则删除该行
    return model


# 特征提取
def extract_feature(img):
    model = make_model()
    model.eval()  # 必须要有，不然会影响特征提取结果
    print(np.shape(img))

    img = cv2.resize(img,(640,640),interpolation=cv2.INTER_AREA)
    tensor = img_to_tensor(img)  # 将图片转化成tensor
    tensor = tensor.cuda()  # 如果只是在cpu上跑的话要将这行去掉

    result = model(Variable(tensor))
    # result_npy = result.data.cpu().numpy()  # 保存的时候一定要记得转成cpu形式的，不然可能会出错

    return result[0]  # 返回的矩阵shape是[1, 512, 14, 14]，这么做是为了让shape变回[512, 14,14]


# if __name__ == "__main__":
#
#     imgpath = '/path/to/img.jpg'
#     tmp = extract_feature(model, imgpath)

