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
                  <div id="logout_page">
                    <br><br><br><br>
                    <h1>Are you sure you want to Logout?</h1>
                  </div>
                  <br><br><br>
                  <div class="d-grid mb-2">
                    <button @click="Logout" class="btn btn-lg btn-primary btn-login fw-bold text-uppercase" type="submit">Yes</button>
                  </div>
                  <div class="d-grid mb-2">
                    <router-link to="/" class="btn btn-lg btn-danger btn-login fw-bold text-uppercase" type="submit">No</router-link>
                  </div>
                  <br><br><br><br><br><br>
                </div>
              </div>
            </div>
          </div>
        </div>
    </body>
</template>

<script>
export default {
    name:"LogOut",

    methods:{
        Logout(){
            localStorage.clear();
            this.$router.push({name:"LogIn"});
        }
    }
}

</script>


<style>
 @import "../assets/style.css"
</style>