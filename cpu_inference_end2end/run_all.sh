conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install -U openmim==0.1.5
mim install mmcv-full==1.5.2
git clone https://github.com/woody8657/mmsegmentation.git
# wget https://drive.google.com/u/0/uc?id=1RKg_yJP2UjSYdoVQ0b86zphRnX4fnEgW&export=download
cd mmsegmentation
pip install -v -e .


# inference by  convnext
sh inference.sh
# change color of mask and colculate confidence by shape analysis
python submission+post.py --dataset hidden
# zip the result output: 'hidden_mask.zip'
zip -r hidden hidden/*
mv hidden.zip ../

# inference by  convnext
sh inference_S5.sh
# change color of mask and colculate confidence by shape analysis
python submission+post.py --dataset S5
# zip the result output: 'S5.zip'
mv S5 S5_solution
zip -r S5_solution S5_solution/*
mv S5_solution.zip ../

# inference by  convnext
sh inference_challenge.sh
# change color of mask and colculate confidence by shape analysis
python submission+post.py --dataset challenge
# zip the result output: 'challenge.zip'
zip -r challenge challenge/*
mv challenge.zip ../

cd ..