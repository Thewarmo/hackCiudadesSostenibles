<template>
  <nav class="navbar navbar-light bg-light p-2 bg-dark">
    <div class="container-fluid">
      <span v-on:click="irHome" class="navbar-brand mb-0 h1 text-white reciclapp">ReciclApp</span>
      <div class="btn-group me-2" role="group" aria-label="First group">
        <button v-on:click="irRegistro" type="button" class="btn btn-primary">
          Registrarse
        </button>
        <button v-on:click="irLogin" type="button" class="btn btn-primary ms-3">Ingresar</button>
      </div>
    </div>
  </nav>
</template>

<script>
//import { defineComponent } from '@vue/composition-api'

export default {
  name: "Encabezado",
  methods: {
    irRegistro: function () {
      this.$router.push({ name: "Registro" });
    },
    irLogin: function () {
      this.$router.push({ name: "Login" });
    },
    irHome: function () {
      this.$router.push({ name: "Home" });
    },
    
  },
};
</script>

<style scoped>
    .reciclapp{
        cursor: pointer;
    }
</style>
