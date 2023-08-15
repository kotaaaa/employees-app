<template>
  <tr v-if="visible" class="modal">
    <td><input v-model="localEmployee.first_name" /></td>
    <td><input v-model="localEmployee.last_name" /></td>
    <td><input v-model="localEmployee.salary" type="number" /></td>
    <td>
      <button @click="save" class="table-button">Save</button>
      <button @click="close" class="table-button">Close</button>
    </td>
  </tr>
</template>

<script>
import apiHelper from "../apiHelper.js";

export default {
  data() {
    return {
      localEmployee: {},
      visible: false,
    };
  },
  methods: {
    open() {
      this.visible = true;
    },
    close() {
      this.visible = false;
    },
    async save() {
      await apiHelper.postData(
        "/api/employees",
        JSON.stringify(this.localEmployee)
      );
      this.$emit("refresh");
      this.close();
    },
  },
};
</script>

<style>
/* style css */
</style>
