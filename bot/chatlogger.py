def store(message, today, printdate):
  chatlog_file = open("chatlogs.txt", "a")
  chatlog_file_read = open("chatlogs.txt", "r")
  if message != "" and message.upper() != "YOBER" and message.upper() != "TOBY":
    if (str(message)+"\n") not in chatlog_file_read.readlines():
      chatlog_file.write(message+"\n")

def getlines():
  chatlog_file = open("chatlogs.txt", "r")
  chatlog_entries = chatlog_file.readlines()
  return chatlog_entries
