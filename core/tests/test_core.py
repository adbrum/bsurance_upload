from django.test import TestCase
from core.forms import ImageForm
from core.models import Image
from django.urls import reverse


class ImageUploadViewTest(TestCase):
    def setUp(self):
        pass

    def test_upload_image_view(self):
        """
        Test that the upload image view works
        """
        response = self.client.get(reverse('upload_image'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/upload_images.html')
        self.assertContains(response, 'Upload Image')
        self.assertIsInstance(response.context['form'], ImageForm)

    def test_upload_image_view_post(self):
        """
        Test that the upload image view works with a post request
        """
        response = self.client.post(reverse('upload_image'), {
            'name': 'test_image',
            'image_file': open('core/tests/test_image.svg', 'rb')
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/upload_images.html')
        self.assertContains(response, 'Upload Image')
        self.assertIsInstance(response.context['form'], ImageForm)
        self.assertEqual(len(Image.objects.all()), 1)

    def test_upload_image_view_post_error(self):
        """
        Test that the upload image view works with a post request
        """
        response = self.client.post(reverse('upload_image'), {
            'name': 'test_image',
            'image_file': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/upload_images.html')
        self.assertContains(response, 'Upload Image')
        self.assertIsInstance(response.context['form'], ImageForm)
        self.assertEqual(len(Image.objects.all()), 0)

    def test_upload_image_view_post_error_2(self):
        """
        Test that the upload image view works with a post request
        """
        response = self.client.post(reverse('upload_image'), {
            'name': '',
            'image_file': open('core/tests/test_image.svg', 'rb')
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/upload_images.html')
        self.assertContains(response, 'Upload Image')
        self.assertIsInstance(response.context['form'], ImageForm)
        self.assertEqual(len(Image.objects.all()), 0)
