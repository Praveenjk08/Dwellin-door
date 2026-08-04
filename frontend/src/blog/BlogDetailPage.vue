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

const setBlogSeo = () => {
    const blog = source.value?.[0] || {};
    const title = `${blog.blog_heading || 'Real Estate Blog'} | Dwell In Door`;
    const description = (blog.small_description || 'Read expert real estate articles, property investing tips, and latest market trends from Dwell In Door.').slice(0, 160);
    const image = blog.image || 'https://www.dwellindoor.com/files/logo-with-some-changes.png';
    const currentUrl = `${window.location.origin}${route.fullPath}`;

    document.title = title;

    const updateMetaByAttribute = (attribute, key, content) => {
        let tag = document.querySelector(`meta[${attribute}="${key}"]`);

        if (!tag) {
            tag = document.createElement('meta');
            tag.setAttribute(attribute, key);
            document.head.appendChild(tag);
        }

        tag.setAttribute('content', content || '');
    };

    updateMetaByAttribute('name', 'description', description);
    updateMetaByAttribute('name', 'keywords', `${blog.blog_heading || 'real estate blog'}, Dwell In Door, Bangalore real estate, property tips, home buying guide`);
    updateMetaByAttribute('property', 'og:title', title);
    updateMetaByAttribute('property', 'og:description', description);
    updateMetaByAttribute('property', 'og:type', 'article');
    updateMetaByAttribute('property', 'og:url', currentUrl);
    updateMetaByAttribute('property', 'og:image', image);
    updateMetaByAttribute('name', 'twitter:card', 'summary_large_image');
    updateMetaByAttribute('name', 'twitter:title', title);
    updateMetaByAttribute('name', 'twitter:description', description);
    updateMetaByAttribute('name', 'twitter:image', image);
};

const setBlogSchema = () => {
    const blog = source.value?.[0] || {};
    const schema = {
        '@context': 'https://schema.org',
        '@type': 'Article',
        headline: blog.blog_heading || 'Real Estate Blog',
        description: blog.small_description || 'Real estate insights and market trends from Dwell In Door.',
        image: blog.image || 'https://www.dwellindoor.com/files/logo-with-some-changes.png',
        url: `${window.location.origin}${route.fullPath}`,
        author: {
            '@type': 'Organization',
            name: 'Dwell In Door'
        },
        publisher: {
            '@type': 'Organization',
            name: 'Dwell In Door',
            logo: {
                '@type': 'ImageObject',
                url: 'https://www.dwellindoor.com/files/logo-with-some-changes.png'
            }
        }
    };

    let scriptTag = document.querySelector('#blog-schema');

    if (!scriptTag) {
        scriptTag = document.createElement('script');
        scriptTag.id = 'blog-schema';
        scriptTag.type = 'application/ld+json';
        document.head.appendChild(scriptTag);
    }

    scriptTag.textContent = JSON.stringify(schema);
};

const get_blog_detail = async () => {
    try {

        const response = await axios.get(
            `/api/method/dwell_in_door.api.blogs.get_blog_detail?route=${route.params.route}`
        );

        source.value = response.data.message;
        setBlogSeo();
        setBlogSchema();

    } catch (error) {
        console.log(error);
    }
};

onMounted(() => {
    get_blog_detail();
});

</script>