__author__ = 'SuturkinAA'

import json
from django.shortcuts import HttpResponse
import resm
from rest_framework.response import Response
from rest_framework import status

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from resources import *

def allocate(request):
    user = str(getRequest(request.path,'allocate'))
    allocate = resm.res.allocate(user)
    print('+'+user)
    if (allocate == False):
        return HttpResponse('Out of resources.', status=status.HTTP_503_SERVICE_UNAVAILABLE)
    else:
        return HttpResponse(allocate, status=status.HTTP_201_CREATED)

def deallocate(request):
    res = str(getRequest(request.path,'deallocater'))
    allocate = resm.res.deallocate(int(res))
    print('-'+res)
    if (allocate == False):
        print('Not allocated')
        return HttpResponse('', status=status.HTTP_204_NO_CONTENT)
    else:
        print('No content')
        return HttpResponse('Not allocated.', status=status.HTTP_404_NOT_FOUND)

def deallocateByName(request):
    res = str(getRequest(request.path,'deallocate'))
    allocate = resm.res.deallocateByName(res)
    print('-bn/'+res)
    if (allocate == False):
        print('Not allocated.')
        return HttpResponse('Not allocated.', status=status.HTTP_404_NOT_FOUND)
    else:
        print('No content.')
        return HttpResponse('', status=status.HTTP_204_OK)

def list(request):
    print('list')
    return HttpResponse(json.dumps(resm.res.listResource()), status=status.HTTP_200_OK)

def listByName(request):
    res = str(getRequest(request.path,'list'))
    userResources = resm.res.listByName(res)
    return HttpResponse(str(userResources), status=status.HTTP_200_OK)

def reset(request):
    resm.res.reset()
    return HttpResponse('', status=status.HTTP_204_NO_CONTENT)

def badRequest(request):
    print('bad request')
    return HttpResponse('Bad request.', status=status.HTTP_400_BAD_REQUEST)

def getRequest(path, template):
    return path[len(template)+2:]
