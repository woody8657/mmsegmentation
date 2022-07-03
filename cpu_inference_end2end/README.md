# Data structure 
# Before run run_all.sh, make share puting the datasets as the following structure and name it correctly:
|---R09246003
    |---README.md
    |---S5
        |---01, 02, 03, ..., 26
            |---0.jpg, 1.jpg, ...
    |---hidden
        |---S11, S22, S33(此處subject名稱僅為範例)
            |---01, 02, 03...  (S11, S22, S33底下的資料夾數量不同)
                |---0.jpg, 1.jpg, ...
    |---challenge
        |---HM
        |---KL  (rename 11.png, 12.png to 11.jpg, 12.jpg)
    
# Running steps
1. conda create --name NoteammateHeHe python=3.8 -y
2. conda activate NoteammateHeHe
3. sh run_all.sh (remember to press y)
Result (hidden_mask.zip) will be saved to R09246003/hidden_mask.zip
