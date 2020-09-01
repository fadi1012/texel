import requests
import os

TASK_DIR = os.path.abspath(os.curdir)
VIDEO_FILES_DIR = TASK_DIR + '/videos'
VIDEO_OUTPUT_FILES_DIR = TASK_DIR + '/output'


def download_video_file(video_url=None):
    if not os.path.exists(VIDEO_FILES_DIR):
        os.makedirs(VIDEO_FILES_DIR)
    video_path = VIDEO_FILES_DIR + "/" + video_url.split("/hiring_process_data/")[1]
    if not os.path.exists(video_path):
        request = requests.get(video_url)
        open(video_path, 'wb').write(request.content)
    return video_path


# this method uses ffmpeg cli with freezedetect filter and exposes video freeze detection
# https://ffmpeg.org/ffmpeg-filters.html#freezedetect
def expose_video_output(video_path, n=0.003, d=2):
    if not os.path.exists(VIDEO_OUTPUT_FILES_DIR):
        os.makedirs(VIDEO_OUTPUT_FILES_DIR)
    output_text_file_path = VIDEO_OUTPUT_FILES_DIR + "/" + video_path.split("videos/")[1].replace("mp4", "txt")
    call_with_args = './ffmpeg -i %s -vf "freezedetect=n=%s:d=%s,metadata=mode=print:file=%s" -map 0:v:0 -f null -' % \
                     (video_path, n, d, output_text_file_path)
    os.system(call_with_args)
    return output_text_file_path
