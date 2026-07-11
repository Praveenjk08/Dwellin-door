<template>
    <section class="mb-10  lg:mx-40 ">
        <!-- <section class="py-12 md:py-12 bg-white px-4 md:px-6 lg:px-0 lg:mx-40"> -->

        <div class="max-w-[1400px] mx-auto px-4">

            <!-- Header -->
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between mb-6">

                <div>

                    <div class="flex items-center gap-3 mb-2">

                        <span class="material-symbols-outlined text-[#00D3A7] text-[14px]">
                            home
                        </span>

                        <span class="text-[#4B5A63] text-[14px] font-medium">
                            Blog
                        </span>

                    </div>

                    <h2 class="text-[23px] md:text-[33px] font-semibold text-[#131A20] leading-tight">
                        Real estate insights
                    </h2>

                    <p class="text-[#8B8B8B] text-[13px] mt-2">
                        Stay ahead in the property market with expert advice and updates
                    </p>

                </div>

                <button
                    class="mt-0 lg:mt-0 bg-[#0D1A20] text-white py-3 px-5    rounded-full text-[10px] font-medium hover:bg-[#15242C] transition">
                    Read all articles
                </button>

            </div>

            <!-- Blog Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

                <div v-for="blog in blogs" :key="blog.title" class="group ">

                    <img :src="blog.image"
                        class="w-full h-[200px] object-cover rounded-[20px] group-hover:scale-[1.02] transition duration-300 cursor-pointer" />

                    <div class="flex justify-between items-center mt-5">

                        <div>
                            <h3 class="text-[14px] font-semibold text-[#222]">
                                {{ blog.blog_name }}
                            </h3>

                            <p class="text-[#8B8B8B] text-[12px] mt-1">
                                {{ blog.blog_date }}
                            </p>
                        </div>

                        <span class="bg-[#EEEEEE] text-[#333] text-[10px] px-3 py-2 rounded-full font-medium">
                            {{ blog.advice }}
                        </span>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
import axios from "axios";

import { onMounted, ref } from "vue";

// const blogs = ref([
//     {
//         title: "Home buying tips",
//         date: "Feb 17, 2024",
//         category: "Tips",
//         image: "blog-image-1"
//     },
//     {
//         title: "Boost home value",
//         date: "Feb 18, 2024",
//         category: "Guides",
//         image: "blog-image-2"
//     },
//     {
//         title: "Mortgage rates update",
//         date: "Feb 19, 2024",
//         category: "Updates",
//         image: "blog-image-3"
//     }
// ]);
const blogs = ref([])

const get_all_blogs = async () => {
    try {
        const response = await axios.get("/api/method/dwell_in_door.api.blogs.get_all_blogs")
        blogs.value = response.data.message
    }
    catch (error) {
        console.log(error);

    }
}


onMounted(() => {
    get_all_blogs()
})
</script>