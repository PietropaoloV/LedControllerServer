from Entity import Message
from Entity import Key
def deserialize(byteMessage):
    stringMessage = byteMessage[0].decode("utf-8")
    messageArgs = stringMessage.split(",")
    return Message(Key(messageArgs[3],messageArgs[4].lower() == "true" ), messageArgs[2], messageArgs[1], messageArgs[0])