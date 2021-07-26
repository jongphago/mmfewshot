# this file is only used for testing the model
from mmcls.models.builder import build_classifier as build_cls_model

from mmfewshot.detection.models import build_detector as build_det_model


def build_model(*args, task_type='mmdet', **kwargs):
    if task_type == 'mmdet':
        return build_det_model(*args, **kwargs)
    elif task_type == 'mmcls':
        return build_cls_model(*args, **kwargs)
