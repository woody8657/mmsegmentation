_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
model = dict(decode_head=dict(num_classes=150, loss_decode=dict(type='DiceLoss')),auxiliary_head=dict(num_classes=150, loss_decode=dict(type='DiceLoss')))
# model = dict(
#     decode_head=dict(num_classes=2), auxiliary_head=dict(num_classes=2))
# norm_cfg = dict(type='SyncBN', requires_grad=True)
# model = dict(
#     type='EncoderDecoder',
#     pretrained='open-mmlab://resnet50_v1c',
#     backbone=dict(
#         type='ResNetV1c',
#         depth=50,
#         num_stages=4,
#         out_indices=(0, 1, 2, 3),
#         dilations=(1, 1, 2, 4),
#         strides=(1, 2, 1, 1),
#         norm_cfg=dict(type='SyncBN', requires_grad=True),
#         norm_eval=False,
#         style='pytorch',
#         contract_dilation=True),
#     decode_head=dict(
#         type='ASPPHead',
#         in_channels=2048,
#         in_index=3,
#         channels=512,
#         dilations=(1, 12, 24, 36),
#         dropout_ratio=0.1,
#         num_classes=2,
#         norm_cfg=dict(type='SyncBN', requires_grad=True),
#         align_corners=False,
#         loss_decode=dict(type='DiceLoss', use_sigmoid=False, loss_weight=1.0)),
#     auxiliary_head=dict(
#         type='FCNHead',
#         in_channels=1024,
#         in_index=2,
#         channels=256,
#         num_convs=1,
#         concat_input=False,
#         dropout_ratio=0.1,
#         num_classes=2,
#         norm_cfg=dict(type='SyncBN', requires_grad=True),
#         align_corners=False,
#         loss_decode=dict(type='DiceLoss', use_sigmoid=False, loss_weight=0.4)),
#     train_cfg=dict(),
#     test_cfg=dict(mode='whole'))
workflow = [('val', 1)]
data = dict(
    samples_per_gpu=12,
    workers_per_gpu=4)
runner = dict(type='IterBasedRunner', max_iters=15000)
checkpoint_config = dict(by_epoch=False, interval=5000)
data = dict(test=dict(data_root='/home/u/woody8657/projs/dataset/public/S5',
                        img_dir=''))
