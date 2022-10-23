from mongoengine import Document, fields, connect, disconnect, EmbeddedDocument
disconnect('default')
connect('NavicMap')
# Create your models here.
class Node(EmbeddedDocument):
    latitude = fields.FloatField()
    longitude = fields.FloatField()


class List(EmbeddedDocument):
    parent_node = fields.EmbeddedDocumentField(
        document_type=Node
    )
    children = fields.EmbeddedDocumentListField(
        document_type=Node
        )



class Area(Document):
    name = fields.StringField(max_length=50)
    coordinates = fields.EmbeddedDocumentListField(
        document_type=Node
        )
    endpoints_to_main_road = fields.EmbeddedDocumentListField(
        document_type=Node
    )
    graph = fields.EmbeddedDocumentListField(
        document_type=List
        )


class City(Document):
    name = fields.StringField(max_length=25)
    areas = fields.ListField(
        field=fields.ObjectIdField() #Area
    )
    coordinates = fields.EmbeddedDocumentListField(
        document_type=Node
        )
    endpoints_to_highway = fields.EmbeddedDocumentListField(
        document_type=Node
    )
    graph = fields.EmbeddedDocumentListField(
        document_type=List
        )



class State(Document):
    name = fields.StringField(max_length=25)
    cities = fields.ListField(
        field=fields.ObjectIdField() #City
    )
    coordinates = fields.EmbeddedDocumentListField(
        document_type=Node
        )
    graph = fields.EmbeddedDocumentListField(
        document_type=List
        )


class Country(Document):
    name = fields.StringField(max_length=25)
    states = fields.ListField(
        field=fields.ObjectIdField() #State
    )
    coordinates = fields.EmbeddedDocumentListField(
        document_type=Node
        )
    graph = fields.EmbeddedDocumentListField(
        document_type=List
        )








