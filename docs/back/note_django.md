# Django

Django를 공부하다가 정리하는 내용



## DateTimeField

- **auto_now**

  > `django model`이 save될 때마다 현재날짜(`date.today()`)로 갱신

- **auto_now_add**

  > **최초 저장시에만** 현재 날짜를 적용
  >
  > :warning:객체를 생성 후 추가하게되면 None값이 들어간다.

  

