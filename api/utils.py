import jwt
from rest_framework.response import Response
from .models import User, Turf, Image, Schedule
from .serializers import UserSerializer, TurfSerializer, ImageSerializer, ScheduleSerializer
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timedelta


def get_turf_list(request):
    turfs = Turf.objects.all()
    serializer = TurfSerializer(turfs, many=True)
    return Response(serializer.data)


def get_turf_detail(request, id):
    turf = Turf.objects.get(id=id)
    serializer = TurfSerializer(turf, many=False)
    return Response(serializer.data)


def create_turf(request):
    data = request.data.copy()
    serializer = TurfSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_turf(request, id):
    data = request.data
    turf = Turf.objects.get(id=id)
    serializer = TurfSerializer(instance=turf, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_turf(request, id):
    turf = Turf.objects.get(id=id)
    turf.delete()
    return Response("Turf was deleted !")


def get_login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username=username).first()

    if user is None:
        raise AuthenticationFailed('User not found')
    if user.password != password:
        raise AuthenticationFailed('Incorrect password')

    payload = {
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt', value=token)
    response.data = {
        'jwt': token,
        'detail': 'Login successfully',
        'user_id': user.id
    }

    return response


def create_user(request):
    data = request.data.copy()
    serializer = UserSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_user(request, id):
    data = request.data
    user = User.objects.get(id=id)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return Response("User was deleted !")


def get_turf_image(request, turf_id):
    images = Image.objects.filter(turf=turf_id)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

def create_turf_image(request, turf_id):
    data = request.data.copy()
    data['turf'] = turf_id
    serializer = ImageSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_schedules(request):
    schedules = Schedule.objects.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


def get_schedule(request, id):
    schedules = Schedule.objects.get(id=id)
    serializer = ScheduleSerializer(schedules, many=False)
    return Response(serializer.data)


def update_schedule(request, id):
    data = request.data
    schedule = Schedule.objects.get(id=id)
    serializer = ScheduleSerializer(instance=schedule, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_schedule(request):
    data = request.data.copy()
    # TODO: calculate total money
    schedule = Schedule.objects.filter(
        start_time__gte=data['start_time'], start_time__lt=data['end_time'])
    if schedule:
        return Response({'detail': 'The turf was scheduled'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ScheduleSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
