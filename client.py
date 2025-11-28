
import requests

url = "http://localhost:8080/process_pcd"

file_path = "example.pcd"

with open(file_path, 'rb') as f:
    response = requests.post(url, files={'file': f})

if response.status_code == 200:
    with open("returned.pcd", 'wb') as out_file:
        out_file.write(response.content)
    print("Processed PCD received and saved as returned.pcd")
else:
    print("Error:", response.text)

