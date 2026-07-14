<template>
    <section class="mx-4 md:pb-10 md:px-2   md:mx-20 my-5 overflow-hidden">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">

            <!-- Left Image -->
            <div class="lg:col-span-4">

                <div class="relative">

                    <img :src="getFileUrl('About-usleft-sde-image.jpeg')" alt="About Dwellin Door"
                        class="w-full h-[320px] md:h-[400px] rounded-lg object-cover shadow-lg" />

                    <!-- Floating Card -->
                    <div class="absolute bottom-4 left-4 md:-bottom-6 md:-left-2
                    bg-[#0D5C63] text-white px-4 py-3 md:px-6 md:py-4
                    rounded-lg shadow-xl">
                        <div class="flex items-center gap-3">

                            <span class="material-symbols-outlined text-[28px] md:text-[35px]">
                                groups
                            </span>

                            <div>
                                <h3 class="text-xl md:text-3xl font-bold">
                                    100+
                                </h3>

                                <p class="text-xs md:text-sm text-white/80">
                                    Happy Clients
                                </p>
                            </div>

                        </div>
                    </div>

                </div>

            </div>

            <!-- Center Content -->
            <div class="lg:col-span-5 text-center lg:text-left">

                <p class="text-[#0D5C63] uppercase font-semibold text-[22px] md:text-[22px] ">
                    Who We Are
                </p>

                <h2 class="text-[22px] md:text-[18px] font-semibold text-black leading-tight mb-2">
                    Your Trusted Real Estate Partner
                </h2>

                <p class="text-gray-700 leading-7 md:leading-6 text-[14px] mb-2">
                    Dwellin Door is a trusted real estate platform dedicated to
                    helping individuals and families find their ideal homes,
                    villas, apartments, plots and investment opportunities.
                </p>

                <p class="text-gray-700 leading-7 md:leading-6 text-[14px] mb-2">
                    With a commitment to transparency, professionalism and customer
                    satisfaction, we simplify the property search process while
                    delivering personalized guidance at every step.
                </p>

                <p class="text-gray-700 leading-7 md:leading-6 text-[14px]">
                    Our mission is to connect people with spaces that perfectly
                    align with their lifestyle, aspirations and future goals.
                </p>

                <!-- Signature -->
                <div class="mt-3 text-center lg:text-left">

                    <p class="text-3xl md:text-4xl italic text-[#0D5C63] font-serif leading-none">
                        Dwellin Door
                    </p>

                    <p class="text-sm text-gray-400 mb-3">
                        Founder Signature
                    </p>

                    <div class="w-24 border-b border-gray-300 mb-3 mx-auto lg:mx-0"></div>

                    <h4 class="font-semibold text-black text-lg">
                        Team Dwellin Door
                    </h4>

                </div>

            </div>

            <!-- Right Features -->
            <div class="lg:col-span-3
            lg:border-l border-gray-200
            lg:pl-8
            space-y-6 md:space-y-6">

                <!-- Feature 1 -->
                <div class="flex gap-4">

                    <div
                        class="w-14 h-14 md:w-16 md:h-16 rounded-full bg-[#F5F8F8] flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-[32px] md:text-[36px] text-[#0D5C63]">
                            verified_user
                        </span>
                    </div>

                    <div>
                        <h3 class="font-semibold text-lg text-black mb-1">
                            Verified Properties
                        </h3>

                        <p class="text-gray-700 text-sm">
                            Every listing is carefully verified for authenticity
                            and reliability.
                        </p>
                    </div>

                </div>

                <!-- Feature 2 -->
                <div class="flex gap-4">

                    <div class="w-14 h-14 rounded-full bg-[#F5F8F8] flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-[32px] md:text-[36px] text-[#0D5C63]">
                            groups
                        </span>
                    </div>

                    <div>
                        <h3 class="font-semibold text-lg text-black mb-1">
                            Trusted Guidance
                        </h3>

                        <p class="text-gray-700 text-sm">
                            Our experienced team provides honest advice and support.
                        </p>
                    </div>

                </div>

                <!-- Feature 3 -->
                <div class="flex gap-4">

                    <div class="w-14 h-14 rounded-full bg-[#F5F8F8] flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-[32px] md:text-[36px] text-[#0D5C63]">
                            location_on
                        </span>
                    </div>

                    <div>
                        <h3 class="font-semibold text-lg text-black mb-1">
                            Prime Locations
                        </h3>

                        <p class="text-gray-700 text-sm">
                            Discover properties in rapidly growing and high-value areas.
                        </p>
                    </div>

                </div>

                <!-- Feature 4 -->
                <div class="flex gap-4">

                    <div class="w-14 h-14 rounded-full bg-[#F5F8F8] flex items-center justify-center flex-shrink-0">
                        <span class="material-symbols-outlined text-[32px] md:text-[36px] text-[#0D5C63]">
                            star
                        </span>
                    </div>

                    <div>
                        <h3 class="font-semibold text-lg text-black mb-1">
                            Customer Satisfaction
                        </h3>

                        <p class="text-gray-700 text-sm">
                            Building long-term relationships through exceptional service.
                        </p>
                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};
</script>