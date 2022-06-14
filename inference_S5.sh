CUDA_VISIBLE_DEVICES=1 python tools/test.py \
    configs/Ganzin/convnext_inf_S5.py \
    ../best_mIoU_iter_17000.pth \
    --show-dir test_results \
    --eval-options efficient_test=True \
    --eval mIoU

