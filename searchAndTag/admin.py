from django.contrib import admin
from .models import Articles
from .models import Authors
from .models import Tags
from .models import Keywords
from .models import Users
# Register your models here.
admin.site.register(Articles)
admin.site.register(Authors)
admin.site.register(Tags)
admin.site.register(Keywords)
admin.site.register(Users)