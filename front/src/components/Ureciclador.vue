<template>
   <div
    class="tab-pane fade show active border border-dark "
    style="height: 75vh"
    id="v-pills-Ureciclador"
    role="tabpanel"
    aria-labelledby="v-pills-Ureciclador-tab"
  >
    <div class="card-header text-center bg-secondary text-white w-100">
      Registrate como reciclador
    </div>

    <form class="p-3">
      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em"
          >Nombre</span
        >
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Correo</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Telefono</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" style="width: 15em">Password</span>
        <input type="text" aria-label="First name" class="form-control" />
      </div>

      <div class="input-group mt-3">
                <span class="input-group-text" style="width: 15em">
                    Zona
                </span>
                <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                    <option selected>Slecciona tu zona</option>
                    <option value="1">sur</option>
                    <option value="2">norte</option>
                    <option value="3">oriente</option>
                    <option value="3">occidente</option>
                </select>
                
            </div>
<div class="input-group mt-3 border border-1">
                <span class="input-group-text" style="width: 15em">
                    Servicios
                </span>
                <div class="form-check form-check-inline ms-2 pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
                    <label class="form-check-label" for="inlineCheckbox1">Vidrio</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Papel</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Plastico</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Aluminio</label>
                </div>
            </div>
            
      <div class="d-grid gap-2 col-6 mx-auto mt-3">
        <button class="btn btn-primary" type="button">Registrarse</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Ureciclador",
  components: {},
};
</script>
