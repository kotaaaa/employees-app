import Vue from "vue";

export default {
  /**
   * Retrieve employees data
   * @param {string} url
   * @returns all employees data
   */
  async fetchData(url) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`);
    return response.json();
  },

  /**
   * Create new employee's record
   * @param {string} url
   * @param {string} data
   * @returns created employee's object
   */
  async postData(url, data) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: data,
    });
    return response.json();
  },

  /**
   * Update specific employee's data
   * @param {string} url
   * @param {string} data
   * @returns updated employee's record
   */
  async putData(url, data) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: data,
    });
    return response.json();
  },

  /**
   * Delete specific employee's record
   * @param {*} url
   * @returns action status
   */
  async deleteData(url) {
    const response = await fetch(`${Vue.prototype.$apiEndpoint}${url}`, {
      method: "DELETE",
    });
    return response.json();
  },
};
