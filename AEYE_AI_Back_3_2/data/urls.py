from django.urls import path
from .views import AI_Train_View, AI_Test_View, AI_Inference_View

urlpatterns = [
    path('ai-train', AI_Train_View.as_view(), name='ai-test'),
    path('ai-test', AI_Test_View.as_view(), name='ai-test'),
    path('ai-inference', AI_Inference_View.as_view(), name='ai-inference')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)