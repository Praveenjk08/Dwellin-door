<template>
    <section class="mx-4 md:mx-20 my-5">
        <div v-for="(item, index) in source" :key="index">
            <!-- Category -->

            <div class=" mb-6">
                <span v-if="item?.advice"
                    class="bg-[#F2F2F2] text-[#333] text-[12px] px-4 py-2 rounded-full font-medium">
                    {{ item.advice }}
                </span>
            </div>

            <!-- Title -->
            <h1 v-if="item?.blog_heading" class="text-[22px] md:text-[32px] font-semibold text-[#111827] leading-[1.1]">
                <!-- Top 5 tips for first-time home buyers navigating the market -->
                {{ item.blog_heading }}
            </h1>

            <!-- Description -->
            <p v-if="item?.small_description" class="text-[#8B8B8B] text-[15px] md:text-[13px] mt-4 leading-6 ">
                <!-- Buying your first home is an exciting milestone, but it can also feel overwhelming
                with so many factors to consider. To help you make informed decisions, here are the
                top five tips for first-time home buyers to successfully navigate the real estate market. -->
                {{ item.small_description }}
            </p>
        </div>

    </section>

    <AuthorAndStats v-if="source?.length" :blog="source[0]" />
    <BlogIamgeSection v-if="source[0]?.image" :blog="source[0]" />
    <BlogDescriptionANdImage v-if="source?.length" :blog="source[0]" />
    <BlogQuestions :v-if="source.length" :blog="source[0]" />
</template>

<script setup>
import AuthorAndStats from './AuthorAndStats.vue';
import BlogDescriptionANdImage from './BlogDescriptionANdImage.vue';
import BlogIamgeSection from './BlogIamgeSection.vue';
import BlogQuestions from './BlogQuestions.vue';

import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";


const route = useRoute();

const source = ref([]);

const get_blog_detail = async () => {
    try {

        const response = await axios.get(
            `/api/method/dwell_in_door.api.blogs.get_blog_detail?route=${route.params.route}`
        );

        source.value = response.data.message;

    } catch (error) {
        console.log(error);
    }
};

onMounted(() => {
    get_blog_detail();
});

</script>