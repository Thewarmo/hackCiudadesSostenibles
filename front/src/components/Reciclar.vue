<template>
    <div class=" p-3 " >
        <div class="d-flex align-items-start ">
            <div class="nav flex-column nav-pills me-3 " id="v-pills-tab" role="tablist" aria-orientation="vertical">
                <button class="nav-link active border border-primary" id="v-pills-Ingresar_Producto-tab" data-bs-toggle="pill" data-bs-target="#v-pills-Ingresar_Producto" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">Ingresar Producto</button>
                <button class="nav-link border border-primary" id="v-pills-BuscaProducto-tab" data-bs-toggle="pill" data-bs-target="#v-pills-BuscaProducto" type="button" role="tab" aria-controls="v-pills-BuscaProducto" aria-selected="false">Buscar producto de segunda</button>
                <button class="nav-link border border-primary" id="v-pills-BuscaReciclador-tab" data-bs-toggle="pill" data-bs-target="#v-pills-BuscaReciclador" type="button" role="tab" aria-controls="v-pills-BuscaReciclador" aria-selected="false">Buscar Reciclador</button>
            </div>
            <div class="tab-content w-100" id="v-pills-tabContent">
                <ingresarProducto />
                <buscaProducto />
                <buscaReciclador />
            </div>
        </div>
    </div>
</template>




<script>
// @ is an alias to /src

import IngresarProducto from '@/components/IngresarProducto.vue'
import BuscaProducto from '@/components/BuscaProducto.vue'
import BuscaReciclador from '@/components/BuscaReciclador.vue'

export default {
  name: 'Reciclar',
  components: {
    IngresarProducto,
    BuscaProducto,
    BuscaReciclador
    
  }
}


</script>