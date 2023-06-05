from tasks import download

url = "https://example.com"
filename = "example.html"

result = download.delay(url, filename)  # Menjalankan tugas secara asinkronus
print("Menjalankan task!!")
print(f"Task ID: {result.id}")
