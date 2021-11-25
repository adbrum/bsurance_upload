import os
from django.db import models


def rename_path_image(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        class_model = (instance,)
        filename = f"{str(class_model[0]).split(': ')[0]}.{ext}"
        return os.path.join(path, filename)
    return wrapper


class Image(models.Model):
    name = models.CharField(max_length=500)
    image_file = models.FileField(
        upload_to=rename_path_image('static/img/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
