valid_mountain_test_data = {
        "beauty_title": "Кату-Ярык4",
        "title": "Кату-Ярык",
        "other_title": "Кату-Ярык2",
        "connect": "",
        "add_time": "2023-07-17T11:34:10.846790Z",
        "user": {
            "first_name": "Михаил",
            "second_name": "Иванович",
            "last_name": "Анисимов",
            "email": "masxx2x22@yandex.ru",
            "phone": "+7917336353"
        },
        "coords": {
            "latitude": 33.4423,
            "longitude": 43.4324,
            "height": 5435
        },
        "level": {
            "winter": "1A",
            "summer": "",
            "autumn": "",
            "spring": ""
        },
        "images": [
            {
                "id": 1,
                "data": "https://altaitg.ru/upload/resize_cache/iblock/c65/800_500_1/c65f1a62717c5b9894e3e01ace6bc3f5.jpg",
                "title": "foto-1"
            }
        ],
        "status": "NEW"
    }

missing_user_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_coords_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_level_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_images_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              }
            }


patch_data = {
        "beauty_title": "Кату-Ярык33",
        "title": "Кату-Ярык",
        "other_title": "Кату-Ярык2",
        "connect": "",
        "add_time": "2023-07-17T11:34:10.846790Z",
        "user": {
            "first_name": "Михаил",
            "second_name": "Иванович",
            "last_name": "Анисимов",
            "email": "masxx2x22@yandex.ru",
            "phone": "+7917336353"
        },
        "coords": {
            "latitude": 33.4423,
            "longitude": 43.4324,
            "height": 5435
        },
        "level": {
            "winter": "1A",
            "summer": "",
            "autumn": "",
            "spring": ""
        },
        "images": [
            {
                "id": 1,
                "data": "https://altaitg.ru/upload/resize_cache/iblock/c65/800_500_1/c65f1a62717c5b9894e3e01ace6bc3f5.jpg",
                "title": "foto-1"
            }
        ],
        "status": "NEW"
    }
