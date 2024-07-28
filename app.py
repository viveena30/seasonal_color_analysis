# # from flask import Flask, request, render_template, redirect, url_for
# # import os
# # import cv2
# # import numpy as np
# # import mediapipe as mp

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # # Initialize Mediapipe Face Mesh
# # mp_face_mesh = mp.solutions.face_mesh
# # face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# # # Define regions using landmarks
# # # FACE_LANDMARKS = {
# # #     'left_eye': [33, 133, 155, 154, 153, 144, 145, 160, 159, 158],
# # #     'right_eye': [362, 382, 381, 380, 374, 373, 390, 249, 263, 466],
# # #     'forehead': [70, 63, 105, 66, 107, 55],
# # #     'left_cheek': [36, 39, 40, 37, 38, 202],
# # #     'right_cheek': [266, 286, 293, 300, 334, 282]
# # # }
# # FACE_LANDMARKS = {
# #     # 'left_eye': [33, 161, 160, 158, 157, 133, 154, 145, 163],
# #     # 'right_eye': [263, 388, 386, 384, 398, 362, 381, 374, 390],
# #     'left_eye': [160, 158, 153, 144],
# #     'right_eye': [ 386, 384, 381, 374], # add 390 if needed
# #     'forehead': [109, 10, 337, 151, 108, 69],
# #     'left_cheek': [123, 117, 118, 101, 50],
# #     'right_cheek': [352, 346, 330, 280]
# # }

# # def get_landmarks(image):
# #     results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# #     if not results.multi_face_landmarks:
# #         return None
# #     return results.multi_face_landmarks[0].landmark

# # def extract_region(image, landmarks, region):
# #     height, width, _ = image.shape
# #     mask = np.zeros((height, width), dtype=np.uint8)
# #     points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
# #     cv2.fillConvexPoly(mask, points, 255)
# #     return cv2.bitwise_and(image, image, mask=mask)

# # def get_average_color(region):
# #     non_black_pixels = region[np.where((region != [0, 0, 0]).all(axis=2))]
# #     if len(non_black_pixels) == 0:
# #         return None
# #     avg_color = np.mean(non_black_pixels, axis=0)
# #     return tuple(avg_color.astype(int))

# # def rgb_to_hex(rgb):
# #     return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# # def visualize_landmarks(image, landmarks):
# #     height, width, _ = image.shape
# #     for landmark in landmarks:
# #         x = int(landmark.x * width)
# #         y = int(landmark.y * height)
# #         cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
# #     return image

# # def visualize_regions(image, landmarks):
# #     height, width, _ = image.shape  # Add this line to define height and width
# #     for region in FACE_LANDMARKS:
# #         points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
# #         cv2.polylines(image, [points], True, (0, 0, 255), 2)
# #     return image

# # def process_image(image_path):
# #     image = cv2.imread(image_path)
# #     if image is None:
# #         return None  # Image failed to load
# #     landmarks = get_landmarks(image)
# #     if landmarks:
# #         image_with_landmarks = visualize_landmarks(image.copy(), landmarks)
# #         image_with_regions = visualize_regions(image_with_landmarks.copy(), landmarks)
# #         visualized_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'visualized_' + os.path.basename(image_path))
# #         cv2.imwrite(visualized_filename, image_with_regions)
        
# #         colors = {}
# #         for region in FACE_LANDMARKS:
# #             region_image = extract_region(image, landmarks, region)
# #             avg_color = get_average_color(region_image)
# #             if avg_color:
# #                 colors[region] = rgb_to_hex(avg_color)
# #         return colors, 'visualized_' + os.path.basename(image_path)
# #     else:
# #         return None, None

# # @app.route('/', methods=['GET', 'POST'])
# # def upload_file():
# #     if request.method == 'POST':
# #         if 'file' not in request.files:
# #             return redirect(request.url)
# #         file = request.files['file']
# #         if file.filename == '':
# #             return redirect(request.url)
# #         if file:
# #             filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
# #             file.save(filename)
# #             colors, visualized_filename = process_image(filename)
# #             if colors:
# #                 return render_template('result.html', colors=colors, image_url=url_for('static', filename='uploads/' + file.filename), visualized_url=url_for('static', filename='uploads/' + visualized_filename))
# #             else:
# #                 return render_template('index.html', error="No face detected or image failed to load. Please upload a different image.")
# #     return render_template('index.html')

# # @app.route('/result')
# # def result():
# #     return render_template('result.html')

# # if __name__ == "__main__":
# #     if not os.path.exists(app.config['UPLOAD_FOLDER']):
# #         os.makedirs(app.config['UPLOAD_FOLDER'])
# #     app.run(debug=True)

# from flask import Flask, request, render_template, redirect, url_for
# import os
# import cv2
# import numpy as np
# import mediapipe as mp

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Initialize Mediapipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# # Define regions using landmarks
# FACE_LANDMARKS = {
#     'left_eye': [160, 158, 153, 144],
#     'right_eye': [386, 384, 381, 374],
#     'forehead': [109, 10, 337, 151, 108, 69],
#     'left_cheek': [123, 117, 118, 101, 50],
#     'right_cheek': [352, 346, 330, 280]
# }

# def get_landmarks(image):
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = face_mesh.process(rgb_image)
#     if not results.multi_face_landmarks:
#         return None
#     return results.multi_face_landmarks[0].landmark

# def extract_region(image, landmarks, region):
#     height, width, _ = image.shape
#     mask = np.zeros((height, width), dtype=np.uint8)
#     points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
#     cv2.fillConvexPoly(mask, points, 255)
#     return cv2.bitwise_and(image, image, mask=mask)

