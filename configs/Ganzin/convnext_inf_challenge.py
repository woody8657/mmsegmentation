_base_ = '../convnext/upernet_convnext_tiny_fp16_512x512_160k_ade20k.py'

model = dict(
    decode_head=dict(num_classes=2, loss_decode=dict(type='DiceLoss')),
    auxiliary_head=dict(num_classes=2, loss_decode=dict(type='DiceLoss'))
)

data = dict(test=dict(data_root='../challenge/',
                        img_dir=''))

dist_params = dict(backend='nccl')
log_level = 'INFO'
workflow = [('val', 1)]
cudnn_benchmark = True

work_dir = './work_dirs/convnext_a'