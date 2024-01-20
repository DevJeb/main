try:
    import urllib.request
    import json
    import time
    import random
except BaseException:
    pass
class Hash():
    def __init__(self):
        response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/info.txt")
        hash_type = int(response.read().decode('utf-8').split("\n")[1])
        print("██████╗░███████╗██╗░░░██╗░░░░░██╗███████╗██████╗░\n██╔══██╗██╔════╝██║░░░██║░░░░░██║██╔════╝██╔══██╗\n██║░░██║█████╗░░╚██╗░██╔╝░░░░░██║█████╗░░██████╦╝\n██║░░██║██╔══╝░░░╚████╔╝░██╗░░██║██╔══╝░░██╔══██╗\n██████╔╝███████╗░░╚██╔╝░░╚█████╔╝███████╗██████╦╝\n╚═════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚══════╝╚═════╝░")
        print("Разработанно DevJeb, используется "+str(hash_type)+"-ая система")
        response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/Hashing_dictionary.json")
        hashing = json.loads(response.read().decode('utf-8'))
        result=""
        back = time.time()
        a=str(input('Введите текст: '))
        b=list(a)
        for s in b:
            result+=hashing[s]
        print('Хэшированные данные:\n\n\n' + result+"\n\n\n")
        print('Результат был выполнен за ' + str(time.time()-back))
    def hash_64(*args):
        i=0
        rs=[]
        for content in args:
            result=""
            content=str(content)
            response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/Hashing_dictionary.json")
            hashing = json.loads(response.read().decode('utf-8'))
            b=list(content)
            for s in b:
                result+=hashing[s]
            rs.append(result)
        return result
    def custom(type, *args):
        rs=[]
        s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        g = {}
        for d in f:
            token = ""
            k=0
            q = True
            while q:
                for i in range(type):
                    token += s[random.randint(0,89)]
                if g:
                    for a, l in g.items():
                        if token==l:
                            k+=1
                        else:
                            k+=0
                    if k==0:
                        q=False
                else:
                    q= False
            g[d] = token
        hashing = g
        i=0
        for content in args:
            content=str(content)
            type=int(type)
            b=list(content)
            result=""
            for s in b:
                result+=hashing[s]
            rs.append(result)
            i+=1
        rs.append(hashing)
        return rs
    def custom_not_a_dictionary(type, *args):
        type=int(type)
        rs=[]
        s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        g = {}
        for d in f:
            token = ""
            k=0
            q = True
            while q:
                for i in range(type):
                    token += s[random.randint(0,89)]
                if g:
                    for a, l in g.items():
                        if token==l:
                            k+=1
                        else:
                            k+=0
                    if k==0:
                        q=False
                else:
                    q= False
            g[d] = token
        hashing = g
        i=0
        for content in args:
            content=str(content)
            type=int(type)
            result=""
            b=list(content)
            for s in b:
                result+=hashing[s]
            rs.append(result)
            i+=1
        return rs
    def anti_hash_custom(dictionary, *args):
        z=0
        rs=[]
        for content in args:
            content=str(content)
            for c,a in dictionary.items():
                hash_type=len(a)
                break
            b=[content[i:i+hash_type] for i in range(0, len(content), hash_type)]
            result=""
            for s in b:
                for v,h in dictionary.items():
                    if h==s:
                        break
                result+=v
            rs.append(result)
            z+=1
        return rs
    def anti_hash(*args):
        j=0
        rs=[]
        for content in args:
            content=str(content)
            dictionary =json.loads(urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/Hashing_dictionary.json").read().decode('utf-8'))
            for c,a in dictionary.items():
                hash_type=len(a)
                break
            b=[content[i:i+hash_type] for i in range(0, len(content), hash_type)]
            result=""
            for s in b:
                for v,h in dictionary.items():
                    if h==s:
                        break
                result+=v
            rs.append(result)
            j+=1
        return rs
