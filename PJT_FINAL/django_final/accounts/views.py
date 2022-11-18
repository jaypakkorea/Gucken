from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

#for profile
import base64
import os
from datetime import datetime


User = get_user_model()

@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)



# @api_view(['POST'])
# def upload_image(request):
#     img_string = request.data['img_base64'] # POST요청을 통해 받은 base64정보
#     imgdata = base64.b64decode(img_string) # 디코딩
#     now = datetime.now()
#     now = datetime.timestamp(now)
#     filename = f'temp_image_{request.user}.jpg' # DB에 저장하지 않고 사용한다음 지우기 위해
#     with open(filename, 'wb') as f:
#         f.write(imgdata)				# 디코딩한 이미지를 사용하기 위해 잠시 저장
#  	#### 이미지를 사용하는 코드 #####
#     os.remove(filename)    				# 이미지를 사용한 후 삭제
#     return Response({'result' : imgdata})
