<template>
  <div
    class="tab-pane fade show active border border-dark "
    style="height: 75vh"
    id="v-pills-Ingresar_Producto"
    role="tabpanel"
    aria-labelledby="v-pills-Ingresar_Producto-tab"
  >
    <div class="card-header text-center bg-secondary text-white w-100">
      Ingresa el producto que quieres entregar para reciclar
    </div>

    <form class="p-3">
      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em"
          >Nombre del producto</span
        >
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Peso</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Dirección</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Estado</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em"
          >url de la imagen del producto</span
        >
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="d-grid gap-2 col-6 mx-auto mt-3">
        <button class="btn btn-primary" type="button">Ingresar Producto</button>
      </div>
    </form>
  </div>
</template>
