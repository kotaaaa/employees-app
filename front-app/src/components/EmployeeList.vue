<template>
  <div>
    <button @click="showAddModal">Add</button>
    <table>
      <tr>
        <th>Last name</th>
        <th>First name</th>
        <th>Salary</th>
        <th>Action</th>
      </tr>
      <tr v-for="employee in employees" :key="employee.id">
        <td>{{ employee.first_name }}</td>
        <td>{{ employee.last_name }}</td>
        <td>{{ employee.salary }}</td>
        <td>
          <button @click="showEditModal(employee)">Edit</button>
          <button @click="deleteEmployee(employee.id)">Delete</button>
        </td>
      </tr>
    </table>

    <EmployeeModal
      ref="employeeModal"
      :employee="currentEmployee"
      @close="closeModal"
      @refresh="getEmployees"
    />
  </div>
</template>

<script>
import EmployeeModal from "./EmployeeModal.vue";
import apiHelper from "../apiHelper.js";

export default {
  components: {
    EmployeeModal,
  },
  data() {
    return {
      employees: [],
      currentEmployee: null,
    };
  },
  methods: {
    async getEmployees() {
      this.employees = await apiHelper.fetchData("/api/employees");
    },
    showAddModal() {
      this.currentEmployee = null;
      this.$refs.employeeModal.open();
    },
    showEditModal(employee) {
      this.currentEmployee = employee;
      this.$refs.employeeModal.open();
    },
    closeModal() {
      this.$refs.employeeModal.close();
    },
    async deleteEmployee(employeeId) {
      var response = await apiHelper.deleteData(`/api/employees/${employeeId}`);
      if (response.status) {
        this.getEmployees(); // get latest data if success
      } else {
        console.error("API request failed:", response.status);
      }
    },
  },
  mounted() {
    this.getEmployees();
  },
};
</script>
