from site import ENABLE_USER_SITE
from django.contrib import admin
# accessing the model file and the classes
from .models import Topic, Entry
# Register your models here.
admin.site.register(Topic)
admin.sire.register(Entry)