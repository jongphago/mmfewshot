_base_ = ['baseline_mini_imagenet_5way_5shot_84x84_aug.py']

data = dict(samples_per_gpu=32, workers_per_gpu=2)
model = dict(
    type='BaselineClassifier',
    backbone=dict(type='WRN28x10'),
    head=dict(type='LinearHead', num_classes=100, in_channels=640),
    meta_test_head=dict(type='LinearHead', num_classes=5, in_channels=640))
optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0001)