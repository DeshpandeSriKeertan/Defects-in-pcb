from flask import Flask, request, render_template_string
import os
from ultralytics import YOLO

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLOv8 Model
model = YOLO("yolov8.pt")   # trained model path

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>PCB Defect Detection</title>
</head>
<body>
    <h2>PCB Defect Detection System</h2>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <br><br>
        <button type="submit">Detect Defects</button>
    </form>

    {% if input_image %}
        <h3>Uploaded PCB Image</h3>
        <img src="{{ input_image }}" width="350">
    {% endif %}

    {% if output_image %}
        <h3>Detected Defects Output</h3>
        <img src="{{ output_image }}" width="350">
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def detect():
    input_image = None
    output_image = None

    if request.method == "POST":
        file = request.files["image"]
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)

        # YOLO Detection
        results = model(image_path)

        result_path = os.path.join(RESULT_FOLDER, file.filename)
        results[0].save(filename=result_path)

        input_image = image_path
        output_image = result_path

    return render_template_string(
        HTML_PAGE,
        input_image=input_image,
        output_image=output_image
    )

if __name__ == "__main__":
    app.run(debug=True)
