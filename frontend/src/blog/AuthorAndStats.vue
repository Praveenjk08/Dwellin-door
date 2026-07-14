<template>
    <section class="mx-4 md:mx-20 mt-4 mb-4">

        <div class="flex items-center justify-between gap-4"
            v-if="blog?.author_icon && blog?.author_name && blog?.blog_date">

            <!-- Author -->
            <div class="flex items-center gap-3 min-w-0">

                <div
                    class="w-12 h-12 rounded-full bg-[#E6F4F1] border border-[#0D5C63]/10 flex items-center justify-center flex-shrink-0">

                    <span class="material-symbols-outlined text-[28px] text-[#0D5C63]">
                        {{ blog?.author_icon }}
                    </span>

                </div>

                <div class="min-w-0">
                    <h4 class="text-[14px] md:text-[15px] font-semibold text-[#222] truncate">
                        {{ blog?.author_name }}
                    </h4>
                </div>

            </div>

            <!-- Date -->
            <div class="flex items-center gap-2 text-[12px] md:text-[13px] text-[#666] whitespace-nowrap">

                <span class="material-symbols-outlined text-[18px] text-[#0D5C63]">
                    schedule
                </span>

                <span>
                    {{ blog?.blog_date }}
                </span>

            </div>

        </div>

    </section>
</template>

<script setup>
defineProps({
    blog: Object
})
</script>