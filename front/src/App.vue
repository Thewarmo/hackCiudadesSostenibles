 <template>

   <!--
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>-->

  <encabezado />
   <!---<router-view
    v-on:completedLogIn="cambiarRol"
   >
   </router-view>-->
   <router-view
v-on:completedLogIn="cambiarRol"
v-on:completedSignUp="completedSignUp"
>
</router-view>
</template>


<script>
  import Encabezado from '@/components/Encabezado.vue'
  

  export default {
  name: 'App',
  data: function () {
    return {
      datos: {
        nombreUsuario: "",
        rol: "uno",
      },
    };
  },
  components: {
    Encabezado,  
  },methods: {
    cambiarRol: function(){
     
      //swal("hola")
      alert('holll')
    }
  },created: async function(){
    this.getData();
  },
}
</script>
