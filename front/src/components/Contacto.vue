<template>
  <div class="m-3 border border-dark" style="height: 75vh">
    <div class="card-header text-center bg-secondary text-white w-100">
      Revisa tus solicitudes y sus estados
    </div>

    <div class="p-3">
      <table class="table table-bordered">
        <thead>
          <tr class="table-secondary">
            <th>Username</th>
            <th>Estado</th>
            <th>Fecha</th>
            <th>Centro de acopio</th>
            <th>Cambiar estado</th>
            <th>Guardar estado</th>
          </tr>
        </thead>

        <tr>
          <td>Soleado</td>
          <td>Mayormente soleado</td>
          <td>Parcialmente nublado</td>
          <td>
            <select
              class="form-select form-select-sm"
              aria-label=".form-select-sm example"
            >
              <option selected>Seleccione el centro</option>
              <option value="1">centro 1</option>
              <option value="2">centro 2</option>
            </select>
          </td>
          <td>
            <select
              class="form-select form-select-sm"
              aria-label=".form-select-sm example"
            >
              <option selected>Seleccione el estado</option>
              <option value="1">Abierto</option>
              <option value="2">Cerrado</option>
            </select>
          </td>
          <td>
            <button type="button" class="btn btn-secondary btn-sm">
              Guardar
            </button>
          </td>
        </tr>
        <tr>
          <td>Soleado</td>
          <td>Mayormente soleado</td>
          <td>Parcialmente nublado</td>
          <td>
            <select
              class="form-select form-select-sm"
              aria-label=".form-select-sm example"
            >
              <option selected>Seleccione el centro</option>
              <option value="1">centro 1</option>
              <option value="2">centro 2</option>
            </select>
          </td>
          <td>
            <select
              class="form-select form-select-sm"
              aria-label=".form-select-sm example"
            >
              <option selected>Seleccione el estado</option>
              <option value="1">Abierto</option>
              <option value="2">Cerrado</option>
            </select>
          </td>
          <td>
            <button type="button" class="btn btn-secondary btn-sm">
              Guardar
            </button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>