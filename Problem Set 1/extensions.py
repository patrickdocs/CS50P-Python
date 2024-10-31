extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

def main():
    filename = str(input("File name: ")).lower()
    for extension in extensions:
        if extension in filename:
            return (extensions.get(extension))
            break
    return ("application/octet-stream")

print(main())
#check50 cs50/problems/2022/python/extensions
