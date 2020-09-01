from freeze_output import VideoOutput, FreezeOutput
from video_utils import download_video_file, expose_video_output
import json

video_files_urls = ["https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4",
                    "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"]


# This method goes over videos output file and returns
# VideoOutput Object that contains :
# list of all valid periods of the stream,
# longest valid period of the stream
# valid_video_percentage of the stream
def get_video_valid_periods(output_file):
    valid_periods_list = []
    valid_period_start = 0
    longest_valid_period = 0
    total_valid_video_period = 0
    with open(output_file, 'r') as file:
        for line in file:
            if 'freeze_start' in line:
                freeze_start_value = float("{:.2f}".format(float(line.split("=")[1].replace("\n", ""))))
                if freeze_start_value != 0:
                    valid_periods_list.append((valid_period_start, freeze_start_value))
                    # Determine the longest period of valid video
                    valid_period = freeze_start_value - valid_period_start
                    if valid_period > longest_valid_period:
                        longest_valid_period = valid_period
                    # sums total valid periods of the stream
                    total_valid_video_period += valid_period
            elif 'freeze_end' in line:
                valid_period_start = float("{:.2f}".format(float(line.split("=")[1].replace("\n", ""))))
        # for simplicity last freeze end is the total duration of the stream
        total_stream_duration = valid_period_start
        # calc percentage of all aggregated valid video periods over the entire duration of the stream
        total_valid_video_percentage = float("{:.2f}".format(total_valid_video_period * 100 / total_stream_duration))
    return VideoOutput(valid_periods=valid_periods_list, longest_valid_period=longest_valid_period, valid_video_percentage=total_valid_video_percentage)


# This method determines whether the entire video set is synced freeze-frame wise,
def check_if_synced_frame_freeze(videos_output):
    total_valid_periods = -1
    # check if all videos have the same amount of valid periods,
    for value in videos_output:
        valid_period_count = len(value.valid_periods)
        if total_valid_periods == -1:
            total_valid_periods = valid_period_count
        elif valid_period_count != total_valid_periods:
            return False
    # check each period's corresponding 'start' or 'end' cross all videos
    # and validate are no more than 500 ms apart.
    for i in range(total_valid_periods):
        for j in range(len(videos_output)):
            for k in range(j + 1, len(videos_output)):
                period1 = videos_output[j].valid_periods[i]
                period2 = videos_output[k].valid_periods[i]
                if not check_synced_periods(period1, period2):
                    return False
    return True


def check_synced_periods(period1, period2):
    if abs(period1[0] - period2[0]) > 0.5:
        return False
    if abs(period1[1] - period2[1]) > 0.5:
        return False
    return True


def main():
    valid_video_periods_list = []
    for video_url in video_files_urls:
        video = download_video_file(video_url)
        output_file = expose_video_output(video)
        valid_video_periods_list.append(get_video_valid_periods(output_file))
    synced_frame = check_if_synced_frame_freeze(valid_video_periods_list)
    freeze_output_obj = FreezeOutput(videos=valid_video_periods_list, all_videos_freeze_frame_synced=synced_frame)
    print(json.dumps(freeze_output_obj.to_dict()))


if __name__ == "__main__":
    main()
