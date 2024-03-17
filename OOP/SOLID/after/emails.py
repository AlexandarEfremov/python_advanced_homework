from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class IContent(ABC):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass

class MyMl(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])

class HTML(IContent):
    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])

class Modifier(ABC):
    @abstractmethod
    def modify(self, data: str) -> str:
        pass

class NoModification(Modifier):
    def modify(self, data: str) -> str:
        return data

class IMModifier(Modifier):
    def modify(self, data: str) -> str:
        return "I'm " + data

class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None
        self.sender_modifier = NoModification()
        self.receiver_modifier = NoModification()

    def set_sender(self, sender):
        self.__sender = self.sender_modifier.modify(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.receiver_modifier.modify(receiver)

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)

# Usage
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = HTML('Hello, there!')
email.set_content(content)
print(email)
