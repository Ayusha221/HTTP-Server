import socket
import sys
import os
SERVER = "127.0.0.1"
PORT = int(sys.argv[1])
#get method testing1
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("--------------------Sending get request1(html content)--------------------------")
headers = "GET / HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
headers += "Accept-Language: en-us,en;q=0.5\r\n"
headers +="Accept-Encoding: gzip,deflate\r\n"
headers += "Connection: close\r\n\r\n"
string=headers
client.send(string.encode())
in_data =  client.recv(1024)
print(in_data.decode())
client.close()

#get method testing2 
print("-----------------------------------------------------------------------------------------------------------------------------")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("----------------Sending get request2(there is no such file)-----------------------------------")
headers = "GET /computer.html HTTP/1.1 \r\n"
headers += "Host: Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
headers += "Accept-Language: en-us,en;q=0.5\r\n"
headers +="Accept-Encoding: gzip,deflate\r\n"
headers += "Connection: close\r\n\r\n"
string=headers
client.send(string.encode())
data =  client.recv(1024).decode()
print(data)
client.close()




#Head method testing
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("-----------------------------------------------------------------------------------------------------------------------------")
print("--------------------Sending HEAD request--------------------------")
headers = "HEAD /blog.html HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
headers += "Accept-Language: en-us,en;q=0.5\r\n"
headers +="Accept-Encoding: gzip,deflate\r\n"
headers += "Connection: close\r\n\r\n"
string=headers
client.send(string.encode())
in_data =  client.recv(1024)
print(in_data.decode())
client.close()


print("-----------------------------------------------------------------------------------------------------------------------------")
#post method testing
print("--------------------------------------------------------------------------------------------------------------------------------")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("--------------------Sending POST request(form data)--------------------------")
headers = "POST /post.html HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Connection: close\r\n\r\n"
headers +="fname=Ahana&lname=Sharma\n"
string=headers
client.send(string.encode())
in_data =  client.recv(1024)
print(in_data.decode())
print("Reading and printing post_data.txt")
f = open("post_data.txt")
text=f.read()
print(text)
client.close()



#put method testing
#basically here we will put sample.html in Blog (DOCUMENTROOT)
print("--------------------------------------------------------------------------------------------------------------------------------")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("--------------------Sending PUT request--------------------------")
print("putting sample.html in DocumentRoot")
headers = "PUT /sample.html HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Connection: close\r\n\r\n"
fi = open("sample.html")
data=fi.read()
string=headers+data
client.send(string.encode())
in_data =  client.recv(1024)
print(in_data.decode())
print("Reading sample.html from Documentroot")
fl=open("Blog/sample.html")
text=fl.read()
print(text)
client.close()



#basically here we will put (overwrite) sample.html in Blog (DOCUMENTROOT)
print("--------------------------------------------------------------------------------------------------------------------------------")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("--------------------Sending PUT request(overwrite)--------------------------")
print("----------Initial Content of  overwrite.html------------")
t=open("Blog/overwrite.html")
r=t.read()
print(r)
headers = "PUT /overwrite.html HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Connection: close\r\n\r\n"
fi = open("overwrite.html")
data=fi.read()
string=headers+data
client.send(string.encode())
in_data =  client.recv(1024)
print(in_data.decode())
print("-----------overwriting overwrite.html in DocumentRoot--------")
print("-----------Reading overwrite.html from Documentroot----------")
fl=open("Blog/overwrite.html")
text=fl.read()
print(text)




#DELETE METHOD TESTING
print("-----------------------------------------------------------------------------------------------------------------")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("--------------------Sending DELETE request--------------------------")
print("--------------------Before  DELETE request--------------------")
files = os.listdir("Blog")
print(files)
print("\n")
headers = "DELETE /nature.jpg HTTP/1.1 \r\n"
headers += "Host:Ayusha_client.py\r\n"
headers += "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r\n"
headers += "Connection: close\r\n\r\n"
string=headers
client.send(string.encode())
in_data =  client.recv(1024)

print(in_data.decode())
client.close()
print("--------------------After DELETE request--------------------")
files_new = os.listdir("Blog")
print(files_new)
