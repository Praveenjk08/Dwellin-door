<template>
    <section class="mx-4 md:mx-20 mb-10">

        <!-- Heading -->
        <p class="text-[#0D5C63] font-semibold uppercase text-[18px] md:text-[20px]">
            What Our Clients Say
        </p>

        <div class="w-16 h-[3px] bg-[#D4AF37] mb-8 md:mb-10"></div>

        <!-- Carousel -->
        <Carousel :items-to-show="1" :wrap-around="true" :autoplay="5000" :breakpoints="{
            768: {
                itemsToShow: 2
            },
            1024: {
                itemsToShow: 3
            }
        }">

            <Slide v-for="(review, index) in reviews" :key="index">

                <div
                    class="bg-white border border-gray-100 rounded-[20px] shadow-sm p-4 md:p-5 mx-2 h-[200px] flex flex-col">

                    <!-- Stars -->
                    <div class="flex gap-1 mb-2">
                        <span v-for="i in 5" :key="i" class="text-[#D4AF37] text-sm md:text-lg">
                            ★
                        </span>
                    </div>

                    <!-- Review -->
                    <p class="text-gray-700 text-[13px] md:text-[14px] leading-6 flex-1 line-clamp-3">
                        "{{ review.review }}"
                    </p>

                    <!-- Profile -->
                    <div class="flex items-center gap-2 mt-2">

                        <img :src="review.image" :alt="review.name"
                            class="w-9 h-9 md:w-10 md:h-10 rounded-full object-cover flex-shrink-0 border border-gray-200" />

                        <div class="leading-tight">
                            <h4 class="font-semibold text-[14px] md:text-[15px] text-black">
                                {{ review.name }}
                            </h4>

                            <p class="text-gray-500 text-[11px] md:text-xs">
                                {{ review.role }}
                            </p>
                        </div>

                    </div>

                </div>

            </Slide>

            <template #addons>
                <Navigation />
            </template>

        </Carousel>

    </section>
</template>

<script setup>
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const reviews = [
    {
        name: 'Rakesh Sharma',
        role: 'Happy Homeowner',
        image: 'https://i.pravatar.cc/150?img=12',
        review: 'Dwellin Door made our property search effortless. Their guidance and transparency gave us complete confidence throughout the process.'
    },
    {
        name: 'Neha Patel',
        role: 'Property Investor',
        image: 'https://i.pravatar.cc/150?img=5',
        review: 'Professional team, great locations and excellent support. Highly recommended for anyone looking to buy property.'
    },
    {
        name: 'Arjun Mehta',
        role: 'Satisfied Customer',
        image: 'https://i.pravatar.cc/150?img=15',
        review: 'Found the perfect home for my family with the help of Dwellin Door. Truly a wonderful experience!'
    }
]




</script>

<style>
.carousel {
    position: relative;
    padding: 0 10px;
}

.carousel__track {
    padding-bottom: 10px;
}

.carousel__prev,
.carousel__next {
    width: 45px;
    height: 45px;
    border-radius: 9999px;
    background: #f5f5f5;
    color: #0D5C63;
    border: none;
    transition: all 0.3s ease;
}

.carousel__prev:hover,
.carousel__next:hover {
    background: #0D5C63;
    color: white;
}

.carousel__prev {
    left: -20px;
}

.carousel__next {
    right: -20px;
}

.line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

@media (max-width: 768px) {

    .carousel__prev,
    .carousel__next {
        width: 35px;
        height: 35px;
    }

    .carousel__prev {
        left: -5px;
    }

    .carousel__next {
        right: -5px;
    }
}
</style>