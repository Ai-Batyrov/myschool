from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/<int:user_id>/profile', ShowProfile.as_view(), name='user-profile'),
    # path('dashboard/<int:user_id>/grades', ShowProfile.as_view(), name='grades'),
    # path('dashboard/<int:user_id>/system_calendar', ShowProfile.as_view(), name='system-calendar'),
    # path('dashboard/<int:user_id>/schedule', ShowProfile.as_view(), name='schedule'),
    # path('dashboard/<int:user_id>/myteachers', ShowProfile.as_view(), name='student-my-teachers'),
    # path('dashboard/<int:user_id>/messages', ShowProfile.as_view(), name='messages'),
    # path('dashboard/<int:user_id>/chat', ShowProfile.as_view(), name='student-classmates-chat),
    path('', LoginUser.as_view(), name='login'),
]
