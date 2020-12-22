import requests
from sys import stdout

#cookiesString = 'CloudFront-Key-Pair-Id=K33HSRY3XILYEV; uid=XKAxNPbEjnRtcxDPkcMfjqktth23; last-domain=virtual.spwn.jp; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIwMTIyMS0yMjAxLWhvbG9saXZlLTJuZGZlcy9ncnAxL2NhbTFfdjEvKiIsIkNvbmRpdGlvbiI6eyJJcEFkZHJlc3MiOnsiQVdTOlNvdXJjZUlwIjoiMC4wLjAuMC8wIn0sIkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjEwMzc3MTk5fX19XX0_; CloudFront-Signature=imLT0V14FI7rOYZdR18W9-vEcmdoD7jCgwH2HbxWAJFcWrRNg7TgA-~vkIkSynRbY7fzct-BdrmbIHhaSrjgHlP9~ooC1e-gZGSKTo4ltJzvpveSl4-LhpFo8rfLWbpvdZ0-I4mL~dwfAt7qlXqDUXotb4uiQ00uw35sw7FRBU059ZFhnDOuJoZXoug2POy6gsg8K1Ozn-SRu8XtOQPmH6wp71iRi~Q8W-izclZeijUNOkR8HS8SILN6UKZ4qdOP0WFjnoXgvb2DQrtcUUgDMcDUWfjfhBEEe~ZoHdO1N~vZsw8lyjLr9qJDMOwVqq0bZwswr83syZrrnjBi94ST1A__'
cookiesString = 'CloudFront-Key-Pair-Id=K33HSRY3XILYEV; uid=XKAxNPbEjnRtcxDPkcMfjqktth23; last-domain=virtual.spwn.jp; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIwMTIyMS0yMjAxLWhvbG9saXZlLTJuZGZlcy9ncnAyL2NhbTJfdjEvKiIsIkNvbmRpdGlvbiI6eyJJcEFkZHJlc3MiOnsiQVdTOlNvdXJjZUlwIjoiMC4wLjAuMC8wIn0sIkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjEwMzc3MTk5fX19XX0_; CloudFront-Signature=YykW6EzkuouvEqSyPctZ4Ik4Vcnw34S9YmlU18IuypUq-RvDbuoeuYHC0kbRb1N1BCNXXL3JAnOzl-bwwVyV47Xj8RYgKUPjDdrjMyd~uePBTTBa9vPqwqcKyRDdIhL~lhi801m82zViSWJxd-CrDetylY3JN9CiSbaxfHzE-Y21gYjNKfSPtLXfOQ9W8DyUIxxLICbO9J5NH1IPHIeXLzT7BTfWF8d6AT0UoE~2Re2EdUYY91wTWj0ViPlhF6f3MhUuhpB6ZD6TabKBT-HR95M9ofBXOiKY4pv3tpeA~UWMR1gKpcHcPUxl7PHYuz6ANYHV6PJpTXJNZNAF2ipRug__'
stage1BaseUrl = 'https://vod2.spwn.jp/spwn-vod2/201221-2201-hololive-2ndfes/grp1/cam1_v1/'
stage1Path = "stage1\\index_12.m3u8"


stage2BaseUrl = 'https://vod2.spwn.jp/spwn-vod2/201221-2201-hololive-2ndfes/grp2/cam2_v1/'
stage2Path = "stage2\\index_12.m3u8"
stage2Folder = "stage2\\"

def ParseCookies(cookieString):
    cookiesString = cookieString.replace(" ","")
    cookiesList = cookiesString.split(";")
    cookies = {}
    for cookie in cookiesList:
        temp = cookie.split("=")
        cookies[temp[0]] = temp[1]
    return cookies



def ReadM3U8(filePath):
    f = open(filePath)
    lines = f.readlines()
    f.close()
    fileList = []
    next = False
    for line in lines:
        if next:
            fileList.append(line.strip("\n"))
        if line.startswith("#EXTINF"):
            next = True
        else:
            next = False
    return fileList

def GetFile(fileName,my_cookies):
    url = stage2BaseUrl + fileName
    fileName = stage2Folder+fileName
    f = open(fileName, 'wb')
    r = requests.get(url,cookies=my_cookies)
    print(r)
    for chunk in r.iter_content(chunk_size=8192): 
        f.write(chunk)

    f.close()
    

def main(): 
    cookies = ParseCookies(cookiesString)
    fileList = ReadM3U8(stage2Path)
    GetFile(fileList[0],cookies)
    for file in fileList:
        GetFile(file,cookies)


if __name__ == '__main__':
    main()