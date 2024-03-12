from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category.id not in self.categories:
            self.categories.append(category.id)

    def add_topic(self, topic: Topic):
        if topic.id not in self.topics:
            self.categories.append(topic.id)

    def add_document(self, document: Document):
        if document.id not in self.documents:
            self.categories.append(document.id)

    def edit_category(self, category_id: int, new_name: str):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.edit(new_name)

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((filter(lambda d: d.id == document_id, self.documents)))
        document.edit(new_file_name)


