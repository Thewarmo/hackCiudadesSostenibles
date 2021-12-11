<template>
    <div class=" p-3 " >
        <div class="d-flex align-items-start ">
            <div class="nav flex-column nav-pills me-3 " id="v-pills-tab" role="tablist" aria-orientation="vertical">
                <button class="nav-link active border border-primary" id="v-pills-Ureciclador-tab" data-bs-toggle="pill" data-bs-target="#v-pills-Ureciclador" type="button" role="tab" aria-controls="v-pills-Ureciclador" aria-selected="true">Reciclador</button>
                <button class="nav-link border border-primary" id="v-pills-Uusuario-tab" data-bs-toggle="pill" data-bs-target="#v-pills-Uusuario" type="button" role="tab" aria-controls="v-pills-Uusuario" aria-selected="false">Usuario</button>
                <button class="nav-link border border-primary" id="v-pills-Ucentro-tab" data-bs-toggle="pill" data-bs-target="#v-pills-Ucentro" type="button" role="tab" aria-controls="v-pills-Ucentro" aria-selected="false">Centro de acopio</button>
            </div>
            <div class="tab-content w-100" id="v-pills-tabContent">
                <ureciclador />
                <uusuario />
                <ucentro />
            </div>
        </div>
    </div>
</template>


<script>
import Ucentro from '@/components/Ucentro.vue'
import Ureciclador from '@/components/Ureciclador.vue'
import Uusuario from '@/components/Uusuario.vue'



export default {
  name: 'Registro',
  components: {
    Ureciclador,
    Uusuario,
    Ucentro
    
  }
}
    Uusuario
</script>