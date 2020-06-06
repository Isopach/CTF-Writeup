import zipfile
import glob 

zipfile_list = glob.glob("*.zip")
zipfile_list.sort(key=len, reverse=True)

for i in range(0,len(zipfile_list)):

    archive = zipfile.ZipFile(zipfile_list[i], 'r')

    infolist = archive.infolist()
    for info in infolist:
        print(info.comment)
