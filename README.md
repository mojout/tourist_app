# REST API for for the Federation of Sports Tourism of Russia - pereval.online website
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
