from django.contrib import admin

from app.models import Leave, LeaveApprovingFaculty, LeaveApprovingWarden,Comment

admin.site.register(Leave)
admin.site.register(LeaveApprovingFaculty)
admin.site.register(LeaveApprovingWarden)
admin.site.register(Comment)
