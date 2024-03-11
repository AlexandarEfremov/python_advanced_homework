class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls,photos_count: int):
        return cls(photos_count // 4 if photos_count % 4 == 0 else (photos_count // 4) + 1)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[index].append(label)
            else:
                continue
            return f"{label} photo added successfully on page {index + 1} slot {len(self.photos[index])}"
        else:
            return "No more free slots"

    def display(self):
        result = ''
        for index, row in enumerate(self.photos):
            result += '-----------\n'
            result += ("[] " * len(self.photos[index])).rstrip()
            result += '\n'
        result += '-----------\n'
        return result[:-1]
