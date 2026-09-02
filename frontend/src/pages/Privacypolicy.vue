```vue
<template>
    <div class="bg-white min-h-screen overflow-hidden">

        <!-- =========================================================
             HERO SECTION
        ========================================================== -->
        <section class="relative bg-[#FAF8F2] overflow-hidden">

            <!-- Decorative Shape -->
            <div
                class="absolute -top-24 -right-24 w-[420px] h-[420px] bg-[#F3EEE3] rounded-full opacity-70">
            </div>

            <div
                class="absolute -bottom-32 -left-32 w-[350px] h-[350px] bg-[#E8F1F0] rounded-full opacity-60">
            </div>

            <div class="relative z-10 max-w-[1200px] mx-auto px-6 md:px-10 py-16 md:py-20">

                <div class="max-w-3xl">

                    <p class="uppercase tracking-[3px] text-[#0D5C63] font-semibold mb-3">
                        Legal Information
                    </p>

                    <h1 class="text-4xl sm:text-5xl md:text-6xl font-bold leading-tight text-black mb-5">
                        Privacy 
                        <span class="text-[#0D5C63]">
                            Policies
                        </span>
                    </h1>

                    <p class="text-gray-600 text-base md:text-lg leading-7 max-w-2xl">
                        Please read our privacy, policies and guidelines carefully
                        before using Dwellin Door's website and services.
                    </p>

                    <div class="mt-6 flex flex-wrap gap-3">

                        <!-- <button
                            @click="scrollToSection('terms')"
                            class="bg-[#0D5C63] text-white px-5 py-3 rounded-xl font-semibold hover:bg-[#08474d] transition duration-300">
                            Terms & Conditions
                        </button> -->

                        <button
                            @click="scrollToSection('privacy')"
                            class="border border-[#0D5C63] text-[#0D5C63] px-5 py-3 rounded-xl font-semibold hover:bg-[#0D5C63] hover:text-white transition duration-300">
                            Privacy Policy
                        </button>

                    </div>

                </div>

            </div>
        </section>


        <!-- =========================================================
             MAIN CONTENT
        ========================================================== -->
        <section class="max-w-[1200px] mx-auto px-6 md:px-10 py-12 md:py-16">

            <!-- Last Updated -->
            <div
                class="mb-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 bg-[#FAF8F2] border border-[#F3EEE3] rounded-2xl px-5 py-4">

                <div class="flex items-center gap-3">
                    <div
                        class="w-10 h-10 rounded-xl bg-[#0D5C63] text-white flex items-center justify-center">
                        ✓
                    </div>

                    <div>
                        <!-- <p class="font-semibold text-[#153451]">
                            Terms & Policies
                        </p> -->
                        <p class="text-sm text-gray-500">
                            Please review these guidelines before using our website.
                        </p>
                    </div>
                </div>

                <p class="text-sm text-gray-500">
                    Last Updated: {{ lastUpdated }}
                </p>

            </div>


            <!-- =====================================================
                 TERMS & CONDITIONS
            ====================================================== -->
            <!-- <div id="terms" class="scroll-mt-24 mb-12">

                <div class="flex items-start gap-4 mb-6">

                    <div
                        class="shrink-0 w-12 h-12 rounded-2xl bg-[#0D5C63] text-white flex items-center justify-center text-xl font-bold">
                        01
                    </div>

                    <div>
                        <p class="uppercase tracking-[2px] text-xs text-[#0D5C63] font-semibold">
                            Website Usage
                        </p>

                        <h2 class="text-3xl md:text-4xl font-bold text-black">
                            Terms & Conditions
                        </h2>
                    </div>

                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

                    <div class="policy-card">
                        <h3>1. Acceptance of Terms</h3>

                        <p>
                            By accessing or using the Dwellin Door website,
                            you agree to comply with these Terms & Conditions.
                            If you do not agree with any part of these terms,
                            please discontinue use of the website.
                        </p>
                    </div>


                    <div class="policy-card">
                        <h3>2. Website Information</h3>

                        <p>
                            We make reasonable efforts to keep property details,
                            pricing, images, availability and other information
                            accurate and updated. However, information may change
                            without prior notice.
                        </p>
                    </div>


                    <div class="policy-card">
                        <h3>3. Property Listings</h3>

                        <p>
                            Property listings displayed on our website are provided
                            for informational purposes. Availability, specifications,
                            pricing, amenities and other details should be verified
                            before making any property-related decision.
                        </p>
                    </div>


                    <div class="policy-card">
                        <h3>4. Property Transactions</h3>

                        <p>
                            Information available on this website does not constitute
                            a binding offer, agreement or guarantee of sale, purchase,
                            lease or investment. Final transactions are subject to
                            applicable agreements and verification.
                        </p>
                    </div>


                    <div class="policy-card">
                        <h3>5. Intellectual Property</h3>

                        <p>
                            Website content including text, images, graphics, logos,
                            designs and other materials may be protected by applicable
                            intellectual property laws and should not be reproduced
                            without appropriate authorization.
                        </p>
                    </div>


                    <div class="policy-card">
                        <h3>6. External Links</h3>

                        <p>
                            Our website may contain links to third-party websites.
                            Dwellin Door is not responsible for the content,
                            availability or privacy practices of external websites.
                        </p>
                    </div>

                </div>

            </div> -->


            <!-- =====================================================
                 PRIVACY POLICY
            ====================================================== -->
            <div id="privacy" class="scroll-mt-24 mb-12">

                <div class="flex items-start gap-4 mb-6">

                    <div
                        class="shrink-0 w-12 h-12 rounded-2xl bg-[#0D5C63] text-white flex items-center justify-center text-xl font-bold">
                        01
                    </div>

                    <div>
                        <p class="uppercase tracking-[2px] text-xs text-[#0D5C63] font-semibold">
                            Your Information
                        </p>

                        <h2 class="text-3xl md:text-4xl font-bold text-black">
                            Privacy Policy
                        </h2>
                    </div>

                </div>


                <div class="space-y-5">

                    <div class="policy-wide">
                        <h3>Information We Collect</h3>

                        <p>
                            When you interact with our website, submit an enquiry,
                            request a callback or contact us, we may collect information
                            such as your name, phone number, email address, property
                            preferences and other information voluntarily provided by you.
                        </p>
                    </div>


                    <div class="policy-wide">
                        <h3>How We Use Your Information</h3>

                        <p>
                            Your information may be used to respond to enquiries,
                            provide requested property information, arrange callbacks,
                            improve our services and communicate with you regarding
                            relevant services or property opportunities.
                        </p>
                    </div>


                    <div class="policy-wide">
                        <h3>Protection of Information</h3>

                        <p>
                            We take reasonable measures to protect information
                            submitted through our website. However, no internet-based
                            transmission or storage system can be guaranteed to be
                            completely secure.
                        </p>
                    </div>


                    <div class="policy-wide">
                        <h3>Information Sharing</h3>

                        <p>
                            We do not intend to sell your personal information.
                            Information may be shared with relevant service providers,
                            property partners or other parties where necessary to
                            respond to your request or provide the requested service,
                            subject to applicable law.
                        </p>
                    </div>


                    <div class="policy-wide">
                        <h3>Cookies & Website Analytics</h3>

                        <p>
                            Our website may use cookies or similar technologies to
                            improve functionality, understand website usage and
                            enhance the user experience.
                        </p>
                    </div>

                </div>

            </div>


            <!-- =====================================================
                 PROPERTY DISCLAIMER
            ====================================================== -->
            <div class="mb-12">

                <div class="flex items-start gap-4 mb-6">

                    <div
                        class="shrink-0 w-12 h-12 rounded-2xl bg-[#0D5C63] text-white flex items-center justify-center text-xl font-bold">
                        02
                    </div>

                    <div>
                        <p class="uppercase tracking-[2px] text-xs text-[#0D5C63] font-semibold">
                            Important Information
                        </p>

                        <h2 class="text-3xl md:text-4xl font-bold text-black">
                            Property Disclaimer
                        </h2>
                    </div>

                </div>


                <div
                    class="relative overflow-hidden bg-[#FAF8F2] rounded-3xl p-6 md:p-8 border border-[#F3EEE3]">

                    <div
                        class="absolute -right-16 -top-16 w-40 h-40 rounded-full bg-[#E8F1F0]">
                    </div>

                    <div class="relative z-10">

                        <p class="text-gray-600 leading-7 mb-5">
                            Property images, floor plans, specifications, dimensions,
                            amenities, prices and other project information displayed
                            on this website are subject to change and may vary from
                            the actual property.
                        </p>

                        <p class="text-gray-600 leading-7 mb-5">
                            Users are advised to independently verify all relevant
                            information, approvals, documentation, pricing,
                            availability and other details with the concerned
                            developer, seller or authorized representative before
                            making a purchase or investment decision.
                        </p>

                        <div
                            class="flex items-start gap-3 bg-white rounded-2xl p-4 border border-gray-100">

                            <span class="text-[#0D5C63] text-xl">
                                ⚠
                            </span>

                            <p class="text-sm text-gray-600 leading-6">
                                Dwellin Door does not guarantee the completeness,
                                accuracy or availability of every property listing
                                displayed on the website.
                            </p>

                        </div>

                    </div>

                </div>

            </div>


            <!-- =====================================================
                 USER RESPONSIBILITIES
            ====================================================== -->
            <div class="mb-12">

                <div class="flex items-start gap-4 mb-6">

                    <div
                        class="shrink-0 w-12 h-12 rounded-2xl bg-[#0D5C63] text-white flex items-center justify-center text-xl font-bold">
                        03
                    </div>

                    <div>
                        <p class="uppercase tracking-[2px] text-xs text-[#0D5C63] font-semibold">
                            Responsible Usage
                        </p>

                        <h2 class="text-3xl md:text-4xl font-bold text-black">
                            User Responsibilities
                        </h2>
                    </div>

                </div>


                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">

                    <div class="responsibility-card">
                        <span>01</span>
                        <h3>Accurate Information</h3>
                        <p>
                            Provide accurate and genuine information when submitting
                            enquiries or contact forms.
                        </p>
                    </div>


                    <div class="responsibility-card">
                        <span>02</span>
                        <h3>Lawful Use</h3>
                        <p>
                            Use the website only for lawful purposes and in accordance
                            with applicable regulations.
                        </p>
                    </div>


                    <div class="responsibility-card">
                        <span>03</span>
                        <h3>No Misuse</h3>
                        <p>
                            Do not attempt to disrupt, damage or interfere with
                            the operation or security of the website.
                        </p>
                    </div>

                </div>

            </div>


            <!-- =====================================================
                 CONTACT
            ====================================================== -->
            <div
                class="relative overflow-hidden bg-[#0D5C63] rounded-3xl p-7 md:p-10 text-white">

                <div
                    class="absolute -right-20 -top-20 w-64 h-64 rounded-full border-[50px] border-white/5">
                </div>

                <div
                    class="absolute -left-20 -bottom-24 w-60 h-60 rounded-full bg-white/5">
                </div>

                <div class="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-7">

                    <div class="max-w-2xl">

                        <p class="uppercase tracking-[3px] text-white/60 font-semibold text-sm mb-3">
                            Need Assistance?
                        </p>

                        <h2 class="text-3xl md:text-4xl font-bold mb-3">
                            Have questions about our policies?
                        </h2>

                        <p class="text-white/75 leading-7">
                            If you have any questions regarding these terms,
                            privacy practices or property information, feel free
                            to get in touch with our team.
                        </p>

                    </div>

                    <button
                        @click="router.push('/contact-us')"
                        class="shrink-0 bg-white text-[#0D5C63] px-6 py-3 rounded-xl font-semibold hover:bg-[#F3EEE3] transition duration-300">
                        Contact Us
                    </button>
                    

                </div>

            </div>

        </section>

    </div>
</template>


<script setup>

import router from '../router.js';

const lastUpdated = 'August 31, 2026';

const scrollToSection = (id) => {
    const element = document.getElementById(id);

    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
};

</script>


<style scoped>

.policy-card {
    background: white;
    border: 1px solid #eeeeee;
    border-radius: 20px;
    padding: 24px;
    transition: all 0.3s ease;
}

.policy-card:hover {
    transform: translateY(-4px);
    border-color: #dcebea;
    box-shadow: 0 12px 30px rgba(13, 92, 99, 0.08);
}

.policy-card h3,
.policy-wide h3 {
    color: #153451;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 10px;
}

.policy-card p,
.policy-wide p {
    color: #6b7280;
    line-height: 1.8;
    font-size: 15px;
}

.policy-wide {
    background: #ffffff;
    border: 1px solid #eeeeee;
    border-radius: 20px;
    padding: 25px;
    transition: all 0.3s ease;
}

.policy-wide:hover {
    border-color: #dcebea;
    box-shadow: 0 10px 25px rgba(13, 92, 99, 0.06);
}

.responsibility-card {
    background: #faf8f2;
    border: 1px solid #f3eee3;
    border-radius: 22px;
    padding: 25px;
    transition: all 0.3s ease;
}

.responsibility-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(13, 92, 99, 0.08);
}

.responsibility-card span {
    display: inline-flex;
    width: 40px;
    height: 40px;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: #0d5c63;
    color: white;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 18px;
}

.responsibility-card h3 {
    color: #153451;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
}

.responsibility-card p {
    color: #6b7280;
    font-size: 14px;
    line-height: 1.7;
}

html {
    scroll-behavior: smooth;
}

</style>
