from deepface import DeepFace
import cv2

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Optional: make detection faster by resizing
    frame_resized = cv2.resize(frame, (640, 480))

    try:
        # Analyze emotions in the frame
        result = DeepFace.analyze(frame_resized, actions=['emotion'], enforce_detection=False)

        # Handle result format (dict or list)
        if isinstance(result, list):
            result = result[0]

        dominant_emotion = result['dominant_emotion']

        # Display emotion on frame
        cv2.putText(frame_resized, f"Emotion: {dominant_emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except Exception as e:
        print("Error:", e)

    # Show the live video
    cv2.imshow("Live Emotion Detection", frame_resized)

    # Quit when pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
