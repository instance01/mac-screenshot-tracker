import argparse
import subprocess
import time


def track(wait_time=60):
    # In the following, a select set of parameters that are passed to ffmpeg is
    # described:
    # -vframes -> Number of frames to output.
    # -q:v -> (alias: qscale) Quality of the output, 100 means as lossy as
    #   possible (resulting in less filesize).
    # -vf scale=1280:-1 -> Rescale to 1280 width (and automatically keep aspect
    #   ratio). Uses ffmpeg filtering.
    args = ("ffmpeg -f avfoundation -framerate 1 -i 1:0 -vframes 1 -q:v 100 "
            "-vf scale=1280:-1")
    args = args.split(" ")

    while True:
        time.sleep(wait_time)
        filename = "output" + str(int(time.time())) + ".jpeg"

        args_ = args.copy()
        args_.append(filename)

        p = subprocess.Popen(args_)
        p.wait()


def watch():
    pass  # TODO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cmd',
        nargs='?',
        default='track',
        help='Command to execute. Can be either track or watch.'
    )
    parser.add_argument(
        '--waittime',
        help='How many seconds to wait between each capture.',
        default=60,
        type=int
    )

    args = parser.parse_args()

    if args.cmd == 'track':
        track(args.waittime)
    elif args.cmd == 'watch':
        watch()
