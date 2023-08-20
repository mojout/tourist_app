![action status](https://github.com/mojout/tourist_app/actions/workflows/django.yml/badge.svg)

# :sunrise_over_mountains: Tourist app - REST API for for the Federation of Sports Tourism of Russia - pereval.online website
The Federation for Sports Tourism in Russia maintains a database of mountain passes that receives tourist contributions. The FSTR group of experts verifies the information and saves it to the database. This is an API solution for a mobile application, which can be used by tourists to submit mountain pass data and send it to FSTR once they have internet access.

When tourists reach a mountain pass, they can take pictures and use the mobile application to submit the information. Once a tourist clicks "Send", the mobile application calls submitData method, which accepts data in JSON format.

Example JSON data:
```
 {
        "id": 3,
        "beauty_title": "Гум-Баши",
        "title": "Гум-Баши",
        "other_title": "Гум-Баши",
        "connect": "",
        "add_time": "2023-07-17T11:38:55.508651Z",
        "user": {
            "first_name": "Дмитрий",
            "second_name": "Николаевич",
            "last_name": "Герасимов",
            "email": "yassd22@mail.ru",
            "phone": "+7917343422"
        },
        "coords": {
            "latitude": 34.4434,
            "longitude": 23.43244,
            "height": 344
        },
        "level": {
            "winter": "1A",
            "summer": "",
            "autumn": "",
            "spring": ""
        },
        "images": [
            {
                "id": 2,
                "data": "https://avatars.dzeninfra.ru/get-zen_doc/103153/pub_5ded1b66ec575b00b206bf41_5ded2677e6cb9b00aee52d63/scale_1200",
                "title": "foto-1"
            },
            {
                "id": 3,
                "data": "https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
                "title": "foto-2"
            }
        ],
        "status": "NEW"
    }
]
```
# :computer: API methods
### GET /submitdata/ method
Returns a list of all mountain passes.
### POST /submitdata/ method
Allows for a single mountain pass submission.
### GET /submitdata/{id}
Retrieves data for a particular mountain pass.
### PATCH /submitdata/{id}
Allows to change a mountain pass attribute values. Returns a JSON response with:
- [X] state: '1' for successful update and '0' for unsuccessful update.
- [X] message: explains why an update has failed.
### GET /submitdata/?user__email=\<email> 
Return a list of all objects that were sent to the system by the user with the specified email address.

# ☑️ Testing

```
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
__init__.py                                         0      0   100%
manage.py                                          12      2    83%
mountains/__init__.py                               0      0   100%
mountains/admin.py                                  7      0   100%
mountains/apps.py                                   4      0   100%
mountains/migrations/0001_initial.py                6      0   100%
mountains/migrations/0002_alter_user_email.py       4      0   100%
mountains/migrations/__init__.py                    0      0   100%
mountains/models.py                                35      0   100%
mountains/serializers.py                           44      1    98%
mountains/tests/__init__.py                         0      0   100%
mountains/tests/payloads.py                         6      0   100%
mountains/tests/test_api.py                        79      7    91%
mountains/urls.py                                   8      0   100%
mountains/views.py                                 25      1    96%
mountains/yasg.py                                   6      0   100%
tourist_app_drf/__init__.py                         0      0   100%
tourist_app_drf/asgi.py                             4      4     0%
tourist_app_drf/settings.py                        26      0   100%
tourist_app_drf/urls.py                             5      0   100%
tourist_app_drf/wsgi.py                             4      4     0%
-------------------------------------------------------------------
TOTAL                                             275     19    93%
```

# Development stages:
**Sprint 1, duration 1 week :**
1. Database creation, normalization.
2. Creating a class for working with data.
3. Creating a REST API with one method - POST submitData.

**Sprint 2, duration 1 week :**

Adding new methods for REST API:
   - GET /submitdata/\<id>
   - PATCH /submitdata/\<id>
   - GET /submitData/?user__email=\<email>
     
**Sprint 3, duration 1 week :**
1. Add REST API documentation to Readme.md
2. Implemented documentation with Swagger
3. Cover code with tests

Upd 20.08.2023:
* authorization by JWT
