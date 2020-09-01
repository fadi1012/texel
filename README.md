# Texel's Home Assignment

# steps to run locally:
- 1) you can run freeze_detector.py locally but activating texelvenv is needed:
-     source texelvenv/bin/activate
-     python freeze_detector.py

- 2) you can run docker container :
-     docker build -t freezedetector .
-     docker run freezedetector

# freeze_detector.py:
- main file that contains the task requirements

# freeze_output.py:
- contains case classes for the final generated json object

# video_utils.py
- contain utils method to download a video by url and to generate 
- video output using ffmpeg cli with freezedetector filter