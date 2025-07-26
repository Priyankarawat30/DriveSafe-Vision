import requests, bz2, os

url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
print("Downloading (~100 MB)...")
resp = requests.get(url, stream=True)
with open("model.bz2", "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        f.write(chunk)

print("Extracting...")
with open("model.bz2", "rb") as f_in:
    data = bz2.decompress(f_in.read())
with open("shape_predictor_68_face_landmarks.dat", "wb") as f_out:
    f_out.write(data)

os.remove("model.bz2")
print("Done: shape_predictor_68_face_landmarks.dat")
