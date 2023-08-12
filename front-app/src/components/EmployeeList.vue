<template>
  <div>
    <table>
      <tr>
        <td>
          <h1>Employees</h1>
        </td>
        <td></td>
        <td></td>
        <td>
          <button @click="showAddModal">Add</button>
        </td>
      </tr>
      <tr>
        <th>First name</th>
        <th>Last name</th>
        <th>Salary</th>
        <th>Action</th>
      </tr>
      <tr v-for="employee in employees" :key="employee.id">
        <td>
          <input
            v-if="editingEmployeeId === employee.id"
            v-model="employee.first_name"
          />
          <span v-else>{{ employee.first_name }}</span>
        </td>
        <td>
          <input
            v-if="editingEmployeeId === employee.id"
            v-model="employee.last_name"
          />
          <span v-else>{{ employee.last_name }}</span>
        </td>
        <td>
          <input
            v-if="editingEmployeeId === employee.id"
            v-model.number="employee.salary"
            type="number"
          />
          <span v-else>${{ employee.salary | formatCurrency }}</span>
        </td>
        <td>
          <button v-if="editingEmployeeId === employee.id" @click="endEdit">
            Save
          </button>
          <button v-else @click="startEdit(employee.id)">Edit</button>
          <button @click="deleteEmployee(employee.id)">Delete</button>
        </td>
      </tr>
      <EmployeeModal
        ref="employeeModal"
        :employee="currentEmployee"
        @close="closeModal"
        @refresh="getEmployees"
      />
    </table>
  </div>
</template>

<script>
import EmployeeModal from "./EmployeeModal.vue";
import apiHelper from "../apiHelper.js";
import Vue from "vue";

Vue.filter("formatCurrency", function (value) {
  if (!value) return "";
  return value.toLocaleString();
});

export default {
  components: {
    EmployeeModal,
  },
  data() {
    return {
      employees: [],
      currentEmployee: null,
      editingEmployeeId: null,
    };
  },
  methods: {
    async getEmployees() {
      this.employees = await apiHelper.fetchData("/api/employees");
    },
    startEdit(employeeId) {
      this.$refs.employeeModal.close();
      this.editingEmployeeId = employeeId;
    },
    async endEdit() {
      const editedEmployee = this.employees.find(
        (emp) => emp.id === this.editingEmployeeId
      );

      try {
        await apiHelper.putData(
          `/api/employees/${this.editingEmployeeId}`,
          JSON.stringify(editedEmployee)
        );
        this.editingEmployeeId = null; // End of edit mode
        this.getEmployees(); // get latest data from API
      } catch (error) {
        console.error("Error updating employee:", error);
      }
    },
    showAddModal() {
      this.getEmployees(); // get latest data from API
      this.currentEmployee = null;
      this.editingEmployeeId = null; // End of edit mode
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

<style scoped>
table {
  width: 100%;
  table-layout: fixed;
}

table td {
  width: 25%;
  overflow: hidden;
}

table input {
  width: 100%;
  border: none;
  box-sizing: border-box;
}
</style>
