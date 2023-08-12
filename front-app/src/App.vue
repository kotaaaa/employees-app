<template>
  <div id="app">
    <EmployeeList />
  </div>
</template>

<script>
import EmployeeList from "./components/EmployeeList.vue";
export default {
  name: "App",
  components: {
    EmployeeList,
  },
};
</script>

<style src="./assets/style.css"></style>
