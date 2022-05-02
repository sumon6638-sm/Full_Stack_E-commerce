<template>
  <div class="SubCategory">
    <div class="grid grid-cols-3 gap-4">
      <div
        class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden"
        v-for="subCategory in subCategories"
        v-bind:key="subCategory.id"
      >
        <div class="w-1/3 bg-cover">
          <img :src="subCategory.get_image" alt="" />
        </div>
        <div class="w-2/3 p-4">
          <h1 class="text-gray-900 font-bold text-2xl">{{ subCategory.name }}</h1>
          <p class="mt-2 text-gray-600 text-sm">
            {{ subCategory.description }}
          </p>
          <div class="flex item-center justify-between mt-3">
            <h1 class="text-gray-700 font-bold text-xl">
              ${{ subCategory.price }}
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
              <router-link v-bind:to="subCategory.get_absolute_url"
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
import axios from 'axios'
import { useToast, POSITION } from "vue-toastification";

export default {
  name: 'SubCategory',
  data() {
    return {
      subCategories: {
        vehicles: []
      }
    };
  },
  mounted() {
    this.getSubCategories()
  },
  setup() {
    const toast = useToast();

    return { toast };
  },
  methods: {
    async getSubCategories() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const category_fashion = this.$route.params.category_fashion;

      await axios
        .get(`/${category_slug}/${category_fashion}`)
        .then((res) => {
          this.subCategories = res.data;

          document.title = this.subCategories.name + ' | EasyToBuy'
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    }
  }
}


</script>