# def get_average_color(image, landmarks, region_indices):
#     height, width, _ = image.shape
#     region_pixels = []

#     for idx in region_indices:
#         x = int(landmarks[idx].x * width)
#         y = int(landmarks[idx].y * height)
#         if 0 <= x < width and 0 <= y < height:
#             region_pixels.append(image[y, x])

#     if len(region_pixels) == 0:
#         return None

#     region_pixels = np.array(region_pixels)
#     average_color = region_pixels.mean(axis=0)

#     return tuple(average_color.astype(int))

# def rgb_to_hex(rgb):
#     return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# def visualize_landmarks(image, landmarks):
#     height, width, _ = image.shape
#     for landmark in landmarks:
#         x = int(landmark.x * width)
#         y = int(landmark.y * height)
#         cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
#     return image

# def visualize_regions(image, landmarks):
#     height, width, _ = image.shape
#     for region in FACE_LANDMARKS:
#         points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
#         cv2.polylines(image, [points], True, (0, 0, 255), 2)
#     return image

# def process_image(image_path):
#     image = cv2.imread(image_path)
#     if image is None:
#         return None
#     landmarks = get_landmarks(image)
#     if landmarks:
#         image_with_landmarks = visualize_landmarks(image.copy(), landmarks)
#         image_with_regions = visualize_regions(image_with_landmarks.copy(), landmarks)
#         visualized_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'visualized_' + os.path.basename(image_path))
#         cv2.imwrite(visualized_filename, image_with_regions)
        
#         colors = {}
#         for region in FACE_LANDMARKS:
#             avg_color = get_average_color(image, landmarks, FACE_LANDMARKS[region])
#             if avg_color:
#                 colors[region] = rgb_to_hex(avg_color)
#         return colors, 'visualized_' + os.path.basename(image_path)
#     else:
#         return None, None

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#         if file:
#             filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filename)
#             colors, visualized_filename = process_image(filename)
#             if colors:
#                 return render_template('result.html', colors=colors, image_url=url_for('static', filename='uploads/' + file.filename), visualized_url=url_for('static', filename='uploads/' + visualized_filename))
#             else:
#                 return render_template('index.html', error="No face detected or image failed to load. Please upload a different image.")
#     return render_template('index.html')

# @app.route('/result')
# def result():
#     return render_template('result.html')

# if __name__ == "__main__":
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     app.run(debug=True)

from flask import Flask, request, render_template, redirect, url_for
import os
import cv2
import numpy as np
import mediapipe as mp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# Define regions using landmarks
FACE_LANDMARKS = {
    'left_eye': [160, 158, 153, 144],
    'right_eye': [386, 384, 381, 374],
    'forehead': [109, 10, 337, 151, 108, 69],
    'left_cheek': [123, 117, 118, 101, 50],
    'right_cheek': [352, 346, 330, 280]
}

def get_landmarks(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)
    if not results.multi_face_landmarks:
        return None
    return results.multi_face_landmarks[0].landmark

def extract_region(image, landmarks, region):
    height, width, _ = image.shape
    mask = np.zeros((height, width), dtype=np.uint8)
    points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
    cv2.fillConvexPoly(mask, points, 255)
    return cv2.bitwise_and(image, image, mask=mask)

def get_average_color(image, landmarks, region_indices):
    height, width, _ = image.shape
    region_pixels = []

    for idx in region_indices:
        x = int(landmarks[idx].x * width)
        y = int(landmarks[idx].y * height)
        # Ensure the coordinates are within the image bounds
        if 0 <= x < width and 0 <= y < height:
            region_pixels.append(image[y, x])

    # Debug: Print the region pixels
    print(f"Region Pixels: {region_pixels}")

    if len(region_pixels) == 0:
        return None

    # Compute the average color of the selected region
    region_pixels = np.array(region_pixels)
    average_color = region_pixels.mean(axis=0)

    # Debug: Print the average color in BGR and RGB
    print(f"Average Color (BGR): {average_color}")
    average_color_rgb = average_color[::-1]  # Convert BGR to RGB
    print(f"Average Color (RGB): {average_color_rgb}")

    return tuple(average_color_rgb.astype(int))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def visualize_landmarks(image, landmarks):
    height, width, _ = image.shape
    for landmark in landmarks:
        x = int(landmark.x * width)
        y = int(landmark.y * height)
        cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
    return image

def visualize_regions(image, landmarks):
    height, width, _ = image.shape
    for region in FACE_LANDMARKS:
        points = np.array([(int(landmarks[idx].x * width), int(landmarks[idx].y * height)) for idx in FACE_LANDMARKS[region]], dtype=np.int32)
        cv2.polylines(image, [points], True, (0, 0, 255), 2)
    return image

def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    landmarks = get_landmarks(image)
    if landmarks:
        image_with_landmarks = visualize_landmarks(image.copy(), landmarks)
        image_with_regions = visualize_regions(image_with_landmarks.copy(), landmarks)
        visualized_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'visualized_' + os.path.basename(image_path))
        cv2.imwrite(visualized_filename, image_with_regions)
        
        colors = {}
        for region in FACE_LANDMARKS:
            avg_color = get_average_color(image, landmarks, FACE_LANDMARKS[region])
            if avg_color:
                colors[region] = rgb_to_hex(avg_color)
        return colors, 'visualized_' + os.path.basename(image_path)
    else:
        return None, None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            colors, visualized_filename = process_image(filename)
            if colors:
                return render_template('result.html', colors=colors, image_url=url_for('static', filename='uploads/' + file.filename), visualized_url=url_for('static', filename='uploads/' + visualized_filename))
            else:
                return render_template('index.html', error="No face detected or image failed to load. Please upload a different image.")
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
