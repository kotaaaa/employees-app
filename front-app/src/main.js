import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;
Vue.prototype.$apiEndpoint = "http://localhost:8000";

new Vue({
  render: (h) => h(App),
}).$mount("#app");
