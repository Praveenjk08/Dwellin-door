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
// ✅ Add this block
router.afterEach((to) => {
  document.title = to.meta.title || "Dwell In Door";

  const updateMeta = (name, content) => {
    let tag = document.querySelector(`meta[name="${name}"]`);

    if (!tag) {
      tag = document.createElement("meta");
      tag.setAttribute("name", name);
      document.head.appendChild(tag);
    }

    tag.setAttribute("content", content || "");
  };

  updateMeta("description", to.meta.description);
  updateMeta("keywords", to.meta.keywords);
});
// ✅ End
app.use(resourcesPlugin)
app.use(VueAwesomePaginate);

app.component('Button', Button)
app.mount('#app')
