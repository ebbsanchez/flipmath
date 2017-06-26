# Import some necessary libraries.
import socket

import payment

# Some basic variables used to configure the bot
server = "irc.freenode.org" # Server
channel = "#tkuic18" # Channel
botnick = "payment_bot" # Your bots nick


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def respond_payment_info():
  ordered, payed, not_payed = payment.respond()
  ircsock.send("PRIVMSG " + channel + " :ordered: %d, payed: %d\n" %(len(ordered), len(payed)))
  ircsock.send("PRIVMSG " + channel + " :not_payed:\n")
  people = ""
  i = 0
  for p in not_payed:
    people += p + "/"
    i += 1
    if i == 100 or p == not_payed[-1]:
      ircsock.send("PRIVMSG "+ channel +" :%s\n" %people)
      i = 0
      people = ""

def respond_payment_update(msg):
  msg_list = msg.split()
  i = msg_list.index("update")
  varname = msg_list[i+1]
  data = msg_list[i+2:]
  print "[*] msglist " + str(type(msg_list))
  print "[*] msglist " + str(msg_list)

  print "[*] i " + str(i)
  print "[*] msglist " + str(msg_list)
  for d in data:
    payment.adding(varname, d)



    # payment.adding(varname, d)

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()

  if ircmsg.find(":bot, payment") != -1:
    respond_payment_info()

  if ircmsg.find("payment update") != -1:
    respond_payment_update(ircmsg)
    # payment.adding()




