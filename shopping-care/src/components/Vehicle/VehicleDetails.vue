<template>
  <div>
    <div class="grid grid-cols-3 grid-4">
      <div class="col-span-2">
        <div
          class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden"
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
                @click="addToCart"
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
                Add to Card
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="flex">
        <span
          @click="minus()"
          class="
            focus:outline-none
            dark:text-white
            focus:ring-2 focus:ring-offset-2 focus:ring-gray-800
            cursor-pointer
            border border-gray-300 border-r-0
            w-7
            h-7
            flex
            items-center
            justify-center
            pb-1
          "
          >-</span
        >
        <input
          id="quantity"
          v-model="quantity"
          aria-label="input"
          class="
            border
            dark:text-white
            border-gray-300
            dark:bg-transparent
            text-center
            w-14
            pb-1
          "
          type="text"
        />
        <span
          @click="plus()"
          class="
            focus:outline-none
            dark:text-white
            focus:ring-2 focus:ring-offset-2 focus:ring-gray-800
            cursor-pointer
            border border-gray-300 border-l-0
            w-7
            h-7
            flex
            items-center
            justify-center
            pb-1
          "
          >+</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductDetails",
  data() {
    return {
      vehicle: {},
      quantity:1,
    }
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    plus() {
      this.quantity
      this.quantity=this.quantity + 1;
    },
    minus() {
      var preValue = document.getElementById("quantity").value;
      if (parseInt(preValue) != 0) {
          this.quantity=this.quantity - 1;
      }
    },
    getProduct() {
      const category_slug = this.$route.params.category_slug
      const category_fashion = this.$route.params.category_fashion
      const product_slug = this.$route.params.vehicle_slug

      axios
        .get(`/vehicles/${category_slug}/${category_fashion}/${product_slug}/`)
        .then(res => {
          this.vehicle = res.data;
        })
        .catch(error => {
          console.log(error);
        })
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }

      const item = {
        vehicle: this.vehicle,
        quantity: this.quantity
      }

      this.$store.commit('addToCart', item)
    }
  }
};
</script>