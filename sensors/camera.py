from datetime import datetime

from picamera import PiCamera


def capture_image():
    try:
        with PiCamera() as camera:
            camera.rotation = 180
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            image_path = '/tmp/image {}.jpeg'.format(dt)
            camera.capture(image_path)
        return image_path
    except:
        return None


def capture_video(duration=10):
    try:
        with PiCamera() as camera:
            camera.rotation = 180
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            video_path = '/tmp/video {}.h264'.format(dt)
            camera.start_recording(video_path)
            camera.wait_recording(duration)
            camera.stop_recording()
        return video_path
    except:
        return None
