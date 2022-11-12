# <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a>

Author: Chuen

## Counting beetles made easy with TriCount

### Check out the <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a> app

1. Upload an image.

2. Adjust the options to find suitable values for your purposes.

<p align="center">
<img src="https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/demo_options.png?raw=true" alt="Demo_options" width="300"/>
</p>

3. See <a href="https://github.com/Chuen-Lee/TriCount#examples">examples</a>

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

## Examples
### Images used can be found in demo_images <a href="https://github.com/Chuen-Lee/TriCount/tree/main/demo_images" target="_blank">TriCount</a>

### Example A - 10 Beetles

Upload image <a href = "https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/10.jpg?raw=true" target="_blank">10.jpg</a> to <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a> app

<p align="center">
<img src="https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/output/10_exampleA.png?raw=true" alt="Demo_upload" width="600"/>
</p>

```
python3 scripts/TriCount.py -i demo_images/10.jpg -o demo_images/output/10_exampleA.png
```


### Example B - 28 Beetles
Upload image 28.jpg to <a href = "https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/28.jpg?raw=true" target="_blank">28.jpg</a> <a href="https://tricount.streamlit.app/" target="_blank">TriCount</a> app

<p align="center">
<img src="https://github.com/Chuen-Lee/TriCount/blob/main/demo_images/output/28_exampleB.png?raw=true" alt="Demo_upload" width="600"/>
</p>

```
python3 scripts/TriCount.py -i demo_images/28.jpg -o demo_images/output/28_exampleB.png
```

## LICENSE

Copyright (c) 2022 Chuen Zhang Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Citation:

## Acknowledgement:
A huge thanks to George West for providing images of beetles for testing and development. Thanks to all that have helped test the app.

<a href="https://chuen-lee.github.io/"> <img src="https://avatars.githubusercontent.com/u/92123911?v=4" alt="Demo_upload" width="600"/> </a>
