from django.contrib import admin

from jobs_app.models import jobsmodel , employeemodel
# from jobs_app.models import  servicmodel

admin.site.register(jobsmodel)
admin.site.register(employeemodel)
# admin.site.register(servicmodel)
