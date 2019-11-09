<template>
	<v-container class="h-100">
    <v-row class="h-100 title-top-margin mt-sm-10" justify="center">
      <v-form ref="loginForm" v-model="valid" class="w-100">
        <v-col cols="12" sm="12" xs="12" class="text-center display-1">End Movie</v-col>
        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto">
          <v-flex class="font-weight-bold ml-1">
						아이디
					</v-flex>
					<v-text-field
            v-model="username"
            type="text"
            label="아이디"
            :rules="[rules.isNull('아이디')]"
            solo
            required
            @keyup.enter="loginValidate"
          ></v-text-field>
          <v-flex class="font-weight-bold ml-1">
						비밀번호
					</v-flex>
          <v-text-field
            v-model="password"
            type="password"
            label="비밀번호"
            :rules="[rules.isNull('비밀번호')]"
            solo
            required
            @keyup.enter="loginValidate"
          ></v-text-field>
          <v-flex class="font-weight-bold ml-1">
						비밀번호 재확인
					</v-flex>
          <v-text-field
            v-model="passwordConfirm"
            type="password"
            label="비밀번호 재확인"
            :rules="[rules.isNull('비밀번호')]"
            solo
            required
            @keyup.enter="loginValidate"
          ></v-text-field>
          <v-flex class="ml-1">
						<span class="font-weight-bold">본인 확인 이메일</span>
						<small class="grey--text">(선택)</small>
					</v-flex>
          <v-text-field
            v-model="passwordConfirm"
            type="password"
            label="비밀번호 재확인"
            :rules="[rules.isNull('비밀번호')]"
            solo
            required
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
            <v-btn text tile small class="border-left-line">회원가입</v-btn>
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
			passwordConfirm: '',
			email: '',
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
@media (max-width: 600px) {
	.title-top-margin {
		margin-top: 50px;
	}
}
</style>