from django.contrib import admin
from firstApp.models import WeeklyObj,Week, UserInfo,Workshop,Evaluation, Chair,Reservation, Need,Module,Course,Content,Locker,Postit,Visitor, Startup,Presence, Objective
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Reservation)
admin.site.register(Need)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Locker)
admin.site.register(Postit)
admin.site.register(Visitor)
admin.site.register(Startup)
admin.site.register(Presence)
admin.site.register(Chair)
admin.site.register(Workshop)
admin.site.register(Evaluation)
admin.site.register(Week)
admin.site.register(WeeklyObj)
admin.site.register(Objective)
