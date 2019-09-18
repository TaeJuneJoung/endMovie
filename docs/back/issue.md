# :vertical_traffic_light:ISSUE

## 1. Key값 숨기기

​	프로젝트를 함에 있어서 숨겨야하는 값들이 많다. 무엇보다 `token`값은 숨겨야하는데, windows에서 숨기기에는 환경변수를 쓰기 부담스럽다. 기존에 그래왔듯 `json`파일이나 `txt`파일을 이용해서 값을 넣고 불러오는 형식으로 진행하였다. 그런데 Django Project에서 파일의 경로를 계속 못찾아온다는 Error가 발생했다. Django에 SECRET_KEY를 숨겨야한다는데 다들 어떻게 숨기는지 찾아보게 되었고 아래와 같은 해결방도로 해결하였다.

​	JSON파일 생성은 똑같이 하고, 경로는 `settings.py`에 있는 쪽으로 하면 된다.

```python
with open(os.path.join(SECRET_DIR, 'secret_key.json')) as f:
	data = f.read()
    
secret_key = json.loads(data)

SECRET_KEY = secret_key.get('SECRET_KEY')
```



## 2. Swagger

​	RestAPI 문서 swagger을 이용하려고 하는데 에러가 발생하였다. 기존에 사용하던 부분은 문제없이 되었는데 파이썬의 버전이 바뀌어서 이러한 일이 발생한 것인가...

```python
#settings.py
REST_FRAMEWORK = {
  'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
```

​	자동화 API문서를 만들어 주는 방법으로는 Swagger도 있지만, **drf-yasg** 라는 것도 있다.



## 3. RESTFUL POST USER

​	RESTAPI에서 `POST`를 이용하여 user를 생성하려고 하는데 password가 평문으로 들어가는 문제가 발생하였다. SHA256을 이용해서 만든 후 다시 해결해나볼까 고민하다가 복잡하게 이렇게 풀거 같진 않아 검색하여 찾아보았다. 하다가 많은 오류를 만나면서 이렇게 해야겠다하며 짠 소스가 아래와 같다. 정확히 이게 맞는지 재확인은 필요!

```python
#request.method POST 일부
serializer = UserPostSerializer(data=request.data)
if serializer.is_valid():
    user = get_user_model().objects.create_user(**serializer.data)
    return Response({'message':'생성되었습니다.'})
```





### 참고자료

[1. Key값 숨기기](https://blog.isaccchoi.com/programing/Django-secretkey-%EC%88%A8%EA%B8%B0%EA%B8%B0/)

[2-1. Swagger](https://stackoverflow.com/questions/57123611/why-swagger-raises-unclear-error-django)

[2-2. Swagger](https://www.django-rest-framework.org/community/3.10-announcement/)

[2-3. 다양한 REST API 자동 문서화](https://medium.com/towncompany-engineering/친절하게-django-rest-framework-api-문서-자동화하기-drf-yasg-c835269714fc)

[3. RESTFUL POST USER](https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework)