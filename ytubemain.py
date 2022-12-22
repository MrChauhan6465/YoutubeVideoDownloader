import pytube as pt 



link = input("Enter The  Youtube Video Link :")

res = pt.YouTube(link)

print(res.title)

videos = res.streams.all()
vid = enumerate(videos)
for i in vid:
    print(i)
print()

strm = int(input("\nEnter : "))
videos[strm].download()
print('successfully downloaded !')