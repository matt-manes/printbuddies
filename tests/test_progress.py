import time

import printbuddies


def test__progress_track():
    for _ in printbuddies.track(range(10)):
        time.sleep(0.25)


def test__progress_Progress():
    with printbuddies.Progress() as progress:
        task = progress.add_task(f"<>ProggyWoggy<>", total=500)
        while not progress.finished:
            time.sleep(0.01)
            progress.update(task, advance=1)
    with printbuddies.Progress() as progress:
        task = progress.add_task(suffix=f"<>ProggyWoggy<>", total=500)
        while not progress.finished:
            time.sleep(0.01)
            progress.update(task, advance=1)
