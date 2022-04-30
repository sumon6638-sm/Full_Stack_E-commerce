<template>
  <div
    class="
      w-full
      mx-auto
      dark-mode:text-gray-200 dark-mode:bg-gray-800
      sticky
      top-0
      z-50
      md:mt-0
      p-4
      bg-black
    "
  >
    <div
      class="
        container
        flex flex-col
        max-w-screen-xl
        mx-auto
        md:items-center md:justify-between md:flex-row
      "
    >
      <div class="md:pb-4 lg:pr-4 flex flex-row items-center justify-between">
        <a
          href="#"
          class="
            text-lg
            font-semibold
            tracking-widest
            text-gray-300
            uppercase
            rounded-lg
            dark-mode:text-white
            focus:outline-none focus:shadow-outline
          "
        >
          <router-link to="/" class="font-bold my-10">EasyToBuy</router-link>
        </a>
        <button
          class="
            md:hidden
            rounded-lg
            focus:outline-none focus:shadow-outline
            self-start
            mt-3
            mr-4
          "
          @click="openNav = !openNav"
        >
          <!-- <svg fill="currentColor" viewBox="0 0 20 20" class="w-6 h-6">
            <path
              x-show="!open"
              fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z"
              clip-rule="evenodd"
            ></path>
            <path
              x-show="open"
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg> -->
          <img
            v-if="!openNav"
            class="h-[17px] w-[26px] text-white"
            src="@/assets/menu-icon.svg"
            alt=""
          />
          <img
            v-else
            class="h-[17px] w-[26px] text-white"
            src="@/assets/cross.svg"
            alt=""
          />
        </button>
      </div>
      <nav
        class="
          flex-col flex-grow
          hidden
          self-start
          md:flex md:justify-end md:flex-row
        "
        :class="[
          scrollPosition > 50
            ? 'fixed top-0 right-0 z-10 w-[100vw] bg-[#0b0b0b] mt-0 pr-[3%] xl:pr-[4%] 2xl:pr-[15.5%] transition-all ease-in-out duration-300'
            : 'pb-4 md:pb-0',
        ]"
      >
        <a
          class="
            self-center
            px-8
            py-2
            mt-2
            text-sm
            font-semibold
            text-white
            rounded-lg
            md:mt-0
            hover:text-[#27E278]
            focus:text-[#27E278] focus:outline-none focus:shadow-outline
          "
          href="/home"
          >HOME</a
        >
        <a
          class="
            self-center
            px-8
            py-2
            mt-2
            text-sm
            font-semibold
            text-white
            rounded-lg
            md:mt-0
            hover:text-[#27E278]
            focus:text-[#27E278] focus:outline-none focus:shadow-outline
          "
          href="/about"
          >ABOUT</a
        >
        <a
          class="
            self-center
            items-center
            px-8
            py-2
            mt-2
            text-sm
            flex
            font-semibold
            text-white
            rounded-lg
            md:mt-0
            hover:text-[#27E278]
            focus:text-[#27E278] focus:outline-none focus:shadow-outline
          "
          href="/product"
          >PRODUCT
          <!-- <img
            class="w-[30px] h-[30px] mt-[-2px]"
            src="@/assets/images/spark.png"
          /> -->
        </a>
        <div>
          <div
            @click="showVehicle = !showVehicle"
            class="
              self-center
              px-8
              py-2
              mt-2
              whitespace-nowrap
              text-sm
              font-semibold
              text-white
              rounded-lg
              md:mt-0
              hover:text-[#27E278]
              focus:text-[#27E278] focus:outline-none focus:shadow-outline
            "
          >
            VEHICLE
          </div>
          <div v-if="showVehicle" class="text-white bg-black">
            <ul>
              <li><div @click="showCar =! showCar">CAR</div></li>
              <li><div @click="showBike =! showBike">BIKE</div></li>
            </ul>
          </div>

          <div v-if="showCar" class="text-white bg-black">
            <ul>
              <li><a href="/car/new-car">NEW CAR</a></li>
              <li><a href="/car/old-car">OLD CAR</a></li>
            </ul>
          </div>

          <div v-if="showBike" class="text-white bg-black">
            <ul>
              <li><a href="/bike/new-bike">NEW BIKE</a></li>
              <li><a href="/bike/new-bike">OLD BIKE</a></li>
            </ul>
          </div>
        </div>
        <a
          class="
            self-center
            px-8
            py-2
            mt-2
            text-sm
            whitespace-nowrap
            font-semibold
            text-white
            rounded-lg
            md:mt-0
            hover:text-[#27E278]
            focus:text-[#27E278] focus:outline-none focus:shadow-outline
          "
          href="#"
          >BUY NOW</a
        >
        <button
          class="
            bg-green-500
            hover:bg-green-800
            text-black
            font-bold
            py-2
            px-4
            rounded
          "
        >
          Log In
        </button>
        <button
          class="
            ml-5
            bg-blue-500
            hover:bg-blue-700
            text-white
            font-bold
            py-2
            px-4
            rounded
          "
        >
          <span><i class="fa-solid fa-cart-arrow-down"></i></span>
          <span>Cart</span>
        </button>
        <a
          class="
            self-center
            items-center
            px-4
            xl:px-8
            py-2
            mt-2
            text-sm
            flex
            font-semibold
            text-black
            rounded-lg
            md:mt-0
            hover:text-[#27E278]
            focus:text-[#27E278] focus:outline-none focus:shadow-outline
          "
          href="#"
        >
          <!-- <img
            class="w-[30px] h-[30px] mt-[-2px]"
            src="@/assets/images/telegram.png"
          /> -->
        </a>
      </nav>

      <!-- For Mobile Header -->
      <nav
        v-if="openNav"
        class="md:hidden w-[95%] absolute mt-[60px] mx-auto pr-0"
      >
        <div
          class="
            navbar-collapse
            justify-content-end
            mCustomScrollbar
            _mCS_1
            collapse
            show
            mCS_no_scrollbar
          "
          id="navbarSupportedContent"
          style="top: 60px; display: block"
        >
          <div
            id="mCSB_1"
            class="mCustomScrollBox mCS-dark mCSB_vertical mCSB_inside"
            style="max-height: none"
            tabindex="0"
          >
            <div
              id="mCSB_1_container"
              class="mCSB_container mCS_y_hidden mCS_no_scrollbar_y"
              style="position: relative; top: 0; left: 0"
              dir="ltr"
            >
              <ul class="navbar-nav">
                <li class="text-left">
                  <a
                    class="
                      px-4
                      py-2
                      mt-2
                      text-sm
                      font-semibold
                      text-white
                      rounded-lg
                      md:mt-0
                      hover:text-[#27E278]
                      focus:text-[#27E278]
                      focus:outline-none
                      focus:shadow-outline
                    "
                    href="/home"
                    >HOME</a
                  >
                </li>
                <li class="text-left">
                  <a
                    class="
                      self-center
                      items-center
                      px-4
                      py-2
                      text-sm
                      flex
                      font-semibold
                      text-white
                      rounded-lg
                      md:mt-0
                      hover:text-[#27E278]
                      focus:text-[#27E278]
                      focus:outline-none
                      focus:shadow-outline
                    "
                    href="#"
                    >PRODUCT
                    <!-- <img
                      class="w-[30px] h-[30px] mt-[-2px]"
                      src="@/assets/images/spark.png"
                    /> -->
                  </a>
                </li>
                <li class="text-left">
                  <a
                    class="
                      self-center
                      px-4
                      py-2
                      mt-2
                      whitespace-nowrap
                      text-sm
                      font-semibold
                      text-white
                      rounded-lg
                      md:mt-0
                      hover:text-[#27E278]
                      focus:text-[#27E278]
                      focus:outline-none
                      focus:shadow-outline
                    "
                    href="#"
                    >VEHICLE</a
                  >
                </li>
                <li class="text-left pt-4">
                  <a
                    class="
                      self-center
                      px-4
                      py-2
                      mt-2
                      text-sm
                      whitespace-nowrap
                      font-semibold
                      text-white
                      rounded-lg
                      md:mt-0
                      hover:text-[#27E278]
                      focus:text-[#27E278]
                      focus:outline-none
                      focus:shadow-outline
                    "
                    href="#"
                    >BUY NOW</a
                  >
                </li>
                <li class="text-left">
                  <a
                    class="
                      self-center
                      items-center
                      px-4
                      py-2
                      text-sm
                      flex
                      font-semibold
                      text-white
                      rounded-lg
                      md:mt-0
                      hover:text-[#27E278]
                      focus:text-[#27E278]
                      focus:outline-none
                      focus:shadow-outline
                    "
                    href="#"
                    >TELEGRAM
                    <!-- <img
                      class="w-[30px] h-[30px] mt-[-2px]"
                      src="@/assets/images/telegram.png"
                    /> -->
                  </a>
                </li>
              </ul>
            </div>
            <div
              id="mCSB_1_scrollbar_vertical"
              class="
                mCSB_scrollTools mCSB_1_scrollbar
                mCS-dark
                mCSB_scrollTools_vertical
              "
              style="display: none"
            >
              <div class="mCSB_draggerContainer">
                <div
                  id="mCSB_1_dragger_vertical"
                  class="mCSB_dragger"
                  style="
                    position: absolute;
                    min-height: 30px;
                    top: 0px;
                    height: 0px;
                    display: block;
                  "
                >
                  <div class="mCSB_dragger_bar" style="line-height: 30px"></div>
                </div>
                <div class="mCSB_draggerRail"></div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      openNav: false,
      scrollPosition: null,
      showVehicle: false,
      showCar: false,
      showBike: false,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },
  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
  },
};
</script>

<style scoped>
.navbar-collapse {
  background-color: #101227;
  padding: 10px;
}
</style>