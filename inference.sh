CUDA_VISIBLE_DEVICES=1 python tools/test.py \
    configs/Ganzin/convnext_inf.py \
    /home/u/woody8657/projs/mmsegmentation/work_dirs/convnext_b/best_mIoU_iter_12000.pth \
    --show-dir test_results \
    --eval-options efficient_test=True \
    --eval mIoU

