from django.contrib import admin

# Register your models here.
import blog.models

class PubArtikel(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if self.model._meta.model_name == 'category':
            exclude = ('penulis')
        elif not obj.penulis:
            obj.penulis = request.user
        obj.save()
    
    def get_readonly_fields(self, request, obj):
        current_user = request.user
        print(self.model._meta.fields)
        if obj != None:
            # Read only Fields untuk editor
            if current_user.has_perm('blog.terbitkan'):
                if self.model._meta.model_name == 'category':
                    readonly_fields = {
                        'slug_cat',
                    }
                    return readonly_fields
                else:
                    readonly_fields = {
                        'penulis',
                        'slug',
                    }
                    return readonly_fields
            # Read Only Fields untuk Penulis
            elif current_user.has_perm('blog.add_artikel'):
                if self.model._meta.model_name == 'category':
                    return [data.name for data in self.model._meta.fields]
                if obj.publish:
                    # semua read only
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields = {
                        'date_create',
                        'date_edit',
                        'publish',
                        'slug',
                        'penulis',
                    }
                    return readonly_fields
        
        else:
            if self.model._meta.model_name == 'category':
                readonly_fields = {
                    'slug_cat',
                }
                return readonly_fields
            else:
                readonly_fields = {
                    'date_create',
                    'date_edit',
                    'publish',
                    'slug',
                    'penulis',
                }
                return readonly_fields

for model_name in dir(blog.models):
    model = getattr(blog.models, model_name)
    if isinstance(model, type):
        admin.site.register(model, PubArtikel)