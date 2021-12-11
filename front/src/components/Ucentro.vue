<template>
  <div
    class="tab-pane fade border border-dark"
    style="height: 75vh"
    id="v-pills-Ucentro"
    role="tabpanel"
    aria-labelledby="v-pills-Ucentro-tab"
  >
    <div
      class="tab-pane fade show active border border-dark"
      style="height: 75vh"
      id="v-pills-Ucentro"
      role="tabpanel"
      aria-labelledby="v-pills-Ucentro-tab"
    >
      <div class="card-header text-center bg-secondary text-white w-100">
        Registrate como centro de acopio
      </div>
      <form class="p-3">
        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em"
            >Persona a cargo</span
          >
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Direccion</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Telefono</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em"
            >Nombre de Centro</span
          >
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Password</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>
        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em"> Zona </span>
          <select
            class="form-select form-select-sm"
            aria-label=".form-select-sm example"
          >
            <option selected>Slecciona tu zona</option>
            <option value="1">sur</option>
            <option value="2">norte</option>
            <option value="3">oriente</option>
            <option value="3">occidente</option>
          </select>
        </div>

        <div class="d-grid gap-2 col-6 mx-auto mt-3">
          <button class="btn btn-primary" type="button">
            Registrarse
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Ucentro",
  components: {},
};
</script>
