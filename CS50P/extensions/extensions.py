import sys

type = input("Filename: ").strip().lower()

found = type.rfind(".")


if found == -1:
    print("application/octet-stream")
    sys.exit()

type = type[found + 1:]

if type == "gif":
    print("image/gif")
elif type == "jpeg" or type == "jpg":
    print("image/jpeg")
elif type == "png":
    print("image/png")
elif type == "pdf":
    print("application/pdf")
elif type == "zip":
    print("application/zip")
elif type == "txt":
    print("text/plain")
else:
    print("application/octet-stream")


