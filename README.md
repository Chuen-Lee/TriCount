# <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a>

## Counting beetles made easy with TriCount

### Check out the <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a> app

1. Upload an image.

<p align="center">
<img src="https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/demo_upload.png?raw=true" alt="Demo_upload" width="600"/>
</p>

2. Adjust the options to find suitable values for your purposes.

<p align="center">
<img src="https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/demo_options.png?raw=true" alt="Demo_options" width="300"/>
</p>

### A few tips

1. Use images taken from the same height (object should be similar size) and lighting (avoid shadows).
2. Adjust "Size of beetles" first to find a reasonable count. Then, alter "Distance between beetles" to find the best reading.
3. If both steps 1 and 2 were followed but still not working, go to "Advanced Options", try changing "Threshold".
4. If all above fails, reach out to me.

## Alternatively, use the python code. Quick Start Guide:
### clone this github repo:
```
git clone https://github.com/Chuen-Lee/TriCount.git
```
```
cd TriCount
```
### Copy the environment:
You will need to pre-install miniconda
```
conda env create -f scripts/TriCountenv.yml
```
```
conda activate tricount
```
### Usage:
```
python3 scripts/TriCount.py -i {inputfile} -o {outputfile}
```
### Example:
```
python3 scripts/TriCount.py -i demo_images/10.jpg -o demo_images/out10.jpg
```

## Citation:

## Acknowledgement:


<iframe src="https://tricount.streamlitapp.com/?embedded=true" width="600" height="450"></iframe>
