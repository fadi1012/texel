class FreezeOutput:
    def __init__(self, videos, all_videos_freeze_frame_synced):
        self.videos = videos
        self.all_videos_freeze_frame_synced = all_videos_freeze_frame_synced

    def to_dict(self):
        videos = [video.__dict__ for video in self.videos]
        return {'all_videos_freeze_frame_synced': self.all_videos_freeze_frame_synced, 'videos': videos}


class VideoOutput:
    def __init__(self, valid_periods, longest_valid_period, valid_video_percentage):
        self.valid_periods = valid_periods
        self.longest_valid_period = longest_valid_period
        self.valid_video_percentage = valid_video_percentage
