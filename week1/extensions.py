a=input("enter file name with extensions i.e. file_name.format_name: ")
a=a.lower().strip()
a=a.split(".")
if a[-1]=="gif":
    print("image/gif")
elif a[-1]=="jpg":
    print("image/jpeg")
elif a[-1]=="jpeg":
    print("image/jpeg")
elif a[-1]=="png":
    print("image/png")
elif a[-1]=="pdf":
    print("application/pdf")
elif a[-1]=="txt":
    print("text/plain")
elif a[-1]=="zip":
    print("application/zip")
else:
    print("application/octet-stream")

