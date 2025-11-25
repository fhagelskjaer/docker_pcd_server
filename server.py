
from flask import Flask, request, send_file
import os
import open3d as o3d

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/process_pcd', methods=['POST'])
def process_pcd():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Load point cloud using Open3D
    pcd = o3d.io.read_point_cloud(input_path)

    # Apply voxel downsampling (reduce density)
    downsampled_pcd = pcd.voxel_down_sample(voxel_size=0.02)

    # Save processed point cloud
    output_path = os.path.join(PROCESSED_FOLDER, f"processed_{file.filename}")
    o3d.io.write_point_cloud(output_path, downsampled_pcd)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

