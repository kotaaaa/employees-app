import Vue from "vue";

export default {
  async fetchData(url) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`);
    return response.json();
  },

  async postData(url, data) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: data,
    });
    return response.json();
  },

  async putData(url, data) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: data,
    });
    return response.json();
  },

  async deleteData(url) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "DELETE",
    });
    return response.json();
  },
};
