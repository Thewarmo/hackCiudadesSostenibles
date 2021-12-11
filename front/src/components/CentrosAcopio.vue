<template>
  <div class="m-3 border border-dark" style="height: 75vh">
    <div class="card-header text-center bg-secondary text-white w-100">
      Consulta los diferentes sitios de acopio de materiales reciclables
    </div>
    <form class="d-flex flex-column p-3 mx-5">
      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">
          Nombre del Centro
        </span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3 border border-1">
        <span class="input-group-text" style="width: 15em"> Zona </span>
        <div class="form-check form-check-inline ms-2 pt-1">
          <input
            class="form-check-input"
            type="checkbox"
            id="inlineCheckbox1"
            value="option1"
          />
          <label class="form-check-label" for="inlineCheckbox1">sur</label>
        </div>
        <div class="form-check form-check-inline pt-1">
          <input
            class="form-check-input"
            type="checkbox"
            id="inlineCheckbox2"
            value="option2"
          />
          <label class="form-check-label" for="inlineCheckbox2">norte</label>
        </div>
        <div class="form-check form-check-inline pt-1">
          <input
            class="form-check-input"
            type="checkbox"
            id="inlineCheckbox2"
            value="option2"
          />
          <label class="form-check-label" for="inlineCheckbox2">oriente</label>
        </div>
        <div class="form-check form-check-inline pt-1">
          <input
            class="form-check-input"
            type="checkbox"
            id="inlineCheckbox2"
            value="option2"
          />
          <label class="form-check-label" for="inlineCheckbox2"
            >occidente</label
          >
        </div>
      </div>
      <div class="d-grid gap-2 col-6 mx-auto mt-3">
        <button class="btn btn-primary" type="button">Buscar</button>
      </div>
    </form>
    <div class="p-3">
      <table class="table table-bordered">
        <thead>
          <tr class="table-secondary">
            <th>Nombre</th>
            <th>Zona</th>
            <th>Telefono de contacto</th>
            <th>Direcciòn</th>
            <th>Encargado</th>
          </tr>
        </thead>

        <tr>
          <td>Soleado</td>
          <td>Mayormente soleado</td>
          <td>Parcialmente nublado</td>
          <td>Call 123</td>
          <td>Juan Perez</td>
        </tr>
        <tr>
          <td>Soleado</td>
          <td>Mayormente soleado</td>
          <td>Parcialmente nublado</td>
          <td>Call 123</td>
          <td>Juan Perez</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "CentrosAcopio",
  components: {},
};
</script>