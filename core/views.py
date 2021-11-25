from django.shortcuts import render
from core.forms import ImageForm
from core.models import Image


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'core/upload_images.html', {'form': form})


def show_images(request, image_name):
    try:
        images = Image.objects.get(name=image_name)
        image_file = images.image_file.url
        context = {'image_file': image_file}
        return render(request, 'core/show_images.html', context)
    except Image.DoesNotExist:
        context = {'image_file': None}

    return render(request, 'core/show_images.html', context)
