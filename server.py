#!usr/bin/python
import threading
from socket import *
import sys
import socket
import time
import string
import os.path
from os import path
from datetime import datetime
import logging
#LOGGING CONFIGURATION
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s %(levelname)-8s %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename='server.log',
                   filemode='w')


   
#GET METHOD
def handleget(client,req,url,statuscode,codestring):
	if ".html" in url:
		content_type = "text/html"
	if ".png" in url:
		content_type = "image/png"
	if ".jpg" in url:
		content_type = "image/jpeg"
	if url == "/":
		content_type = "text/html"
	if url == "/" :
		f = open("Blog/index.html")
		text= f.read()
		length = len(text)
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Content-Length:"+str(length)+"\n"
		string+="Content-Type: "+ content_type+" ;charset=iso-8850-i\r\n"
		string+="Connection:close\r\n"
		output=string+text
		client.send(output.encode())
		client.close()
		return
	file_path= "Blog"+url
	#print(file_path)
	if path.exists(file_path):
		if content_type == "image/jpeg":
			f = open(file_path,'rb')
			imagedata= f.read()
			length = len(imagedata)
			string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
			string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
			string+="Server:Ayusha/1.1 (Linux)\r\n"
			string+="Content-Length:"+str(length)+"\r\n"
			string+="Content-Type: "+ content_type+" ;charset=iso-8850-i\r\n"
			string+="Connection:close\r\n\r\n"
			
			client.send(string.encode())
			client.send(imagedata)	
			client.close()
		elif content_type == "text/html":
			f = open(file_path)
			text= f.read()
			length = len(text)
			string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
			string+="DATE: "+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
			string+="Server: Ayusha/1.1 (Linux)\r\n"
			string+="Content-Length: "+str(length)+"\r\n"
			string+="Content-Type: "+ content_type+";charset=iso-8850-i\r\n"
			string+="Connection :close\r\n\r\n"
			output=string+text
			client.send(output.encode())
			client.close()
	else: 
		statuscode=404
		codestring= "FILE NOT FOUND"
		#print("404")
		err = open("error.log","a")
		err.write(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+" ERR "+str(statuscode)+ " " + codestring+"\n")
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring +"\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Connection:close\r\n"
		f = open("error.html")
		text= f.read()
		output=string+text
		client.send(output.encode())
		client.close()
		
	
	
#HEAD METHOD
def handlehead(client,req,url,statuscode,codestring):
	if ".html" in url:
		content_type = "text/html"
	if ".png" in url:
		content_type = "image/png"
	if ".jpg" in url:
		content_type = "image/jpeg"
	if url == "/":
		content_type = "text/html"
	if url == "/" :
		f = open("Blog/index.html")
		text= f.read()
		length = len(text)
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Content-Length:"+str(length)+"\n"
		string+="Content-Type: "+ content_type+" ;charset=iso-8850-i\r\n"
		string+="Connection:close\r\n"
		output=string
		client.send(output.encode())
		client.close()
		return 
	file_path = "Blog"+url
	if path.exists(file_path):		
		f = open(file_path)
		text=f.read()
		length = len(text)
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Content-Length:"+str(length)+"\n"
		string+="Content-Type: "+ content_type+" ;charset=iso-8850-i\r\n"
		string+="Connection:close\r\n\r\n"
		output=string
		client.send(output.encode())	
		client.close()
	else:
		statuscode = 404
		codestring="NOT FOUND"
		err = open("error.log","a")
		err.write(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+" ERR "+str(statuscode)+ " " + codestring+"\n")
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Content-Length:"+str(length)+"\n"
		string+="Content-Type: "+ content_type+" ;charset=iso-8850-i\r\n"
		string+="Connection:close\r\n\r\n"
		client.send(string.encode())	
		client.close()
		
		
