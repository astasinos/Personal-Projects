# Python-Lane-Detection-with-OpenCV

This is a simple lane detector script based on OpenCV
It works by cropping a specific polygon on the given video,
after it performs grayscaling and gaussian blur.
Then, Hough Transform is used to detect the lines. This is by no means a fully-fledged line detector, since it only uses image processing techniques. 
You can see a demo in the following gif.

  
<img src="https://github.com/astasinos/Personal-Projects/blob/main/Python-Lane-Detection-with-OpenCV/blob/main/videos/gif_image.gif"/>

<p align="center">
  
  <img src="https://github.com/astasinos/Personal-Projects/blob/main/Python-Lane-Detection-with-OpenCV/blob/main/videos/Screenshot_3.png"/>
</p>

The data used was taken from a youtube video of a greek road: [https://www.youtube.com/watch?v=KSHLTmPVSKg](https://www.youtube.com/watch?v=KSHLTmPVSKg)
