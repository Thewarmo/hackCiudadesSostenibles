<template>
  <div
    class="
      position-absolute
      top-50
      start-50
      translate-middle
      border border-primary
    "
    style="width: 20em"
  >
    <div class="card-header text-center bg-dark text-white">Login</div>

    <form class="p-3" v-on:submit.prevent="LogInUser">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Username</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          v-model="user.username"
        />
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword1"
          v-model="user.password"
        />
      </div>
      <!--    <select
        class="form-select form-select-sm"
        aria-label=".form-select-sm example"
      >
        <option selected>Tipo de usuario</option>
        <option value="1">Usuario</option>
        <option value="2">Reciclador</option>
        <option value="3">Centro de acopio</option>
      </select> -->

      <button type="submit" class="btn btn-primary mt-4">Iniciar Sesión</button>
    </form>
  </div>
</template>


<script>

export default {
  name: "Loguear",
  components: {},
  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
   /* processLogInUser: function () {
      axios
        .post("https://mision-tic-bank-be.herokuapp.com/login/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedLogIn", dataLogIn);
        })
        .catch((error) => {
          if (error.response.status == "401")
            alert("ERROR 401: Credenciales Incorrectas.");
        });
    },*/
    LogInUser: function () {
      //alert("usuario", user.username + "password ", password)
     // swal("hola" , this.user.username)
      this.$emit('cambiarRol')
      //alert(this.user.username, " " , this.user.password)
      //alert(this.user.password)
    }

  },
};
</script>