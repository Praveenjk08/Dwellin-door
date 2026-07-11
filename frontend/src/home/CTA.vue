<template>
    <section class="mx-4 md:mx-10 lg:mx-40 pt-5 pb-20">

        <div class="max-w-[1400px] mx-auto px-4">



            <div class="relative rounded-[10px] overflow-hidden">

                <!-- Background Image -->
                <img :src="getFiles('CTA-image.jpeg')" class="w-full h-[320px] md:h-[450px] object-cover" />

                <!-- Content -->
                <div class="absolute inset-0 flex flex-col items-center justify-center text-center px-4 md:px-6">

                    <h2
                        class="absolute top-16 md:top-36 left-4 right-4 md:left-20 md:right-20 text-white text-[20px] md:text-[33px] lg:text-[35px] font-medium leading-tight">

                        Enter a realm where exquisite design and
                        timeless luxury come together.

                    </h2>

                    <button
                        class="mt-16 md:mt-20 bg-white text-[#111] px-4 py-2 text-[12px] rounded-full font-medium hover:bg-gray-100 transition">

                        Get in touch

                    </button>

                </div>

                <!-- Bottom Strip -->
                <div class="absolute bottom-0 left-0 w-full bg-[#17C08E] text-white">

                    <div
                        class="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-10 py-3 px-4 md:px-6 text-[9px] md:text-[10px] uppercase text-center">

                        <span class="hidden md:block absolute left-0 bottom-5 w-[30px] h-[1px] bg-white/70">
                        </span>

                        <span>
                            Browse thousands of listings in prime locations at great prices!
                        </span>

                        <span class="hidden md:block w-[50px] h-[1px] bg-white/70">
                        </span>

                        <span>
                            Get a free property valuation—sell your home with confidence!
                        </span>

                        <span class="hidden md:block absolute right-0 bottom-5 w-[30px] h-[1px] bg-white/70">
                        </span>

                    </div>

                </div>

            </div>
        </div>

    </section>
</template>
<script setup>
const getFiles = (file) => {

    return `${window.location.origin}/files/${file}`

}

</script>