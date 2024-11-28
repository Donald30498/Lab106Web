from django.db import models

class Reservation(models.Model):
    date = models.DateField()  # 預約日期
    time_slot = models.CharField(max_length=20)  # 時段
    reserver_name = models.CharField(max_length=100)  # 預約者姓名
    reserver_id = models.CharField(max_length=50)  # 預約者 ID (學生或教授)
    remarks = models.TextField(blank=True, null=True)  # 備註欄位 (可選)

    class Meta:
        unique_together = ('date', 'time_slot')  # 每日期 + 時段僅允許一個預約

    def __str__(self):
        return f"{self.date} {self.time_slot} - {self.reserver_name}"
