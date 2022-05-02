<template>
  <div id="wrapper">
    <Header />

    <router-view class="h-[80vh]" />

    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
export default {
  name: "",
  components: {
    Header,
    Footer,
  },
};
</script>

<style lang="scss">
</style>
