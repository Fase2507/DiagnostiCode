import cv2
import os
import dis
import marshal
import binascii
import contextlib
import ast
import io
import dis
from PIL import Image, ImageDraw, ImageFont

##YUZ
source1 = """
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
            # cv2.imshow("Face Schema", schema_img)
            generated_schemas["face"] = True
        face_count += 1
"""
##GOZ
source2 = """
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
for i, (ex, ey, ew, eh) in enumerate(eyes):
    if eye_count < max_photos:
        eye_img = roi_color[ey:ey + eh, ex:ex + ew]
        eye_path = f"{output_dir}/eye_{eye_count}.jpg"
        cv2.imwrite(eye_path, eye_img)
        eye_count += 1
        break

"""
##AGIZ
source3 = """
mouths = mouth_cascade.detectMultiScale(roi_gray, 1.5, 11)
for (mx, my, mw, mh) in mouths:
    if my > h / 2 and mouth_count < max_photos:
        mouth_img = roi_color[my:my + mh, mx:mx + mw]
        mouth_path = f"{output_dir}/mouth_{mouth_count}.jpg"
        cv2.imwrite(mouth_path, mouth_img)
        mouth_count += 1
        break
"""
class Disassembler:
    def __init__(self, source,part_name):
        self.source = source
        self.part_name = part_name
        self.tree = ast.parse(source)
        self.ntr = ast.dump(self.tree, indent=4)
        self.dis_output = self.get_dis_output()
    def create_dir(self):
        part_dir=self.part_name
        if not os.path.exists(part_dir):
            os.makedirs(part_dir)

    def get_dis_output(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            dis.dis(self.ntr)
        return buffer.getvalue()

    def byteCode(self, filename):
        with open(filename, "w") as f:
            f.write(self.dis_output)
    def get_hex_code(self, output_file=None):
        bytecode = compile(self.source, self.part_name, 'exec')
        code = marshal.dumps(bytecode)
        hex_code = code.hex()
        if output_file:
            with open(output_file, 'w') as f:
                f.write(hex_code)
        return hex_code
    def parse(self, filename):
        with open(filename, "w") as f:
            f.write(self.ntr)

# Setup
# output_dir = "output"
# os.makedirs(output_dir, exist_ok=True)
max_photos = 2
face_count = eye_count = mouth_count = 0

# Load Haar cascades

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
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
        #frame1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if face_count < max_photos:
            face_img = cv2.rectangle(frame.copy(), (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.imshow('Face', face_img)
            face_path = f"Face/face_{face_count}.jpg"
            cv2.imwrite(face_path, face_img)
            Face=Disassembler(source1,"Face")
            Face.create_dir()
            Face.byteCode("Face/2face_bytecode.txt")
            Face.parse("Face/1face_parse.txt")
            output_file = 'Face/3face_hex.txt'
            Face.get_hex_code(output_file)
            face_count += 1

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        for i, (ex, ey, ew, eh) in enumerate(eyes):
            #frame2
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
            if eye_count < max_photos:
                eye_img = roi_color[ey:ey + eh, ex:ex + ew]
                eye_path = f"Eye/eye_{eye_count}.jpg"
                cv2.imwrite(eye_path, eye_img)
                Eye = Disassembler(source2,"Eye")
                Eye.create_dir()
                Eye.byteCode("Eye/2eye_bytecode.txt")
                Eye.parse("Eye/1eye_parse.txt")
                output_file = 'Eye/3eye_hex.txt'
                Eye.get_hex_code(output_file)
                eye_count += 1
                break

        # Detect mouth
        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.5, 11)
        for (mx, my, mw, mh) in mouths:
            #frame3
            cv2.rectangle(frame, (x + mx, y + my), (x + mx + mw, y + my + mh), (0, 0, 255), 2)
            if my > h / 2 and mouth_count < max_photos:
                mouth_img = roi_color[my:my + mh, mx:mx + mw]
                mouth_path = f"Mouth/mouth_{mouth_count}.jpg"
                cv2.imwrite(mouth_path, mouth_img)
                Mouth = Disassembler(source3,"Mouth")
                Mouth.create_dir()
                Mouth.byteCode("Mouth/2mouth_bytecode.txt")
                Mouth.parse("Mouth/1mouth_parse.txt")
                output_file = 'Mouth/3mouth_hex.txt'
                Mouth.get_hex_code(output_file)
                mouth_count += 1
                break

    cv2.imshow('Face, Eyes and Mouth Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


# def export_to_pdf(image_folder, pdf_path):
#     image_files = sorted([
#         f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png"))
#     ])
#
#     images = [Image.open(os.path.join(image_folder, f)).convert("RGB") for f in image_files]
#     if images:
#         images[0].save(pdf_path, save_all=True, append_images=images[1:])
#         print(f"[✓] PDF exported to: {pdf_path}")
#     else:
#         print("[!] No images found to export.")


cv2.destroyAllWindows()
# export_to_pdf(output_dir, os.path.join(output_dir, "Detection_Report.pdf"))