#POST METHOD	
def handlepost(client,data,url,statuscode,codestring):
	#print(data)
	#print("in post")
	f = open("post_data.txt","a")
	strings = data.partition("\r\n\r\n")
	#print(strings)
	post_data = strings[2]
	values = post_data.split("&")
	first = values[0].split("=")
	fname=first[1]
	last = values[1].split("=")
	lname= last[1]
	if fname == '' and lname == '':
		statuscode = 204
		codestring="NO CONTENT"
		err = open("error.log","a")
		err.write(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+" ERR "+str(statuscode)+ " " + codestring+"\n")
	else:
		statuscode = 200
		codestring="OK"
	f.write(fname +"," + lname+"\n")
	f.close()
	string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
	string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
	string+="Server:Ayusha/1.1 (Linux)\n"
	string+="Connection:close\r\n\r\n"
	output=string
	client.send(output.encode())	
	client.close()
	
	
#DELETE METHOD	
def handledelete(client,data,url,statuscode,codestring):
	file_path = "Blog"+url
	if path.exists(file_path):
		os.remove(file_path)
		statuscode = 200
		codestring="OK"
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Connection:close\r\n\r\n"
		client.send(string.encode())	
		client.close()
		
		
#PUT METHOD	
def handleput(client,data,url,statuscode,codestring):
	#rint(data)
	statuscode=200
	codestring="OK"
	if ".html" in url:
		content_type = "text/html"
	if ".png" in url:
		content_type = "image/png"
	if ".jpg" in url:
		content_type = "image/jpeg"
	if content_type == "text/html":
		
		file_path="Blog"+url
		#print(file_path)
		f = open(file_path,"w")
		strings = data.partition("\r\n\r\n")
		file_data = strings[2]
		f.write(file_data)
		f.close()
		string="HTTP/1.1 "+ str(statuscode) + " " + codestring + "\r\n"
		string+="DATE:"+ time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())+"\r\n"
		string+="Server:Ayusha/1.1 (Linux)\n"
		string+="Connection:close\r\n\r\n"
		client.send(string.encode())	
		client.close()
	
#log function for maintaining logs	
def log(req,hostname,useragent):
	msg = req+ " " + "HostName: "+hostname + " 		UserAgent: " + useragent
	#print(msg)
	logging.info(msg)	




#parsing headers
def parseheaders(client,data):
	statuscode=200
	codestring= "OK"
	
	if "HOST:" not in data:
		statuscode= 400
		codestring = "BAD REQUEST"
	req = data.split('\n')	
	first_line=req[0].split(' ')
	req_type=first_line[0]
	req_file= first_line[1]
	version = first_line[2]
	data_headers = data.partition("\r\n\r\n")
	headers = data_headers[0]
	
	line = headers.split("\r\n")
	
	num = len(line)
	i=0
	while i<num:
		string = line[i];
		if string.find("Host:") == 0:
			host_index = string.find(" ")
			host_index2=string.find("\r\n")
			hostname=string[host_index+1:host_index2]
			#print(hostname)
		elif string.find("User-Agent:") == 0:
			user_index = string.find(" ")
			user_index2=string.find("\r\n")
			useragentname=string[user_index+1:user_index2]
			#print(useragentname)
		i=i+1
	log(req[0],hostname,useragentname)
	if version != "HTTP/1.1":
		statuscode = 505
		codestring = "HTTP Version Not Supported"
		log_error(505,"HTTP Version Not Supported")
	if req_type == "GET":
		handleget(client,req,req_file,statuscode,codestring)
	if req_type == "HEAD":
		handlehead(client,req,req_file,statuscode,codestring)
	if req_type == "POST":
		handlepost(client,data,req_file,statuscode,codestring)
	if req_type == "DELETE":
		handledelete(client,data,req_file,statuscode,codestring)
	if req_type == "PUT":
		handleput(client,data,req_file,statuscode,codestring)






#class for multithreading
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print("server started.....")
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size).decode()
                if data:
                    parseheaders(client,data)
                    #print(data)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False
            

if __name__ == "__main__":
		while True:
			serverPort = int(sys.argv[1])
			ThreadedServer('',serverPort).listen()
