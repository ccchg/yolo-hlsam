# Training instruction for Yolov7

If you have previously used a different version of YOLO, we strongly recommend that you delete and files.

## 1. Data Preparation
The production of the dataset needs to be done carefully. After all, it is necessary to observe the quality of the model training and make improvements accordingly.

The folder Settings are as follows:

```
VOCData
|____VOCTest
| |____Annotations
| |____ImageStes
| |____JPEGImages
|____VOCTranVal
| |____Annotations
| |____ImageStes
| |____JPEGImages
```
## 2. For training using Yolov7-CBAM
```
python train.py --batch 16 --cfg cfg/training/CBAM3.yaml --img 640 --epochs 100 --data "your data" --weights yolov7.pt --name "file name" --hyp data/hyp.scratch.p5.yaml --device 0
```


# Training instruction for HLSAM

We organize the training folder as follows.
```
train
|____data
|____pretrained_checkpoint
|____train.py
|____utils
| |____dataloader.py
| |____misc.py
| |____loss_mask.py
|____segment_anything_training
|____work_dirs
```

## 1. Data Preparation



### Expected dataset structure

```
data
|____DIS5K
|____cascade_psp
| |____DUTS-TE
| |____DUTS-TR
| |____ecssd
| |____fss_all
| |____MSRA_10K
|____thin_object_detection
| |____COIFT
| |____HRSOD
| |____ThinObject5K

```

## 2. Init Checkpoint
Init checkpoint can be downloaded from [hugging face link](https://huggingface.co/sam-hq-team/sam-hq-training/tree/main/pretrained_checkpoint)

### Expected checkpoint

```
pretrained_checkpoint
|____sam_vit_b_maskdecoder.pth
|____sam_vit_b_01ec64.pth
|____sam_vit_l_maskdecoder.pth
|____sam_vit_l_0b3195.pth
|____sam_vit_h_maskdecoder.pth
|____sam_vit_h_4b8939.pth

```

## 3. Training
To train HLSAM on dataset



