from datetime import datetime

from picamera import PiCamera


camera = PiCamera()


def capture_image():
    dt = datetime.now().strftime('%Y-%m-%d.%H:%M:%S')
    image_path = '/tmp/image.{}.jpg'.format(dt)
    camera.capture(image_path)

    return image_path


def capture_video(duration=10):
    dt = datetime.now().strftime('%Y-%m-%d.%H:%M:%S')
    video_path = '/tmp/video.{}.h264'.format(dt)
    camera.start_recording(video_path)
    camera.wait_recording(duration)
    camera.stop_recording()

    return video_path
