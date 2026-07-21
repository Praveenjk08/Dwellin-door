<template>
    <section class="bg-white my-5 mx-5   md:mx-20">

        <!-- Heading -->
        <div class="text-center mb-8">

            <div class="flex items-center justify-center gap-2 mb-2">
                <span class="w-3 h-3 rounded-full bg-[#0D5C63]"></span>
                <span class="text-[#0D5C63] text-[16px] font-medium">
                    Blog
                </span>
            </div>

            <h1 class="text-[26px] md:text-[26px] font-semibold text-[#111827]">
                Real estate insights
            </h1>

            <p class="text-[#8B8B8B] text-[13px] mt-1">
                Stay ahead in the property market with expert advice and updates
            </p>

        </div>

        <!-- Blog Cards -->

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 gap-y-10">

            <div v-for="blog in blogs" :key="blog.title" class="group px-4 rounded-xl  shadow-md"
                @click="goToBlog(blog.url)">

                <img :src="blog.image"
                    class="w-full h-[200px] object-cover rounded-xl group-hover:scale-[1.02] transition duration-300 cursor-pointer" />

                <div class="flex justify-between items-center mt-5 mb-5">

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

    </section>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

const blogs = ref([]);

const duplicatedBlogs = computed(() => {
    return [...blogs.value, ...blogs.value];
});

const router = useRouter();

const goToBlog = (url) => {
    router.push({
        name: "BlogDetailPage",
        params: {
            route: url
        }
    });
};

const get_all_blogs = async () => {
    try {
        const response = await axios.get(
            "/api/method/dwell_in_door.api.blogs.get_all_blogs"
        );

        // blogs.value = [
        //     ...response.data.message,
        //     ...response.data.message
        // ];
        blogs.value = response.data.message;
    } catch (error) {
        console.log(error);
    }
};

onMounted(() => {
    get_all_blogs();
});
</script>