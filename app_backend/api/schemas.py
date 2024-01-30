from ninja import ModelSchema
from api.models import Device, Location

class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')

class DeviceSchema(ModelSchema):
    # : LocationSchema | None -> attribute location can either have type of  LocationSchema or None
    # =None -> if no input provided, the default type is none
    location : LocationSchema | None = None

    class Meta:
        model = Device
        fields = ('id', 'name', 'slug', 'location')

