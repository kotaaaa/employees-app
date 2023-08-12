<template>
  <div v-if="visible" class="modal">
    <div>
      <label>First Name: <input v-model="localEmployee.first_name" /></label>
      <label>Last Name: <input v-model="localEmployee.last_name" /></label>
      <label
        >Salary: <input v-model="localEmployee.salary" type="number"
      /></label>
      <button @click="save">Save</button>
      <button @click="close">Close</button>
    </div>
  </div>
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
      if (this.localEmployee.id) {
        await apiHelper.putData(
          `/api/employees/${this.localEmployee.id}`,
          JSON.stringify(this.localEmployee)
        );
      } else {
        await apiHelper.postData(
          "/api/employees",
          JSON.stringify(this.localEmployee)
        );
      }
      this.$emit("refresh");
      this.close();
    },
  },
};
</script>

<style>
/* style css */
</style>
