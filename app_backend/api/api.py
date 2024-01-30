from ninja import NinjaAPI
from api.models import Device
from api.schemas import DeviceSchema

from api.models import Location
from api.schemas import LocationSchema

app = NinjaAPI()

@app.get("devices/", response = list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

@app.get("locations/", response = list[LocationSchema])
def get_locations(request):
    return Location.objects.all()