<template>
    <body style="background-image: linear-gradient(to right, #3A1078,#3795BD);"> 
        <div class="reg_container">
          <div class="row">
            <div class="col-lg-10 col-xl-9 mx-auto">
              <div class="card flex-row my-5 border-0 shadow rounded-3 overflow-hidden">
                <div class="card-img-left d-none d-md-flex">
                  <!-- Background image for card set in CSS! -->
                </div>
                <div id="whole_form" class="card-body p-4 p-sm-5">
                  <h5 class="card-title text-center mb-5 fw-light fs-5" style="font-weight:bolder;">Login Here</h5>
                  <form>
                    <br><br><br>
                    <div class="form-floating mb-3">
                      <input v-model="username" type="text" class="form-control" id="floatingInputUsername" placeholder="myusername" required autofocus>
                      <label for="floatingInputUsername">Username</label>
                    </div>
                    <hr>
      
                    <div class="form-floating mb-3">
                      <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
                      <label for="floatingPassword">Password</label>
                    </div>
                    <br><br><br>
                    <div class="d-grid mb-2">
                      <button @click.prevent="Login" class="btn btn-lg btn-primary btn-login fw-bold text-uppercase" type="submit">Login</button>
                    </div>
      
                    <router-link to="/sign_up" class="d-block text-center mt-2 small" ><i class="fa fa-plus-circle"></i>Have an account? Sign Up Here</router-link>

      
                    <hr class="my-4">
      
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
    </body>
</template>

<script>
import axios from "axios";
export default {
    name:"LogIn",
    data(){
        return {
            username:"",
            password:"",
            
        }
    },
    methods:{
        async Login(){

          const blogger = {
          username: this.username,
          password: this.password
           };

            let result = await axios.get(
                `http://localhost:8000/users/?username=${this.username}&&password=${this.password}`
                )
            if(result.status==200 && result.data.length>0){

                localStorage.setItem("blogger", JSON.stringify(blogger));
                this.$router.push({name:"HomePage"})
            }
            
        }
    }

}
</script>

<style>
  @import "../assets/style.css"
</style>
