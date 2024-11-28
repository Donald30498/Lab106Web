from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    # 定義在後台列表中顯示的字段
    list_display = ('date', 'time_slot', 'reserver_name', 'reserver_id')
    
    # 添加篩選功能
    list_filter = ('date', 'time_slot')
    
    # 添加搜索功能
    search_fields = ('reserver_name', 'reserver_id')
    
    # 設置可編輯的字段（直接在列表頁面中修改）
    list_editable = ('time_slot', 'reserver_name')
