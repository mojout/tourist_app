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
### GET /submitdata/?user__email=<email> 
Return a list of all objects that were sent to the system by the user with the specified email address.

### Development stages:
**Sprint 1, duration 1 week :**
1. Database creation, normalization.
2. Creating a class for working with data.
3. Creating a REST API with one method - POST submitData.

**Sprint 2, duration 1 week :**
1. Adding new methods for REST API:
   - GET /submitdata/<id>
   - PATCH /submitdata/<id>
   - GET /submitData/?user__email=<email>
2. Server Deployment.
