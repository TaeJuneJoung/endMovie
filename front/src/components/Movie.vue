<template>
  <v-hover v-slot:default="{ hover }">
    <v-card class="mx-auto grey darken-4" :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" max-width="600">
      <v-img :src="movie.poster" max-height="300px">
        <v-expand-transition>
          <v-flex
            v-if="hover"
            class="transition-fast-in-fast-out transition-card v-card--reveal white--text"
          >
            ★★★★★
          </v-flex>
        </v-expand-transition>
      </v-img>

      <v-container>
        <v-flex class="title-shortly white--text">{{ movie.title }}</v-flex>
        <v-flex class="grey--text caption">Date:</v-flex>
        <v-flex class="grey--text caption">Action:</v-flex>
        <v-flex class="grey--text caption">Member:</v-flex>
      </v-container>
    </v-card>
  </v-hover>
</template>


<script>
export default {
	props: {
    movie: {}
  },
}
</script>

<style scoped>
.title-shortly {
	font-weight: bold;
	text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.transition-card {
	background-color: rgba(0, 0, 0, 0.4);
	height: 100%;
}
</style>>
