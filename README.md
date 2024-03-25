# NTIRE2024_HRDepth_M

## Pre-trained models 

We provide a fine-tuned models based on DepthAnything. You can download [ZodDepth4ToM.pt](https://pan.baidu.com/s/1kTxfJEqAkwHVq548XEAeNA?pwd=4vmm)here.  
code:4vmm 

And we use the pre-trained models provided by DepthAnything. You can download [depth_anything_vitl14.pth](https://huggingface.co/spaces/LiheYoung/Depth-Anything/blob/main/checkpoints/depth_anything_vitl14.pth) here. 

Then, put ZopDepth4ToM.pt and depth_anything_vitl14.pth in 'metric_depth/checkpoints'.

## Data set
Put test data in 'metric_depth/data', and rename it with 'Booster-test'

### Running

```bash
cd metric_depth
python blur.py
python run.py -m zoedepth --pretrained_resource="local::./checkpoints/ZoeDepth4ToM.pt" -d Booster
