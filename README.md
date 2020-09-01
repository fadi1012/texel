# Texel's Home Assignment

# steps to run locally:
- 1) you can run freeze_detector.py locally but activating texelvenv is needed:
-     source texelvenv/bin/activate
-     python freeze_detector.py
- after running from clean env you'll see two new dir's
- output and videos

- 2) you can run docker container :
-     docker build -t freezedetector .
-     docker run freezedetector
- currently there is an issue that files from container are not copied to host

# freeze_detector.py:
- main file that contains the task requirements it 
- eventually create a json file that contains the requested data
- under output dir
- you can see all the downloaded videos under videos dir
- all the output text files are located under output dir

# freeze_output.py:
- contains case classes for the final generated json object

# video_utils.py
- contain utils method to download a video by url and to generate 
- video output using ffmpeg cli with freezedetector filter


# under tests folder:
- you can run freeze_detector_test.py which is a simple unittest
- that validates the following:
- if the calc of synced period method return correct values
- a test method that can get a file and it's expected output
- then it compares the date


# TODO/Improvements:
- add more tests coverage
- create a docker file for running tests
- fix the issue that when running the docker container
- it's not creating output/videos files and it's content in the project
- it's currently added inside the container
- need to copy files from container to host