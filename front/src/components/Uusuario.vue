<template>
  <div
    class="tab-pane fade border border-dark"
    style="height: 75vh"
    id="v-pills-Uusuario"
    role="tabpanel"
    aria-labelledby="v-pills-Uusuario-tab"
  >
    <div
      class="tab-pane fade show active"
      id="v-pills-home"
      role="tabpanel"
      aria-labelledby="v-pills-Uusuario-tab"
    >
      <div class="card-header text-center bg-secondary text-white w-100">
        Registrate como usuario
      </div>
      <form class="p-3">
        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Nombre</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em"
            >Identificacion</span
          >
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Telefono</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Username</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="input-group mt-3">
          <span class="input-group-text" style="width: 15em">Password</span>
          <input type="text" aria-label="First name" class="form-control" />
        </div>

        <div class="d-grid gap-2 col-6 mx-auto mt-3">
          <button class="btn btn-primary" type="button">Registrarse</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Uusuario",
  components: {},
};
</script>
