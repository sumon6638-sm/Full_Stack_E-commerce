<template>
  <div class="container w-full mx-auto">
    <div>
      <h2>Welcome to EasyToBuy</h2>
    </div>

    <div class="grid grid-cols-3 gap-4">
      <div
        class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden"
        v-for="vehicle in latestVehicles"
        v-bind:key="vehicle.id"
      >
        <div class="w-1/3 bg-cover">
          <img :src="vehicle.get_image" alt="" />
        </div>
        <div class="w-2/3 p-4">
          <h1 class="text-gray-900 font-bold text-2xl">{{ vehicle.name }}</h1>
          <p class="mt-2 text-gray-600 text-sm">
            {{ vehicle.description }}
          </p>
          <div class="flex item-center justify-between mt-3">
            <h1 class="text-gray-700 font-bold text-xl">
              ${{ vehicle.price }}
            </h1>
            <button
              class="
                px-3
                py-2
                bg-gray-800
                text-white text-xs
                font-bold
                uppercase
                rounded
              "
            >
              <router-link v-bind:to="vehicle.get_absolute_url"
                >View Details</router-link
              >
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      latestVehicles: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();

    document.title = 'Home | EasyToBuy'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/vehicles/latest-vehicles/")
        .then((res) => {
          this.latestVehicles = res.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped>
/* <div class="flex item-center mt-2">
  <svg
    class="w-5 h-5 fill-current text-gray-700"
    viewBox="0 0 24 24"
  >
    <path
      d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
    />
  </svg>
  <svg
    class="w-5 h-5 fill-current text-gray-700"
    viewBox="0 0 24 24"
  >
    <path
      d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
    />
  </svg>
  <svg
    class="w-5 h-5 fill-current text-gray-700"
    viewBox="0 0 24 24"
  >
    <path
      d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
    />
  </svg>
  <svg
    class="w-5 h-5 fill-current text-gray-500"
    viewBox="0 0 24 24"
  >
    <path
      d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
    />
  </svg>
  <svg
    class="w-5 h-5 fill-current text-gray-500"
    viewBox="0 0 24 24"
  >
    <path
      d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
    />
  </svg>
</div> */
</style>