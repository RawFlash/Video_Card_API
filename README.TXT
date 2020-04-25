Это проект API видеокарт

Чтобы получить инфу о карте, ее можно запросить по ID или по имени
Например ID = 284:
https://video-card-api.herokuapp.com/video_card_api/return/json?id=284

id начинаются не с нуля

Например title = firepro-v8700:
https://video-card-api.herokuapp.com/video_card_api/return/json?title=firepro-v8700

Можно получить всю базу данных, имеющуюся на данный момент:
https://video-card-api.herokuapp.com/video_card_api/return/full_db

Можно выбрать ряд параметров, типа memorysize = 1024 MB и memorytype = DDR3
Например memorysize = 1024 MB и memorytype = DDR3:
https://video-card-api.herokuapp.com/video_card_api/return/json?memorysize=1024%20MB&memorytype=DDR3

Например memorysize = 1024 MB:
https://video-card-api.herokuapp.com/video_card_api/return/json?memorysize=1024%20MB

Например Gpuname = Caicos:
https://video-card-api.herokuapp.com/video_card_api/return/json?gpuname=Caicos