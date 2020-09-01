import requests
import os

TASK_DIR = os.path.abspath(os.curdir)
VIDEO_FILES_DIR = TASK_DIR + '/videos'
VIDEO_OUTPUT_FILES_DIR = TASK_DIR + '/output'
video_files_urls = ["https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"]


def download_video_file(video_url=None):
    if not os.path.exists(VIDEO_FILES_DIR):
        os.makedirs(VIDEO_FILES_DIR)
    video_path = VIDEO_FILES_DIR + "/" + video_url.split("/hiring_process_data/")[1]
    if not os.path.exists(video_path):
        request = requests.get(video_url)
        open(video_path, 'wb').write(request.content)
    return video_path


def expose_video_output(video_path, n=0.003, d=2):
    if not os.path.exists(VIDEO_OUTPUT_FILES_DIR):
        os.makedirs(VIDEO_OUTPUT_FILES_DIR)
    output_text_file_path = VIDEO_OUTPUT_FILES_DIR + "/" + video_path.split("videos/")[1].replace("mp4", "txt")
    call_with_args = './ffmpeg -i %s -vf "freezedetect=n=%s:d=%s,metadata=mode=print:file=%s" -map 0:v:0 -f null -' % \
                     (video_path, n, d, output_text_file_path)
    os.system(call_with_args)
    return output_text_file_path


def get_video_valid_periods(output_file):
    valid_periods_list = []
    valid_period_start = 0
    with open(output_file, 'r') as file:
        for line in file:
            if 'freeze_start' in line:
                freeze_start_value = float("{:.2f}".format(float(line.split("=")[1].replace("\n", ""))))
                if freeze_start_value != 0:
                    valid_periods_list.append((valid_period_start, freeze_start_value))
            elif 'freeze_end' in line:
                valid_period_start = float("{:.2f}".format(float(line.split("=")[1].replace("\n", ""))))
    return valid_periods_list


def main():
    valid_video_periods_list = []
    for video_url in video_files_urls:
        video = download_video_file(video_url)
        output_file = expose_video_output(video)
        valid_video_periods_list.append(get_video_valid_periods(output_file))
    print(valid_video_periods_list)


if __name__ == "__main__":
    main()
