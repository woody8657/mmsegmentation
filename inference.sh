CUDA_VISIBLE_DEVICES=1 python tools/test.py \
    configs/Ganzin/test_inf.py \
    /home/u/woody8657/projs/mmsegmentation/work_dirs/pretrain_b_dice/iter_5000.pth \
    --show-dir test_results \
    --eval-options efficient_test=True \
    --eval mIoU

