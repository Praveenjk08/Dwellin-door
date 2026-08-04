import './index.css'
import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'
import VueAwesomePaginate from "vue-awesome-paginate";
import "vue-awesome-paginate/dist/style.css";

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)

const updateMetaTag = (attribute, attributeKey, content) => {
  let tag = document.querySelector(`meta[${attribute}="${attributeKey}"]`);

  if (!tag) {
    tag = document.createElement('meta');
    tag.setAttribute(attribute, attributeKey);
    document.head.appendChild(tag);
  }

  tag.setAttribute('content', content || '');
};

router.afterEach((to) => {
  document.title = to.meta.title || 'Dwell In Door';

  const pageTitle = to.meta.title || 'Dwell In Door';
  const pageDescription = to.meta.description || 'Discover premium apartments, villas, plots, and luxury homes in Bangalore with Dwell In Door.';
  const pageKeywords = to.meta.keywords || 'Dwell In Door, real estate, apartments, villas, plots, Bangalore';
  const canonicalUrl = `${window.location.origin}${to.fullPath}`;

  updateMetaTag('name', 'description', pageDescription);
  updateMetaTag('name', 'keywords', pageKeywords);
  updateMetaTag('property', 'og:title', pageTitle);
  updateMetaTag('property', 'og:description', pageDescription);
  updateMetaTag('property', 'og:type', 'website');
  updateMetaTag('property', 'og:url', canonicalUrl);
  updateMetaTag('property', 'og:site_name', 'Dwell In Door');
  updateMetaTag('property', 'og:image', 'https://www.dwellindoor.com/files/logo-with-some-changes.png');
  updateMetaTag('name', 'twitter:card', 'summary_large_image');
  updateMetaTag('name', 'twitter:title', pageTitle);
  updateMetaTag('name', 'twitter:description', pageDescription);
  updateMetaTag('name', 'twitter:image', 'https://www.dwellindoor.com/files/logo-with-some-changes.png');
});

app.use(resourcesPlugin)
app.use(VueAwesomePaginate);

app.component('Button', Button)
app.mount('#app')
