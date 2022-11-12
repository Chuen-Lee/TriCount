import cv2
import numpy as np
import streamlit as st
from PIL import Image

def main_loop():
    st.title("TriCount App")
    st.text("Author: Chuen")
    st.subheader("Counting beetles made easy with TriCount")
    st.text("Consistent image height and lighting is essential for optimal results")

    with st.sidebar.expander("Basic Options", expanded=True):
        binary = st.slider("Distance between beetles", min_value=5, max_value=11, value=5,step=2)
        size = st.slider("Size of beetles", min_value=1, max_value=50, value=5,step=1)

    with st.sidebar.expander("Advanced Options"):
        resize = st.slider("Resize Image", min_value=300, max_value=5000, value=500,step=100)
        threshold_constant = st.slider("Threshold", min_value=-30, max_value=30, value=4,step=1)
        blur = st.slider("Blur Intensity", min_value=5, max_value=55, value=15,step=10)

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None
    image_file = st.camera_input("Take a picture")
    if not image_file:
        return none

    original_image = Image.open(image_file)
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
        st.image(original_image,width=300)

    with col2:
        st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
        img = np.array(original_image)
        img = cv2.resize(img,(resize,resize),interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray_blur=cv2.GaussianBlur(gray,(blur,blur),0)
        thresh = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,binary,threshold_constant)
        kernel=np.ones((1,1),np.uint8)
        closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=10)
        result_img=closing.copy()
        # cv2.imshow("Binary",result_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        contours,hierachy=cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        counter=0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if  area <  size  :
            #if area<  300 :
                continue
            counter+=1
            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(img,ellipse,(0,255,0),1)
        final_image = cv2.putText(img,"Beetles="+str(counter),(100,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
        st.image(final_image,width=300)
        cv2.imwrite("output.png",final_image)


    st.text("Number of Beetles = " + str(counter))

    st.download_button(label = "Download Output", data = open('output.png', 'rb').read(), mime="image/png")


if __name__ == '__main__':
    main_loop()

st.write("#")
st.write("#")
st.write("### For examples on how to use this app, visit [TriCount GitHub](https://chuen-lee.github.io/TriCount/)")
st.write("#")
st.write("#")
st.write("#")


col1, col2, col3 = st.columns( [1, 1, 1])
with col1:
    st.write("#")
with col2:
    st.markdown('''<a href="https://chuen-lee.github.io/"> <img src="https://avatars.githubusercontent.com/u/92123911?v=4" alt="Chuen's Logo" width="200"/> </a>''', unsafe_allow_html=True)

with col3:
    st.write("#")
