<template>
  <tr v-if="visible" class="modal">
    <td><input v-model="localEmployee.first_name" /></td>
    <td><input v-model="localEmployee.last_name" /></td>
    <td><input v-model="localEmployee.salary" type="number" /></td>
    <td>
      <button @click="save">Save</button>
      <button @click="close">Close</button>
    </td>
  </tr>
</template>

<script>
import apiHelper from "../apiHelper.js";

export default {
  props: {
    employee: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      localEmployee: {},
      visible: false,
    };
  },
  watch: {
    employee: {
      handler(value) {
        this.localEmployee = { ...value };
      },
      immediate: true,
    },
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
