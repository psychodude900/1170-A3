For Reference: Code has been reused from A1 and A2

# Website file structure

|A3/
|------
	|
	|--src/
     	|  |
	|  |----Audio/
	|  |				  
	|  |----Images/
	|  | 
	|  |----Projects/
	|  |
	|  |----Videos/
	|  |
	|  |----contact.html
	|  |
	|  |----index.html
	|  |
	|  |----projects.html
	|  |
	|  |----resume.html
	|  |
	|  |----styles.css
	   |
	   |----script.js
      

# list of assets

Images:

1. DalLogo.jpg
2. EHcertificate.pnh
3. FishNShark.png
4. KnightIcon.png
5. NES.jpg
6. nature1.jpg
7. nature2.jpg
8. nature3.jpg
9. nature4.jpg

Projects:

1. FishNShark.py

Videos:

1. GradVid.mp4

Audio:

1. IntroAudio.mp3

# citations

In A2/src/resume.html line 28 I sourced an image of New English School, Kuwait building from New English School parental portal website and uploaded it to A2/src/Images as NES.jpg [1].

In A2/src/resume.html line 41 I sourced an image of Dalhousie University's logo from AACSB and uploaded it to A2/src/Images as DalLogo.jpg [2].

In A2/src/index.html lines 18-20 I used the <audio controls> tag to upload an audio of an AI explaining the contents of the websites which I got from TTSMP3 which is a free text to mp3 AI reader [3]. The audio has pause, unpause and volume controls, a download option and a playback speed function.

Website's fav icon is of the knight black chess piece from the nooun project website [4]. 

Nature Images used in src/gallery.html are sourced from multiple free stock image websites [5][6][7][8]


# References

[1] New English School. 2020. Retrieved February 9 2023 from https://accounts.neskuwait.com/

[2] AACSB Dalhousie University. Retrieved February 9 2023 from https://www.aacsb.edu/accredited/d/dalhousie-university

[3] TTSMP3. 2023. Retrieved February 9 2023 from https://ttsmp3.com/

[4] Hea Poh Lin. 2016. (August 15 2016). Retrieved February 9 2023 from https://thenounproject.com/icon/chess-knight-589743/

[5] James Wheeler. 2017. (May 10 2017). Retrieved April 6 2023 from https://pixabay.com/photos/alberta-canada-lake-mountains-2297204/

[6] Unknown owner. 2019. Retrieved April 6 from https://www.freepik.com/premium-photo/beautiful-emerald-lake-yoho-national-park-british-columbia-canada_5573421.htm#query=nature&position=43&from_view=keyword&track=sph

[7] Lubomir Chudoba. 2019. Retrieved April 6 2023 from https://www.dreamstime.com/stock-photo-moraine-lake-banff-national-park-canadian-rockies-canada-beautiful-sunny-summer-day-amazing-blue-sky-majestic-mountains-image85168809

[8] Simon Berger. 2017. (July 21 2017). Retrieved April 6 2023 from https://unsplash.com/photos/aZjw7xI3QAA

# code functions

script.js line 1: notifOnSubmit():

This function stores the String value of a textarea and uses a conditional statement to determine the type of notification alert to display based on the length of the String. If the string has a length less than 1, it means that it is empty and so an alert will go off accordingly.

script.js line 10 : colScheme():

This function stores all elements used in CSS in an array called elements. For each element in that array the background, accent and text colors will change when a displayed color scheme is clicked on the webpage. There are certain exceptions to this condition such as the color scheme buttons themselves are to remain visible in their true color in all schemes to maintain the ability to change. Another exception are any buttons created that adapt the accent color of the page. This is to avoid them blending in with the background.
