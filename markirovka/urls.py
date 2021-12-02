from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from decoder import views as decoder
from registration import views as registration
from comments import views as comments
from agr import views as agr
from feedback import views as fb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration.start, name='start'),
    path('documents/', decoder.start, name='documents'),
    path('login/', registration.user_login, name='login'),
    path('logout/', registration.user_logout, name='logout'),
    path('registration/', registration.register, name='registration'),
    path('mymoney/', decoder.balance, name='balance'),
    path('load/', decoder.load_file, name='load_file'),
    path('comment/', comments.comment, name='comment'),
    path('agr/<int:file_pk>', agr.start, name='agr'),
    path('document_select/', agr.post, name='sel_doc'),
    path('help/', registration.help, name='help'),
    path('afterbuy/', registration.afterbuy, name='afterbuy'),
    path('qiwi_in/', registration.qiwi_in, name='qiwi_in'),
    path('buy/', registration.buy, name='buy'),
    path('feedback/', fb.feedback, name='feed')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
