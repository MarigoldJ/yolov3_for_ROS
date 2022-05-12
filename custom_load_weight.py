"""
Download pretrained weight from github.

Usage:
    $ python custom_load_weight.py --name tiny_data.pt
"""
import os
import argparse
import wget

def load_weight(name='person-bottle-01.pt'):
    # directory for pretrained model
    PATH_PT = 'pretrained'
    if not os.path.isdir(PATH_PT):
        os.mkdir(PATH_PT)

    print('weight name:', name)

    # check pretrained model
    if not os.path.exists(f'{PATH_PT}/{name}'):
        wget.download(
            f'https://github.com/MarigoldJ/yolov3_for_ROS/releases/download/custom/{name}',
            out=PATH_PT
        )
        print(f'\n{name} is loaded!')
    else:
        print(f'\n{name} is already loaded.')

    return f'{PATH_PT}/{name}'


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='person-bottle-01.pt', help='released pretrained model weight file name.')
    opt = parser.parse_args()
    return opt


if __name__ == "__main__":
    opt = parse_opt()
    load_weight(**vars(opt))