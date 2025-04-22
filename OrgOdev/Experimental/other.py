import cv2
import os
from PIL import Image, ImageDraw, ImageFont

# Setup
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
max_photos = 3
face_count = eye_count = mouth_count = 0

# Load Haar cascades

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# Schema generation function
generated_schemas = {
    "face": False,
    "eye": False,
    "mouth": False
}


def generate_detection_schema(output_path, feature="face", image_path=None):
    logic_blocks = {
        "face": {
            "Python Code": "face_cascade.detectMultiScale(gray, 1.3, 5)",
            "C Code": "cvHaarDetectObjects(gray, cascade, ...)",
            "Assembly": "LOOP -> CMP pixel intensity -> JMP",
            "Machine Code": "3C 7F | 7F 05 | EB 03 ...",
            "Output": "Detected face: x, y, width, height"
        },
        "eye": {
            "Python Code": "eye_cascade.detectMultiScale(roi_gray, 1.1, 10)",
            "C Code": "cvHaarDetectObjects(eye ROI, cascade, ...)",
            "Assembly": "SCAN ROI -> CMP brightness -> JMP if shape",
            "Machine Code": "3C 5F | 7E 04 | EB 02 ...",
            "Output": "Detected eye: ex, ey, ew, eh"
        },
        "mouth": {
            "Python Code": "mouth_cascade.detectMultiScale(roi_gray, 1.5, 11)",
            "C Code": "cvHaarDetectObjects(mouth ROI, ...)",
            "Assembly": "LOOP over lower half -> CMP -> JMP",
            "Machine Code": "3C 60 | 7C 03 | EB 01 ...",
            "Output": "Detected mouth: mx, my, mw, mh"
        }
    }

    # Image size
    width, height = 900, 600
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    # Draw title
    draw.text((width//2 - 100, 10), f"{feature.upper()} DETECTION LOGIC", fill="black", font=font)

    # Starting Y coordinate for the blocks
    y = 60
    x_offset = 40

    # First: draw the image preview if available
    if image_path and os.path.exists(image_path):
        try:
            part_img = Image.open(image_path).resize((200, 140))
            image.paste(part_img, (x_offset, y))
        except:
            draw.text((x_offset, y), "[Image could not be loaded]", fill="red", font=font)
    draw.text((x_offset + 220, y + 50), "Image ➝ Input to Detection Pipeline", fill="black", font=font)
    y += 160  # Move down for logic

    # Draw logic text
    logic = logic_blocks.get(feature, {})
    for title, desc in logic.items():
        draw.text((x_offset, y), f"{title} ➝ {desc}", fill="black", font=font)
        y += 60

    # Save schema
    image.save(output_path)


# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        if face_count < max_photos:
            face_img = cv2.rectangle(frame.copy(), (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_path = f"{output_dir}/face_{face_count}.jpg"
            cv2.imwrite(face_path, face_img)
            if not generated_schemas["face"]:
                schema_path = f"{output_dir}/face_schema.png"
                generate_detection_schema(schema_path, feature="face", image_path=face_path)
                schema_img = cv2.imread(schema_path)
                cv2.imshow("Face Schema", schema_img)
                generated_schemas["face"] = True
            face_count += 1

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        for i, (ex, ey, ew, eh) in enumerate(eyes):
            if eye_count < max_photos:
                eye_img = roi_color[ey:ey + eh, ex:ex + ew]
                eye_path = f"{output_dir}/eye_{eye_count}.jpg"
                cv2.imwrite(eye_path, eye_img)
                if not generated_schemas["eye"]:
                    schema_path = f"{output_dir}/eye_schema.png"
                    generate_detection_schema(schema_path, feature="eye",image_path=eye_path)
                    schema_img = cv2.imread(schema_path)
                    cv2.imshow("Eye Schema", schema_img)
                    generated_schemas["eye"] = True
                eye_count += 1
                break

        # Detect mouth
        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.5, 11)
        for (mx, my, mw, mh) in mouths:
            if my > h / 2 and mouth_count < max_photos:
                mouth_img = roi_color[my:my + mh, mx:mx + mw]
                mouth_path = f"{output_dir}/mouth_{mouth_count}.jpg"
                cv2.imwrite(mouth_path, mouth_img)
                if not generated_schemas["mouth"]:
                    schema_path=f"{output_dir}/mouth_schema.jpg"
                    generate_detection_schema(schema_path, feature="mouth",image_path=mouth_path)
                    schema_img = cv2.imread(schema_path)
                    cv2.imshow("Mouth Schema", schema_img)
                    generated_schemas["mouth"] = True
                mouth_count += 1
                break

    cv2.imshow('Face, Eyes and Mouth Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


def export_to_pdf(image_folder, pdf_path):
    image_files = sorted([
        f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png"))
    ])

    images = [Image.open(os.path.join(image_folder, f)).convert("RGB") for f in image_files]
    if images:
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        print(f"[✓] PDF exported to: {pdf_path}")
    else:
        print("[!] No images found to export.")


cv2.destroyAllWindows()
export_to_pdf(output_dir, os.path.join(output_dir, "Detection_Report.pdf"))

