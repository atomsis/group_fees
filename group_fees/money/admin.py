from django.contrib import admin
from .models import Collect,Payment,Contribution,Donation

admin.site.register(Payment)
admin.site.register(Collect)
admin.site.register(Contribution)
admin.site.register(Donation)