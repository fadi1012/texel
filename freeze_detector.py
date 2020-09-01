import requests
import os

TASK_DIR = os.path.abspath(os.curdir)
video_files_urls = ["https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"]


def download_video_files(video_files=None):
    videos_list = []
    video_files = video_files or video_files_urls
    for video_url in video_files:
        video_path = TASK_DIR + "/" + video_url.split("/hiring_process_data/")[1]
        if not os.path.exists(video_path):
            request = requests.get(video_url)
            open(video_path, 'wb').write(request.content)
        videos_list.append(video_path)
    return videos_list


def expose_video_output(video_path, n=0.003, d=2):
    output_text_file_path = video_path.replace("mp4", "txt")
    call_with_args = './ffmpeg -i %s -vf "freezedetect=n=%s:d=%s,metadata=mode=print:file=%s" -map 0:v:0 -f null -' % \
                     (video_path, n, d, output_text_file_path)
    os.system(call_with_args)
    file_output_path = TASK_DIR + '/' + output_text_file_path
    return file_output_path


def main():
    files_output_path = []
    videos_list = download_video_files()
    for video in videos_list:
        files_output_path.append(expose_video_output(video))


if __name__ == "__main__":
    main()
