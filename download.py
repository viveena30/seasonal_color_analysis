import os
import urllib.request
import zipfile

def download_and_extract(url, dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    zip_path = os.path.join(dest_path, 'wider_face.zip')
    if not os.path.exists(zip_path):
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, zip_path)
        print("Download complete!")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    print("Extraction complete!")

download_and_extract('http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/bbx_annotation/wider_face_split.zip', 'data')
download_and_extract('http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/WiderFace_Results/WIDER_train.zip', 'data')
download_and_extract('http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/WiderFace_Results/WIDER_val.zip', 'data')
download_and_extract('http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/WiderFace_Results/WIDER_test.zip', 'data')
