<template>
    <section class="mx-4 md:mx-20 mt-4 mb-10">

        <img :src="blog?.image" alt="Blog Banner" class="w-full h-[250px] md:h-[480px] rounded-[16px] object-cover">

    </section>
</template>
<script setup>

defineProps({
    blog: Object
})
</script>