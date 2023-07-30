import requests

def dz1():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        data = response.json()
        for i in range(len(data)):
            if data[i]['name'] == "Hulk" or data[i]['name'] == "Captain America" or data[i]['name'] == "Thanos":
                if data[i]['name'] == "Hulk":
                    intel_Hulk = data[i]["powerstats"]["intelligence"]
                elif data[i]['name'] == "Captain America":
                    intel_CapAm = data[i]["powerstats"]["intelligence"]
                else:
                    intel_Thanos = data[i]["powerstats"]["intelligence"]

    if intel_Hulk > intel_CapAm and intel_Hulk > intel_Thanos:
        print("Hulk is the smartest")
    elif intel_CapAm > intel_Hulk and intel_CapAm > intel_Thanos:
        print("Captain America is the smartest")
    else:
        print("Thanos is the smartest")

def dz2():
    def namefile(path_to_file):
        elem=path_to_file.rfind('\\')
        name=path_to_file[elem+1:]
        return name

    class YaUploader:
        def __init__(self, token: str):
            self.token = token


        def upload(self, file_path: str):
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {"path": "/" + namefile(path_to_file)}
            headers = {"Authorization": "OAuth " + token}
            response=requests.get(url,headers=headers,params=params)
            if 200 <= response.status_code < 300:
                data=response.json()
            url=data["href"]
            with open(path_to_file, "rb") as f:
                requests.post(url,files={"file": f})

    if __name__ == '__main__':

        path_to_file = input("Введите путь к файлу для загрузки: ")
        token = input("Введите ваш токен: ")
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file)


dz1()
dz2()