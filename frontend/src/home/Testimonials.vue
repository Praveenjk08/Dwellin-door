```vue
<template>
    <section class="bg-[#08141A] overflow-hidden py-10 lg:py-5 mb-20 relative">

        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-[55%_35%] gap-8 lg:gap-16 items-center">

                <!-- =====================================================
                     LEFT CONTENT
                ====================================================== -->
                <div class="w-full">

                    <div class="flex items-center gap-3 mb-6">

                        <span class="material-symbols-outlined text-[#00D3A7] text-[20px]">
                            home
                        </span>

                        <span class="text-white text-[16px] font-medium">
                            Client Testimonials
                        </span>

                    </div>

                    <h2 class="text-white text-[26px] md:text-[30px] font-semibold leading-tight mb-5">
                        What Our Bangalore Property Buyers Say
                    </h2>

                    <div class="flex gap-3 lg:gap-4">

                        <span
                            class="material-symbols-outlined text-[#00D3A7] text-[28px] lg:text-[42px] mt-1 lg:mt-2"
                        >
                            home
                        </span>

                        <div class="flex-1">

                            <p class="text-white text-[15px] md:text-[20px] leading-[1.7] font-normal">
                                {{ testimonials[currentIndex].review }}
                            </p>

                            <div class="mt-8">

                                <h4 class="text-white text-[18px] font-medium">
                                    {{ testimonials[currentIndex].name }}
                                </h4>

                                <p class="text-[#7C8A94] text-[16px] mt-1">
                                    {{ testimonials[currentIndex].role }}
                                </p>

                            </div>

                        </div>

                    </div>

                </div>


                <!-- =====================================================
                     RIGHT CONTENT
                ====================================================== -->
                <div class="relative flex flex-col items-center lg:items-end w-full">

                    <!-- =================================================
                         CURVE BORDER
                    ================================================== -->
                    <div
                        class="hidden lg:block absolute -top-40 -right-52
                               w-[600px] h-[600px]
                               border border-[#00D3A7]/40
                               rounded-[260px]"
                    >
                    </div>


                    <!-- =================================================
                         IMAGE
                    ================================================== -->
                    <div
                        class="pt-12 lg:pt-0 pb-14 lg:mt-28
                               relative z-10 w-full
                               flex justify-center lg:justify-end"
                    >

                        <img
                            :src="testimonials[currentIndex].image"
                            :alt="`${testimonials[currentIndex].name} testimonial - Dwell In Door`"
                            class="w-full max-w-full lg:max-w-[440px]
                                   h-[250px] md:h-[320px]
                                   object-cover rounded-[20px]"
                        />

                    </div>


                    <!-- =================================================
                         NAVIGATION ARROWS
                    ================================================== -->
                    <div
                        class="absolute
                               bottom-0
                               left-1/2
                               -translate-x-1/2
                               lg:top-[34px]
                               lg:bottom-auto
                               lg:left-auto
                               lg:translate-x-0
                               lg:right-[-20px]
                               flex gap-3
                               z-50"
                    >

                        <!-- PREVIOUS -->
                        <button
                            type="button"
                            @click.stop="prevSlide"
                            aria-label="Previous testimonial"
                            class="w-10 h-10
                                   rounded-full
                                   bg-white/10
                                   hover:bg-white/20
                                   active:bg-white/30
                                   text-white
                                   flex items-center justify-center
                                   transition-all duration-200
                                   cursor-pointer
                                   touch-manipulation
                                   select-none
                                   focus:outline-none"
                        >

                            <span class="material-symbols-outlined text-[22px]">
                                arrow_back
                            </span>

                        </button>


                        <!-- NEXT -->
                        <button
                            type="button"
                            @click.stop="nextSlide"
                            aria-label="Next testimonial"
                            class="w-10 h-10
                                   rounded-full
                                   bg-white/10
                                   hover:bg-white/20
                                   active:bg-white/30
                                   text-white
                                   flex items-center justify-center
                                   transition-all duration-200
                                   cursor-pointer
                                   touch-manipulation
                                   select-none
                                   focus:outline-none"
                        >

                            <span class="material-symbols-outlined text-[22px]">
                                arrow_forward
                            </span>

                        </button>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from "vue";


/* =========================================================
   TESTIMONIAL DATA
========================================================= */

const testimonials = [
    {
        name: "Anand Family",
        role: "Buyer",
        image: "/files/test1.png",
        review:
            "I found my ideal home in no time! The listings were detailed, the photos were accurate, and the whole process felt seamless. Customer service was top-notch, answering all my questions. I will definitely use this platform again in the future!"
    },
    {
        name: "Rakesh",
        role: "Property Investor",
        image: "/files/test2.png",
        review:
            "The platform made property investing incredibly easy. The team was responsive, professional, and helped me find the perfect investment opportunity."
    },
    {
        name: "Saniya Malik",
        role: "Home Owner",
        image: "/files/test3.png",
        review:
            "Excellent experience from start to finish. The listings were accurate, and the entire process was smooth and stress-free."
    }
];


/* =========================================================
   CURRENT SLIDE
========================================================= */

const currentIndex = ref(0);


/* =========================================================
   NEXT SLIDE
========================================================= */

const nextSlide = () => {
    currentIndex.value =
        (currentIndex.value + 1) % testimonials.length;
};


/* =========================================================
   PREVIOUS SLIDE
========================================================= */

const prevSlide = () => {
    currentIndex.value =
        (currentIndex.value - 1 + testimonials.length) %
        testimonials.length;
};


/* =========================================================
   AUTO SLIDER
========================================================= */

let interval;


onMounted(() => {

    interval = setInterval(() => {
        nextSlide();
    }, 6000);

});


/* =========================================================
   CLEANUP
========================================================= */

onUnmounted(() => {

    clearInterval(interval);

});
</script>
