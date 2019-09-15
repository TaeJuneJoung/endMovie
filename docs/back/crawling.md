# Crawling

## Movie

`https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=ko-KR&sort_by=popularity.desc&page=1`

​	page는 1부터 500까지 제공되며, 총 1만개의 영화 데이터를 받을 수 있다. 1 page에 20개의 영화이니, 적절선의 영화의 갯수는 몇 개로 선정할 것인가.

1. 초기 설정 100개**[page1~5까지]**
2. 완성된 후 1,000개~3,000개
3. 관리한다면, **AWS lambda**를 이용하여 지속적 업그레이드

