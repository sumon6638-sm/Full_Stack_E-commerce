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
import { useToast, POSITION } from "vue-toastification";

export default {
  name: "VehicleDetails",
  data() {
    return {
      vehicle: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  setup() {
    const toast = useToast();

    return { toast };
  },
  methods: {
    plus() {
      this.quantity;
      this.quantity = this.quantity + 1;
    },
    minus() {
      var preValue = document.getElementById("quantity").value;
      if (parseInt(preValue) != 0) {
        this.quantity = this.quantity - 1;
      }
    },
    async getProduct() {
      console.log('hello')
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const vehicle_slug = this.$route.params.vehicle_slug;
      const vehicle_url = this.$route.params.vehicle_url;

      console.log(this.$route.params, category_slug, vehicle_slug, vehicle_url, 'url')

      await axios
        .get(`/vehicles/${category_slug}/${vehicle_slug}/${vehicle_url}/`)
        .then((res) => {
          this.vehicle = res.data;
          console.log(this.vehicle, 'hello')

          document.title = this.vehicle.name + ' | EasyToBuy'
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        vehicle: this.vehicle,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);
      this.toast.success("Vehicle added successfully!!!", {
        position: POSITION.TOP_CENTER,
      });
    },
  },
};
</script>