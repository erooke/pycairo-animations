from subprocess import DEVNULL, PIPE, Popen

DEFAULT_FPS = 24
DEFAULT_OUTPUT_PATH = "video.mkv"


class VideoWriter:
    def __init__(self, fps=DEFAULT_FPS, output_path=DEFAULT_OUTPUT_PATH):
        args = [
            "ffmpeg",
            "-y",
            "-f",
            "image2pipe",
            "-vcodec",
            "png",
            "-framerate",
            str(fps),
            "-i",
            "-",
            "-vcodec",
            "libx264",
            output_path,
        ]

        self.process = Popen(args, stdin=PIPE, stdout=DEVNULL, stderr=DEVNULL)

    def add_frame(self, frame):
        frame.write_to_png(self.process.stdin)

    def __del__(self):
        self.process.stdin.close()
        self.process.wait()
