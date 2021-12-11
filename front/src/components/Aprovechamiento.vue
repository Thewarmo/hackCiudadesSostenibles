<template>
    <div class=" p-3 " >
        <div class="d-flex align-items-start ">
            <div class="nav flex-column nav-pills me-3 " id="v-pills-tab" role="tablist" aria-orientation="vertical">
                <button class="nav-link active border border-primary" id="v-pills-Ingresar_Producto-tab" data-bs-toggle="pill" data-bs-target="#v-pills-Ingresar_Producto" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">Generalidades</button>
                <button class="nav-link border border-primary" id="v-pills-BuscaProducto-tab" data-bs-toggle="pill" data-bs-target="#v-pills-BuscaProducto" type="button" role="tab" aria-controls="v-pills-BuscaProducto" aria-selected="false">Tipos de reciclaje</button>
                <button class="nav-link border border-primary" id="v-pills-BuscaReciclador-tab" data-bs-toggle="pill" data-bs-target="#v-pills-BuscaReciclador" type="button" role="tab" aria-controls="v-pills-BuscaReciclador" aria-selected="false">Como separar mis residuos</button>
                <button class="nav-link border border-primary" id="v-pills-BuscaReciclador-tab" data-bs-toggle="pill" data-bs-target="#v-pills-BuscaReciclador" type="button" role="tab" aria-controls="v-pills-BuscaReciclador" aria-selected="false">Hazlo tu mismo DYI</button>
            </div>
            <div class="tab-content w-100" id="v-pills-tabContent">
                <generalidades/>
                <buscaProducto />
                <buscaReciclador />
            </div>
        </div>
    </div>
</template>

<script>
import Generalidades from './Generalidades.vue';
export default {
  name: "Aprovechamiento",
  components: {
      Generalidades
  },
};
</script>
    