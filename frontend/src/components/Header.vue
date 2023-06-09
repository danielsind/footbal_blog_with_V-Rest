<template>
    <nav id="my_nav_bar" class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#"><img src="../assets/images/pngwing.com.png" width="120" height="100" alt=""></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <router-link to="/" class="nav-link"><i class="fa fa-home" aria-hidden="true"></i>Home<span
                        class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/user_profile" class="nav-link"><i class="fas fa-user"></i>Profile</router-link>

                </li>
                <li class="nav-item">
                    <router-link to="/add_post" class="nav-link"><i class="fa fa-plus-circle"></i>Create Post</router-link>
                </li>
                <li class="nav-item" v-show="logged">
                    <router-link to="/login" class="nav-link"><i class="fa fa-plus-circle"></i>Login</router-link>
                </li>
                <li class="nav-item" v-show="logged">
                    <router-link to="/sign_up" class="nav-link"><i class="fa fa-plus-circle"></i>Sign Up</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/profile_update" class="nav-link"><i class="fa fa-plus-circle"></i>Profile Update</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/logout" class="nav-link"><i class="fa fa-power-off" aria-hidden="true"></i>Logout</router-link>
                </li>
                <li class="nav-item">
                    <div class="nav_dropdown">
                        <button class="btn btn-primary dropdown-toggle">Categories</button>
                        <div class="dropdown-content">
                          <a href="#leagues">Leagues</a>
                          <a href="#players">Players</a>
                          <a href="#highlights">Highlights</a>
                          <a href="#news">Latest News</a>
                          <a href="#videos">Videos</a>
                        </div>
                      </div>
                </li>
            </ul>
              <div v-show="login">
                <h5>Welcome</h5>
                <h5>{{ username }}!</h5>
              </div>
            <form class="form-inline my-2 my-lg-0" >
                <div class="searchBar">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"> 
                </div>
            </form>
        </div>
    </nav>


</template>


<script>
   export default{
    name:"HeaderBar",
    data(){
        return {
            username:"",
            logged: true,
            login: false
        }
    },
    mounted(){
        let result = localStorage.getItem("blogger");
        if(result){
            this.logged = false
            this.login = true
        }
        let username = localStorage.getItem("blogger");
        this.username = JSON.parse(username).username;
        
    }
   
   }
</script>

<style>
 @import "../assets/style.css"
</style>