_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
model = dict(
    pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101),
    decode_head=dict(num_classes=2,loss_decode=dict(type='DiceLoss')), auxiliary_head=dict(num_classes=2,loss_decode=dict(type='DiceLoss')))
data = dict(
    samples_per_gpu=7,
    workers_per_gpu=4,
    )

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '/home/u/woody8657/projs/mmsegmentation/deeplabv3_r101-d8_512x512_80k_ade20k_20200615_021256-d89c7fa4.pth'
resume_from = None
workflow = [('train', 1), ('val', 1)]
cudnn_benchmark = True
checkpoint_config = dict(by_epoch=False, interval=100)
# evaluation = dict(interval=5000, metric='mIoU', pre_eval=True)
work_dir = './work_dirs/pretrain_b_dice_long'
