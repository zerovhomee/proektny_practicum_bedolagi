import cv2
from ultralytics import YOLO

def process_live_feed_yolo(model, show_video=True):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Ошибка: Не удалось открыть веб-камеру.")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            results = model.track(frame, persist=True, iou=0.65, conf=0.8,
                                  tracker="botsort.yaml", imgsz=640, verbose=False)
            annotated_frame = results[0].plot()

            if show_video:
                annotated_frame = cv2.resize(annotated_frame, (annotated_frame.shape[1] * 2, annotated_frame.shape[0] * 2))
                cv2.imshow("YOLOv8 Tracking", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    
def f():
    model = YOLO('best.pt')
    process_live_feed_yolo(model)