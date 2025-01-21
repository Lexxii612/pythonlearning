from enum import Enum
class CollectionType(Enum):
    BOTTLES = 1
    MOSAIC = 2
    ELVENARTIFACT = 3
    LANDMARK = 4

class DaiCollectionItem:
    name = ""
    collectionType = CollectionType(1)

    def __init__(self, name, collection_type):
        self.name = name
        self.collectionType = collection_type


class DaiCollection:
    name = ""
    collectionItems = {}

    def __init__(self, name, collection_item ):
        self.name = name
        self.collectionItems[collection_item.name] = collection_item
