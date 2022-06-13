_base_ = '../convnext/upernet_convnext_tiny_fp16_512x512_160k_ade20k.py'

model = dict(
    decode_head=dict(num_classes=2, loss_decode=dict(type='DiceLoss')),
    auxiliary_head=dict(num_classes=2, loss_decode=dict(type='DiceLoss'))
)

data = dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    )

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '/home/u/woody8657/projs/mmsegmentation/upernet_convnext_tiny_fp16_512x512_160k_ade20k_20220227_124553-cad485de.pth'
resume_from = None
workflow = [('train', 1), ('val', 1)]
cudnn_benchmark = True

work_dir = './work_dirs/convnext'