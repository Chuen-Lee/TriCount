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


<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1718.6454008049905!2d-71.07787073663287!3d42.36955552931532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e370bc261e50e5%3A0xf3cba8437d505a26!2sHubSpot!5e0!3m2!1sen!2sus!4v1602001548652!5m2!1sen!2sus" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
