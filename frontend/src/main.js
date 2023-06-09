import { createApp } from 'vue';
import App from './App.vue';
import router from "./routers";
import 'bootstrap/dist/css/bootstrap.css';
import vueCountryRegionSelect from 'vue3-country-region-select'




createApp(App).use(router).use(vueCountryRegionSelect).mount('#app');

