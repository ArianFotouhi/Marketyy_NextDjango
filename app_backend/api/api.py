from ninja_extra import (NinjaExtraAPI, 
                         api_controller, 
                         route, 
                         )

from api.models import Device, Location
from api.schemas import (
    DeviceSchema,
    LocationSchema,
    DeviceCreateSchema,
    Error,
    DeviceLocationPatch,
    LoginSchema,
    TokenSchema
)
from .utils.token_util import generate_jwt_token
from django.shortcuts import get_object_or_404

from ninja.security import HttpBearer
from django.contrib.auth import authenticate


        
app = NinjaExtraAPI()

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token
        

# @api_controller("/devices", tags=["Devices"], auth=AuthBearer())
@api_controller("/devices", tags=["Devices"])
class DeviceController:

    @route.get("/", response=list[DeviceSchema])
    def get_devices(self):
        return Device.objects.all()

    @route.post("/", response={200: DeviceSchema, 404: Error})
    def create_device(self, device: DeviceCreateSchema):
        if device.location_id:
            # we have a location ID
            location_exists = Location.objects.filter(id=device.location_id).exists()
            if not location_exists:
                return 404, {"message": "Location not found"}

        device_data = device.model_dump()
        device_model = Device.objects.create(**device_data)
        return device_model

    @route.get("/{slug}/", response=DeviceSchema)
    def get_device(self, slug: str):
        device = get_object_or_404(Device, slug=slug)
        return device

    @route.post("/{device_slug}/set-location/", response=DeviceSchema)
    def update_device_location(self, device_slug, location: DeviceLocationPatch):
        device = get_object_or_404(Device, slug=device_slug)
        if location.location_id:
            location = get_object_or_404(Location, id=location.location_id)
            device.location = location
        else:
            device.location = None

        device.save()
        return device


@api_controller("/locations", tags=["Locations"], permissions=[])
class LocationController:
    @route.get("/", response=list[LocationSchema])
    def get_locations(self):
        return Location.objects.all()



@api_controller("/auth", tags=["Login"])
class AuthController:

    @route.post("/login/", response={200: TokenSchema, 401: Error})
    def login(self, request, device: LoginSchema):
        username = device.username
        password = device.password
        user = authenticate(request, username=username, password=password)

        if user:
            # Generate JWT token using a secure function
            token = generate_jwt_token(user)
   
            return 200, {"token": token, 'user':str(user)}
        else:
            return 401, {"message": "Invalid username or password"}





app.register_controllers(DeviceController, LocationController, AuthController)
