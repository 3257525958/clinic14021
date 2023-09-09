from django.contrib import admin

from reserv_app.models import reservemodel,leavemodel,reservemodeltest,neurseformmodel,neurseformtestmodel

admin.site.register(reservemodel)
admin.site.register(reservemodeltest)
admin.site.register(leavemodel)
admin.site.register(neurseformmodel)
admin.site.register(neurseformtestmodel)
