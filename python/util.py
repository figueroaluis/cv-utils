#!/usr/bin/env python
# coding: utf-8

import numpy as np

def get_bbox_center(box):
    '''
    Naive implementation, returns center with floating numbers
    Bounding box has format: x1, y1, x2, y2
    '''
    box_w = box[2] - box[0]
    box_h = box[3] - box[1]
    center = ((box[0] + box[2])/2, (box[1] + box[3])/2)
    
    return center