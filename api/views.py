from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import (
    get_turf_list,
    get_turf_detail,
    create_turf,
    update_turf,
    delete_turf,
    get_login,
    create_user,
    update_user,
    delete_user,
    get_turf_image,
    get_schedules,
    get_schedule,
    update_schedule,
    create_schedule
)
# Create your views here.


@api_view(['GET', 'POST'])
def get_turfs(request):
    if request.method == "GET":
        return get_turf_list(request)
    elif request.method == "POST":
        return create_turf(request)


@api_view(['GET', 'PUT', 'DELETE'])
def get_turf(request, id):
    if request.method == "GET":
        return get_turf_detail(request, id)
    elif request.method == "PUT":
        return update_turf(request, id)
    elif request.method == "DELETE":
        return delete_turf(request, id)


@api_view(['POST'])
def view_login(request):
    if request.method == "POST":
        return get_login(request)


@api_view(['POST'])
def get_users(request):
    if request.method == 'POST':
        return create_user(request)


@api_view(['PUT', 'DELETE'])
def get_user(request, id):
    if request.method == 'PUT':
        return update_user(request, id)
    elif request.method == 'DELETE':
        return delete_user(request, id)


@api_view(['GET'])
def get_turf_images(request, turf_id):
    if request.method == "GET":
        return get_turf_image(request, turf_id)


@api_view(["GET", "POST"])
def api_schedules(request):
    if request.method == "GET":
        return get_schedules(request)
    elif request.method == "POST":
        return create_schedule(request)


@api_view(["GET", "PATCH"])
def api_schedule(request, id):
    if request.method == "GET":
        return get_schedule(request, id)
    elif request.method == "PATCH":
        return update_schedule(request, id)
