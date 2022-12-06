import pdb
from django.test import TestCase
from rest_framework.test import APITestCase
from ..models import User, Image, Schedule, Turf
from ..utils import *
from django.urls import reverse