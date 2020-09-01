import unittest
from freeze_detector import check_synced_periods, get_video_valid_periods
from freeze_output import VideoOutput
import os


class TestCheckSyncedPeriods(unittest.TestCase):

    def test_check_synced_periods(self):
        assert not check_synced_periods(period1=(1.02, 2), period2=(2, 3))
        assert check_synced_periods(period1=(1.52, 2), period2=(1.02, 2))
        assert not check_synced_periods(period1=(1.4, 2.7), period2=(1.02, 2))


class TestCheckVideoValidPeriods(unittest.TestCase):
    video_files_urls = ["https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4",
                        "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4",
                        "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"]

    def test_check_video_valid_periods(self, file_path=None, expected_data=None):
        file_path = file_path or os.path.dirname(os.getcwd()) + "/output/freeze_frame_input_a.txt"
        expected_data = expected_data or VideoOutput(longest_valid_period=4.5, valid_video_percentage=38.79,
                                                     valid_periods=[(0, 4.5),(10.43, 12.01), (14.25, 18.02)])
        video_object = get_video_valid_periods(file_path)
        assert video_object.longest_valid_period == expected_data.longest_valid_period
        assert video_object.valid_video_percentage == expected_data.valid_video_percentage
        assert len(video_object.valid_periods) == len(expected_data.valid_periods)
        for index, period in enumerate(video_object.valid_periods):
            assert period == expected_data.valid_periods[index]
