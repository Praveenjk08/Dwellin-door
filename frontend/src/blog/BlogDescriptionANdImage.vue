<template>
    <section class="mx-4 md:mx-20 mt-8 mb-10">

        <!-- First Paragraphs -->
        <!-- <p class="text-[14px] text-[#444] leading-6 mb-4">
            Mi tincidunt elit, id quisque ligula ac diam, amet. Vel etiam suspendisse
            morbi eleifend faucibus eget vestibulum felis. Dictum quis montes, sit sit.
            Tellus aliquam enim urna, etiam. Mauris posuere vulputate arcu amet,
            vitae nisi, tellus tincidunt. At feugiat sapien varius id.
            

        </p> -->

        <!-- <p class="text-[14px] text-[#444] leading-6 mb-4">
            Eget quis mi enim, leo lacinia pharetra, semper. Eget in volutpat mollis
            at volutpat lectus velit, sed auctor. Porttitor fames arcu quis fusce
            augue enim. Quis at habitant diam at. Suscipit tristique risus, at donec.
            In turpis vel et quam imperdiet. Ipsum molestie aliquet sodales id est
            ac volutpat.
        </p> -->

        <div class="text-[14px] text-[#444] leading-6 mb-4" v-if="blog?.description1" v-html="blog?.description1"></div>

        <!-- Quote Block -->
        <div class="border-l-[4px] border-[#10D19D] pl-6">

            <!-- <p class="text-[16px] font-semibold text-[#222] leading-8">
                Mi tincidunt elit, id quisque ligula ac diam, amet. Vel etiam
                suspendisse morbi eleifend faucibus eget vestibulum felis.
                Dictum quis montes, sit sit. Tellus aliquam enim urna, etiam.
                Mauris posuere vulputate arcu amet, vitae nisi, tellus
                tincidunt. At feugiat sapien varius id.
            </p>

            <p class="mt-5 text-[14px] text-[#555]">
                — Arlene McCoy, Golden Paws Breeders
            </p> -->


            <div class="text-[16px] font-semibold text-[#222] leading-8" v-html="blog?.descrption_2"></div>

        </div>

        <!-- Content + Image -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-0 md:gap-12 mt-6 items-center"
            v-if="blog?.descrption_2 && blog?.image">

            <div class="lg:col-span-8">

                <!-- <p class="text-[14px] text-[#444] leading-7 mb-4">
                    Mi tincidunt elit, id quisque ligula ac diam, amet. Vel etiam suspendisse
                    morbi eleifend faucibus eget vestibulum felis. Dictum quis montes, sit sit.
                    Tellus aliquam enim urna, etiam. Mauris posuere vulputate arcu amet,
                    vitae nisi, tellus tincidunt. At feugiat sapien varius id. Mi tincidunt
                    elit, id quisque ligula ac diam, amet. Vel etiam suspendisse morbi
                    eleifend faucibus eget vestibulum felis. Dictum quis montes, sit sit.
                    Tellus aliquam enim urna, etiam. Mauris posuere vulputate arcu amet,
                    vitae nisi, tellus tincidunt. At feugiat sapien varius id.
                </p>

                <p class="text-[14px] text-[#444] leading-7">
                    Eget quis mi enim, leo lacinia pharetra, semper. Eget in volutpat mollis
                    at volutpat lectus velit, sed auctor. Porttitor fames arcu quis fusce
                    augue enim. Quis at habitant diam at. Suscipit tristique risus, at donec.
                    In turpis vel et quam imperdiet. Ipsum molestie aliquet sodales id est
                    ac volutpat.
                </p> -->
                <div class="description-three text-[14px] text-[#444] leading-7" v-html="blog?.descrption_3"></div>

            </div>
            <div class="lg:col-span-4">
                <img :src="blog?.image" class="w-full h-[260px]  object-cover rounded-[18px]">
            </div>

        </div>

    </section>
</template>

<script setup>
defineProps({
    blog: Object
})


</script>
<!-- <style>
.ql-editor p {
    margin-bottom: 16px;
}

.ql-editor p:last-child {
    margin-bottom: 0;
}
</style> -->