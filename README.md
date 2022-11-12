# TriCount

##Counting beetles made easy with TriCount

Check out the [TriCount](https://chuen-lee-tricount-scriptstrilit-37hlb0.streamlit.app) app

1. Upload an image.

<p align="center">
<img src="/demo_images/demo_upload.png" alt="Demo_upload" width="500"/>
</p>

2. Adjust the options to find suitable values for your purposes.

<p align="center">
<img src="/demo_images/demo_options.png" alt="Demo_options" width="500"/>
</p>

##A few tips

1. Use images taken from the same height (object should be similar size) and lighting (avoid shadows).
2. Adjust "Size of beetles" first to find a reasonable count. Then, alter "Distance between beetles" to find the best reading.
3. If both steps 1 and 2 were followed but still not working, go to "Advanced Options", try changing "Threshold".
4. If all above fails, reach out to me.

# Alternatively, use the python code. Quick Start Guide:
##clone this github repo:
```
git clone https://github.com/Chuen-Lee/TriCount.git
```
```
cd TriCount
```
##conda to copy the environment:
```
conda env create -f scripts/TriCountenv.yml
```
```
conda activate tricount
```
##Usage:
```
python3 scripts/TriCount.py -i {inputfile} -o {outputfile}
```
##Example:
```
python3 scripts/TriCount.py -i demo_images/10.jpg -o demo_images/out10.jpg
```
#End:

Thank you for checking out TriCount!

#Citation:

#Acknowledgement:
