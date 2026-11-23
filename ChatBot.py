class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, room, text):
        room.add_message(self.name, text)


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def show(self):
        print(f"{self.sender}: {self.text}")


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def add_message(self, sender, text):
        msg = Message(sender, text)
        self.messages.append(msg)
        msg.show()

    def show_history(self):
        print("\n--- Chat History ---")
        for msg in self.messages:
            msg.show()



u1 = User("Aditya")
u2 = User("Rahul")

room = ChatRoom("Python")

u1.send_message(room, "Hey!")
u2.send_message(room, "Hello Aditya!")
u1.send_message(room, "How are you?")

room.show_history()