import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/home/Home.vue'),
    meta: {
      title: 'Dwell In Door | Premium Real Estate in Bangalore',
      description: 'Discover premium apartments, villas, plots, and luxury homes with Dwell In Door. Find your dream property today.',
      keywords: 'Dwell In Door, real estate, apartments, villas, plots, luxury homes, Bangalore properties,qb'
    }

  },

  // {
  //   path: "/detailpage",
  //   name: "detailpage",
  //   component: () => import('@/pages/DetailPage.vue')

  // },
  {
  path: "/properties",
  name: "properties",
  component: () => import("@/pages/PropertyList.vue"),
  meta: {
    title: "Properties in Bangalore | Dwell In Door - Apartments, Villas & Plots",
    description:
      "Explore premium apartments, villas, plots, and luxury properties with Dwell In Door. Find your perfect property with detailed information, pricing, and amenities.",
    keywords:
      "properties, apartments for sale, villas, plots, luxury homes, real estate, Bangalore properties, Dwell In Door"
  }
},

 {
  path: "/properties/:url",
  name: "PropertyDetail",
  component: () => import("@/pages/DetailPage.vue"),
  props: true,
  meta: {
    title: "Property Details | Dwell In Door",
    description:
      "Explore detailed information about premium apartments, villas, plots, and luxury properties. View pricing, amenities, specifications, gallery, and location with Dwell In Door.",
    keywords:
      "property details, apartments for sale, luxury villas, plots, real estate, Bangalore properties, property amenities, Dwell In Door"
  }
},

  // {
  //   path: "/about-us",
  //   name: "About-Us",
  //   component: () => import('@/pages/About-Us.vue')

  // },
  {
  path: "/about-us",
  name: "About-Us",
  component: () => import("@/About-us/About.vue"),
  meta: {
    title: "About Us | Dwell In Door - Premium Real Estate Company",
    description:
      "Know more about Dwell In Door, a trusted real estate company offering premium apartments, villas, plots, and luxury homes. Discover our vision, mission, and commitment to helping you find your dream property.",
    keywords:
      "About Dwell In Door, Dwell In Door, real estate company, Bangalore real estate, premium properties, apartments, villas, plots, luxury homes, trusted property consultants"
  }
},

  {
  path: "/blogs",
  name: "Blogs",
  component: () => import("@/blog/BlogList.vue"),
  meta: {
    title: "Real Estate Blogs | Dwell In Door",
    description:
      "Read the latest real estate blogs, home buying tips, property investment guides, market trends, and expert advice from Dwell In Door.",
    keywords:
      "real estate blogs, home buying tips, property investment, real estate news, Bangalore real estate, property guides, Dwell In Door blog"
  }
},

 {
  path: "/blogdetailpage/:route",
  name: "BlogDetailPage",
  component: () => import("@/blog/BlogDetailPage.vue"),
  props: true,
  meta: {
    title: "Blog Details | Dwell In Door",
    description:
      "Read expert real estate articles, home buying tips, property investment guides, and the latest market trends from Dwell In Door.",
    keywords:
      "real estate blog, property articles, home buying guide, property investment, real estate tips, Bangalore real estate, Dwell In Door"
  }
},

{
  path: "/contact-us",
  name: "Contact-Us",
  component: () => import("@/pages/Contact-Us.vue"),
  meta: {
    title: "Contact Us | Dwell In Door - Get in Touch",
    description:
      "Contact Dwell In Door for property enquiries, site visits, investment opportunities, or any real estate assistance. Our team is ready to help you find your dream property.",
    keywords:
      "contact Dwell In Door, property enquiry, real estate contact, apartments, villas, plots, Bangalore real estate, customer support"
  }
},

  {
  path: "/gallery",
  name: "Gallery",
  component: () => import("@/pages/Gallery.vue"),
  meta: {
    title: "Property Gallery | Dwell In Door - Apartments, Villas & Interiors",
    description:
      "Explore the Dwell In Door gallery featuring premium apartments, luxury villas, modern interiors, exteriors, amenities, and residential projects.",
    keywords:
      "property gallery, apartment gallery, villa gallery, luxury homes, real estate gallery, interiors, exteriors, amenities, Bangalore properties, Dwell In Door"
  }
}

]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
  scrollBehavior() {
    return {
      top: 0,
      behavior: "smooth",
    };
  },
})

export default router
