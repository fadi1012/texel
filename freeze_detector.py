import requests
import os

TASK_DIR = os.path.abspath(os.curdir)
video_files_urls = ["https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"]


def download_video_files(video_files=None):
    video_files = video_files or video_files_urls
    for video_url in video_files:
        video_path = TASK_DIR + "/" + video_url.split("/hiring_process_data/")[1]
        if not os.path.exists(video_path):
            request = requests.get(video_url)
            open(video_path, 'wb').write(request.content)


def main():
    download_video_files()


if __name__ == "__main__":
    main()
