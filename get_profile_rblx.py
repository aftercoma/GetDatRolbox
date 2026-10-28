#!/usr/bin/python3.14
import argparse,requests,json
data1 = []
data2 = []
data3 = []
class parse():
    global temp
    parser = argparse.ArgumentParser()
    parser.add_argument(
                "-i",
                "--id",
                type=str,
                required=True,
                help="id profile roblox target"
                )
    parser.add_argument(
                "-g",
                "--getall",
                action="store_true",
                help="to show all data profile target"
                )
    args = parser.parse_args()

class common:
    def __init__(self,username):
        self.username = username 


class data(common):
    def __init__(self, username, link):
        super().__init__(username)
        self.link = link


class main:
    global data1
    global data2
    def __init__(self,url):
        self.url = url
        self.get = requests.get(self.url[1]).text;self.get1=requests.get(self.url[0]).text;self.get2=requests.get(self.url[2]).text
        self.jsprofile = json.loads(self.get);self.jsfriends=json.loads(self.get1);self.jsgroup=json.loads(self.get2)
        data2.append(self.jsfriends['count'])
        self.profiles()
    def profiles(self):
        self.temp = []
        print ("mengambil data dari {}".format(self.jsprofile['name']))
        print ("-"*30, f"community {self.jsprofile['name']} has join", "-"*30)
        for test2 in self.jsgroup['data']:
            self.tampung = test2['group']['name']
            data3.append(self.tampung)
        for xx in self.jsprofile:
            self.temp.append(xx)
        for x in range(0,len(data3)):
            print(data3[x])
        print ("-"*30,f"profile {self.jsprofile['name']}","-"*30)
        self.result = f"""
            [-] Description/Bio Profiles : {self.jsprofile[self.temp[0]]}
            [-] Account was created: {self.jsprofile[self.temp[1]]}
            [-] is Banned?: {self.jsprofile[self.temp[2]]}
            [-] External app display name: {self.jsprofile[self.temp[3]]}
            [-] Has verified badge: {self.jsprofile[self.temp[4]]}
            [-] Id : {self.jsprofile[self.temp[5]]}
            [-] Username: {self.jsprofile[self.temp[6]]}
            [-] Display Name : {self.jsprofile[self.temp[7]]}
            [-] Total community : {len(data3)}
            [-] Total Connection In Game : {data2[0]}
            ---------------------------------------------------------------
            """;print(self.result)
        with open(f'result{self.jsprofile['name']}.txt', mode="w", encoding="utf-8") as nulis:
            nulis.write(self.result+"\n")
            if len(data3) >= 0:
                nulis.write(f"Community has joined {self.jsprofile['name']}")
                for kesrek in data3:
                    nulis.write(kesrek+"\n")
            else:
                nulis.close()
                pass

            




if __name__=='__main__':
    usn = []
    x = data(parse().args.id,"xxxxxxxx");usn.append(x.username)
    real = [f"https://friends.roblox.com/v1/users/{x.username}/friends/count",
            f"https://users.roblox.com/v1/users/{x.username}",
            f"https://groups.roblox.com/v1/users/{x.username}/groups/roles"]

    merge = real
    
    try:

        if parse.args.getall:
            main(merge)
        else:
            pass
        
    except Exception as e:
        print (e)
