<template>
  <v-container class="h-100">
    <v-row class="h-100 title-top-margin mt-sm-10" justify="center">
      <v-form ref="loginForm" v-model="valid" class="w-100">
        <v-col cols="12" sm="12" xs="12" class="text-center display-1">End Movie</v-col>
        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto">
          <v-flex class="font-weight-bold ml-1">아이디</v-flex>
          <v-row>
            <v-col cols="8">
              <v-text-field
                v-model="username"
                type="text"
                label="아이디"
                :rules="[rules.isNull('아이디')]"
                solo
                required
                @keyup.enter="checkUsername"
                @blur="checkUsername"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-btn
                large
                tile
                class="w-100"
                :color="isCheckUsername ? 'success' : 'dark'"
                @click="checkUsername"
              >{{ checkUsernameMessage }}</v-btn>
            </v-col>
          </v-row>
          <v-flex class="font-weight-bold ml-1">비밀번호</v-flex>
          <v-text-field
            v-model="password"
            type="password"
            label="비밀번호"
            :rules="[rules.password, rules.minLength(8), rules.maxLength(20)]"
            solo
            required
            autocomplete="on"
            @keyup.enter="joinValidate"
          ></v-text-field>
          <v-flex class="font-weight-bold ml-1">비밀번호 재확인</v-flex>
          <v-text-field
            v-model="passwordConfirm"
            type="password"
            label="비밀번호 재확인"
            :rules="[rules.password, rules.minLength(8), rules.maxLength(20)]"
            solo
            required
            autocomplete="on"
            @keyup.enter="joinValidate"
          ></v-text-field>
          <v-flex class="text-center mb-7" v-if="password.length >= 8 && passwordConfirm.length >= 8">
            <small class="success--text" v-if="password === passwordConfirm">비밀번호가 일치합니다.</small>
            <small class="error--text" v-else>비밀번호가 일치하지 않습니다.</small>
          </v-flex>
          <v-flex class="ml-1">
            <span class="font-weight-bold">본인 확인 이메일</span>
          </v-flex>
          <v-row>
            <v-col cols="8">
              <v-text-field
                v-model="email"
                type="email"
                label="이메일"
                :rules="[rules.email]"
                solo
                required
                @keyup.enter="emailValidate"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-btn
                large
                tile
                :loading="isLoading"
                :disabled="isLoading"
                class="w-100 success"
                @click="emailValidate"
              >인증받기</v-btn>
            </v-col>
          </v-row>
          <v-text-field v-model="authNum" :disabled="!isStop" label="인증번호" solo required>
            <template v-slot:append v-if="isStop">
              <span>
                <span class="error--text" v-if="notMeching == true">
                  불일치
                  <v-icon class="error--text">mdi-close</v-icon>
                </span>
                <span class="cursor" @click="checkAuthNums">인증</span>
              </span>
            </template>
          </v-text-field>
        </v-col>

        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto my-auto">
          <v-btn class="w-100 title" tile large color="success" @click="joinValidate">회원가입</v-btn>
        </v-col>
        <v-col cols="12" lg="5" sm="7" xs="10" class="mx-auto my-auto">
          <v-divider class="mb-3"></v-divider>
          <v-row justify="center">
            <v-btn text tile small>이용약관</v-btn>
          </v-row>
        </v-col>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
import { emailCheck, joinUser, idCheck } from "../api/user.js";

export default {
  data() {
    return {
      valid: false,
      username: "",
      password: "",
      passwordConfirm: "",
      email: "",
      isCheckUsername: false,
      checkUsernameMessage: '중복확인',
      checkedEmail: "",
      isCheckEmail: false,
      isLoading: false,
      authNum: "",
      emailCheckValue: "",
      notMeching: false,
      isStop: false,
      rules: {
        isNull: str => v => (v || "").length > 0 || `${str}를 입력해주세요.`,
        email: (v) => /.+@.+\..+/.test(v) || '유효한 E-mail을 입력해 주세요.',
        password: (v) =>
          /^(?=.*[a-z])(?=.*\d)(?=.*(_|[^\w])).+$/.test(v || '') ||
          '비밀번호는 영문, 숫자, 특수문자를 포함하여야 합니다.',
        minLength: (len) => (v) =>
          (v || '').length >= len || `해당 내용은 ${len}자를 넘어야 합니다.`,
        maxLength: (len) => (v) =>
          (v || '').length <= len || `해당 내용은 ${len}자를 넘을 수 없습니다.`
      }
    };
  },
  methods: {
    joinValidate() {
      if (this.$refs.loginForm.validate()) {
        if (this.isCheckUsername && (this.password === this.passwordConfirm)) {
          if (this.isCheckEmail) {
            const joinData = { username: this.username, password: this.password, email: this.checkedEmail }
            joinUser(joinData)
              .then(({data}) => {
                this.$router.push("/")
              })
              .catch(error => {
                console.error(error)
              })
          } else {
            alert('이메일 인증이 필요합니다.')
          }
        } else {
          alert('아이디가 중복되거나, \n 비밀번호가 일치하지 않습니다.')
        }
      }
    },
    emailValidate() {
      this.isLoading = true
      emailCheck(this.email)
        .then(({ data }) => {
          if(data.result) {
            this.checkedEmail = this.email
            this.emailCheckValue = data.result
            this.isLoading = false
            this.isStop = true
          } else {
            this.isLoading = false
            alert('지원하지 않는 이메일입니다.')
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    checkAuthNums() {
      if(this.authNum == this.emailCheckValue) {
        this.isStop = false
        this.isCheckEmail = true
        alert('인증이 완료되었습니다.')
      } else {
        this.notMeching = true
      }
    },
    checkUsername() {
      if(this.username) {
        const username = { username: this.username }
        idCheck(username)
          .then(({data}) => {
            this.isCheckUsername = !(data.result)
            if(data.result) {
              this.checkUsernameMessage = '사용불가'
            } else {
              this.checkUsernameMessage = '사용가능'
            }
          })
      } else {
        this.checkUsernameMessage = '중복확인'
        this.isCheckUsername = false
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
.col {
  padding: 0;
  padding-left: 12px;
  padding-right: 12px;
}
.cursor {
  cursor: pointer;
}
</style>