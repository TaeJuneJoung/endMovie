# Movies

## movies List

영화 리스트를 보여주면서 로그인 사용자에 따라 리스트를 보면서 바로 평점을 매길 수 있고, 자신이 매긴 평점을 볼 수 있는 시스템을 구현하려고 하다가 이슈가 발생했다.

### 발생 이슈

1. Login 사용자 정보가 바로 적용되지 않음

   > 로그인 정보가 너무 빨리 도착하여 생긴 문제로 2번 아래에 소스에 나와있듯, setTimeout()을 주어 잠시 delay로 해결함

2. Login 사용자에 대한 평점이 뒤늦게 적용하여 상황에 맞지 않음

   > 사용자의 정보를 영화 리스트Page에 넣어 user정보를 해당 페이지에서 넣었더니 생기는 문제였다. 디버깅해본 결과 **getters의 시점**에서 생기는 문제였다. 가져오는 시점이 더 빨라서 생기는 문제인데 데이터를 가져오는 부분의 시점을 더 건드릴 순 없다 판단하여, store에 넣는 부분을 더 빨리 진행하자 하여, 로그인 부분에서 store에 데이터를 저장하게 하여 문제를 해결하였다.

   ```vue
   methods: {
       loginValidate() {
         if (this.$refs.loginForm.validate()) {
   				const loginData = {username: this.username, password: this.password}
           this.$store.dispatch('login', loginData)
             .then(response => {
               // store user값을 넣어주기 위해 setTimeout 사용
               this.$store.dispatch('FetchMovies', this.username)
               setTimeout(() => {
                 this.$router.push('/')
               }, 500)
             })
         }
       }
   }
   ```

3. 이벤트(부모-자식 엘리먼트)

   > 부모 요소에 @click 이벤트를 주었더니 자식 요소에도 같이 들어가서 문제가 발생하였다. 이를 해결하기 위해 찾아본 결과 js에서는 `preventDefault`라는 부분으로 처리하는 것 같았고, vue에서는 `@click.self`로 자식 엘리먼트에게 이벤트가 들어가지 않게 하였다.