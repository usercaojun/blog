from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

#调用日志库
import logging

# 差古剑日志记录器
logger = logging.getLogger('django')

def log(reqiest):
    # 输出日志
    logger.info('info')
    return HttpResponse('test')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',log),
]