from django.contrib import admin
from .models import *

admin.site.register(Contestant)
admin.site.register(Voter)
admin.site.register(Admin)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Vote)