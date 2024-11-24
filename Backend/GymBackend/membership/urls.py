from django.urls import path
from .views import MemberList,MemberDetail,MembershipTypeList,MembershipTypeDetail,AttendanceDetail,AttendanceList

urlpatterns = [
    path('members/', MemberList.as_view(), name='member_list'),
    path('members/<str:pk>/', MemberDetail.as_view(), name='member_detail'),
    path('membership-types/', MembershipTypeList.as_view(), name='membership_type_list'),
    path('membership-types/<str:pk>/', MembershipTypeDetail.as_view(), name='membership_type_detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance_list'),
    path('attendance/<str:pk>/', AttendanceDetail.as_view(), name='attendance_detail'),
]
