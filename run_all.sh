# Before run this script, make share puting the hidden dataset as following structure and name it as hidden:
# |---mmsegmentation
# |---hidden
#     |---S11, S22, S33(此處subject名稱僅為範例)
#         |---01, 02, 03...  (S11, S22, S33底下的資料夾數量不同)
#            |---0.jpg, 1.jpg, ...

# inference by  convnext
sh inference.sh
# change color of mask and colculate confidence by shape analysis
python submission+post.py
# zip the result output: 'hidden_mask.zip'
zip -r hidden_mask hidden_mask/*