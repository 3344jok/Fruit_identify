import cv2
import nanocamera as nano

camera = nano.Camera(width=640, height=480, fps=30, enforce_fps=True)
print('CSI Camera is ready? - ', camera.isReady())
try:
    while camera.isReady():
        frame = camera.read()
        cv2.imshow('video frame', frame)
        if cv2.waitKey(30) == ord('q'):
            break
finally:
        camera.release()
        del camera
        cv2.destroyAllWindows()

