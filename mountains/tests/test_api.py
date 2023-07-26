import unittest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from mountains.models import *
from mountains.serializers import MountainSerializer
from mountains.tests.payloads import *


class MountainApiTestCase(APITestCase):
    def setUp(self):
        self.setup_data = Mountain.objects.create(
            title="Katu-Yaryik",
            user=User.objects.create(
                first_name="Михаил",
                second_name="Иванович",
                last_name="Анисимов",
                email="masxx2x22@yandex.ru",
                phone="+7917336353"
            ),
            coords=Coord.objects.create(
                latitude=43.18342,
                longitude=32.112525,
                height=900
            ),
            level=Level.objects.create(
                winter="1A",
                summer="1А",
                autumn="1А",
                spring="1A"
            )
        )
        self.image_1 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
            title="foto1"
        )
        self.image_2 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://altaitg.ru/upload/resize_cache/iblock/c65/800_500_1/c65f1a62717c5b9894e3e01ace6bc3f5.jpg",
            title="foto2"
        )

        self.setup_data_status_not_new = Mountain.objects.create(
            title="Passage",
            status='PEN',
            user=User.objects.create(
                first_name="Ivan",
                second_name="Ivanovich",
                last_name="Ivanov",
                email="qwerty@mail.ru",
                phone="+7222232122"
            ),
            coords=Coord.objects.create(
                latitude=42.3322,
                longitude=11.2125,
                height=1000
            ),
            level=Level.objects.create(
                winter="1А",
                summer="1А",
                autumn="1А",
                spring="1А"
            )
        )
        self.image_1 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
            title="foto1"
        )
        self.image_2 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://altaitg.ru/upload/resize_cache/iblock/c65/800_500_1/c65f1a62717c5b9894e3e01ace6bc3f5.jpg",
            title="foto2"
        )


class BaseTestCase(MountainApiTestCase):
    def setUp(self):
        self.patch_data = patch_data
        super().setUp()

    def test_get_list(self):
        url = reverse('submitdata-list')
        response = self.client.get(url)
        serializer_data = MountainSerializer([self.setup_data, self.setup_data_status_not_new], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)

    def test_get_detail(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        response = self.client.get(url)
        serializer_data = MountainSerializer(self.setup_data).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_invalid_passage(self):
        url = reverse('submitdata-detail', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_valid_title(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "title": "Kavkaz"
        }
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('Katu-Yaryik', self.setup_data.title)

    def test_get_data_by_email(self):
        response = self.client.get("/submitdata/", {"user__email": "masxx2x22@yandex.ru"})
        self.assertEqual(len(response.data), 1)

    # def test_valid_patch_passage(self):
    #     response = self.client.patch(path=reverse("submitdata-detail",
    #                                               kwargs={'pk': self.setup_data.pk}),
    #                                  data=self.patch_data,
    #                                  format='json')
    #     self.assertEqual(response.data, {'state': 1, 'message': 'The record was successfully updated'})


class CreateNewMountainTest(APITestCase):
    def setUp(self):
        self.valid_mountain_test_data = valid_mountain_test_data
        self.missing_user_test_data = missing_user_test_data
        self.missing_coords_test_data = missing_coords_test_data
        self.missing_level_test_data = missing_level_test_data
        self.missing_images_test_data = missing_images_test_data

    def test_create_mountain(self):
        url = reverse('submitdata-list')
        response = self.client.post(url, data=json.dumps(self.valid_mountain_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_user(self):
        url = reverse('submitdata-list')
        response = self.client.post(url, data=json.dumps(self.missing_user_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_coords(self):
        url = reverse('submitdata-list')
        response = self.client.post(url, data=json.dumps(self.missing_coords_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_level(self):
        url = reverse('submitdata-list')
        response = self.client.post(url, data=json.dumps(self.missing_level_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_image(self):
        url = reverse('submitdata-list')
        response = self.client.post(url, data=json.dumps(self.missing_images_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    unittest.main()
