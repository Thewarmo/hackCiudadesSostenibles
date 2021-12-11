<template>
  <!--<div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Hola to Your Vue.js App"/>
  </div> -->
  <div>
    <ul class="nav nav-tabs bg-dark bg-gradient" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button
          class="nav-link active"
          id="informacion-tab"
          data-bs-toggle="tab"
          data-bs-target="#informacion"
          type="button"
          role="tab"
          aria-controls="informacion"
          aria-selected="true"
        >
          INFORMACION
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="contacto-tab"
          data-bs-toggle="tab"
          data-bs-target="#contacto"
          type="button"
          role="tab"
          aria-controls="contacto"
          aria-selected="false"
        >
          CONTACTO
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="contact-tab"
          data-bs-toggle="tab"
          data-bs-target="#reciclar"
          type="button"
          role="tab"
          aria-controls="reciclar"
          aria-selected="false"
        >
          RECICLAR
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="contact-tab"
          data-bs-toggle="tab"
          data-bs-target="#centro_acopio"
          type="button"
          role="tab"
          aria-controls="centro_acopio"
          aria-selected="false"
        >
          CENTROS DE ACOPIO
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="contact-tab"
          data-bs-toggle="tab"
          data-bs-target="#aprovechamiento"
          type="button"
          role="tab"
          aria-controls="aprovechamiento"
          aria-selected="false"
        >
          APROVECHAMIENTO Y USO DE RESIDUOS
        </button>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <div
        class="tab-pane fade show active"
        id="informacion"
        role="tabpanel"
        aria-labelledby="informacion-tab"
      >
        <informacion />
      </div>
      <div
        class="tab-pane fade"
        id="contacto"
        role="tabpanel"
        aria-labelledby="contacto-tab"
      >
        <contacto />
      </div>
      <div
        class="tab-pane fade"
        id="reciclar"
        role="tabpanel"
        aria-labelledby="reciclar-tab"
      >
        <reciclar />
      </div>
      <div
        class="tab-pane fade"
        id="centro_acopio"
        role="tabpanel"
        aria-labelledby="centro_acopio-tab"
      >
        <centros-acopio />
      </div>
      <div
        class="tab-pane fade"
        id="aprovechamiento"
        role="tabpanel"
        aria-labelledby="aprovechamiento-tab"
      >
        <aprovechamiento />
      </div>
    </div>
  </div>

  <div
    class="card-footer position-absolute bottom-0 w-100 bg-secondary text-white"
  >
    Contacto
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Reciclar from "@/components/Reciclar.vue";
import CentrosAcopio from "@/components/CentrosAcopio.vue";
import Informacion from "@/components/Informacion.vue";
import Aprovechamiento from "@/components/Aprovechamiento.vue";
import Contacto from "@/components/Contacto.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
    Reciclar,
    CentrosAcopio,
    Informacion,
    Aprovechamiento,
    Contacto,
  },
};
</script>
<style >
</style>