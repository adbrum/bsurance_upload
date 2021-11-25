from django.shortcuts import render
from core.forms import ImageForm
from core.models import Image
from django.contrib import messages


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            try:
                data = Image.objects.get(name=image.name)
                Image.objects.filter(pk=data.pk).delete()
                image.save()
                url = image.image_file.url
                messages.success(request, f'{image.name} image changed')
            except Image.DoesNotExist:
                image.save()
                url = image.image_file.url
                messages.success(request, f'{image.name} image uploaded')

            context = {'image_file': url,  'form': form}

            return render(request, 'core/upload_images.html', context)

        else:
            messages.error(request, 'Image upload failed')

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

    return render(request, 'core/core/404.html', context)


def handler404(request, exception):
    context = {}
    response = render(request, "core/404.html", context=context)
    response.status_code = 404
    return response
