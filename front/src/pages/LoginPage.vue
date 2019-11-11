<template>
  <v-container class="h-90">
    <v-row class="h-100 mt-12" justify="center">
      <v-form ref="loginForm" v-model="valid" class="w-100">
        <v-col cols="12" sm="12" xs="12" class="text-center display-2 my-7">End Movie</v-col>
        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto">
          <v-text-field
            v-model="username"
            type="text"
            label="아이디"
            :rules="[rules.isNull('아이디')]"
            solo
            required
            @keyup.enter="loginValidate"
          ></v-text-field>
          <v-text-field
            v-model="password"
            type="password"
            label="비밀번호"
            :rules="[rules.isNull('비밀번호')]"
            solo
            required
            autocomplete="on"
            @keyup.enter="loginValidate"
          ></v-text-field>
        </v-col>

        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto my-auto">
          <v-btn class="w-100 title" large color="success" @click="loginValidate">로그인</v-btn>
        </v-col>
        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto my-auto">
          <v-divider class="mb-3"></v-divider>
          <v-row justify="center">
            <v-btn text tile small class="border-right-line">아이디 찾기</v-btn>
            <v-btn text tile small>비밀번호 찾기</v-btn>
            <v-btn text tile small class="border-left-line" @click="join">회원가입</v-btn>
          </v-row>
        </v-col>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
      username: "",
      password: "",
      rules: {
        isNull: str => v => (v || "").length > 0 || `${str}를 입력해주세요.`
      }
    };
  },
  methods: {
    loginValidate() {
      if (this.$refs.loginForm.validate()) {
				const loginData = {username: this.username, password: this.password}
        this.$store.dispatch('login', loginData)
        this.$router.push('/')
      }
    },
    join() {
      this.$router.push('/join')
    }
  }
};
</script>

<style scoped>
.border-right-line {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
}
.border-left-line {
  border-left: 1px solid rgba(0, 0, 0, 0.1);
}
</style>