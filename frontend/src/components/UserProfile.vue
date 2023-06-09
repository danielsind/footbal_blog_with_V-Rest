<template>
    <HeaderBar/>
    <div class="container mt-5">
        <div class="row" style="z-index: -1;">
            <!-- User details side -->
            <div class="col-md-4">
                <h1>Blogger Details</h1>
                <div class="text-center">
                    <img src="../assets/images/players/player-1.png" alt="User Photo" class="img-fluid rounded-circle" style="width: 200px;">
                </div>
                <h3 class="text-center mt-3">{{ username }}</h3>
                <p class="text-center">Number of Posts: 10</p>
            </div>

            <!-- Blogger's posts side -->
            <div class="col-md-8">
                <h2>Recent Posts</h2>
                <div class="row">
                    <div class="col-md-6">
                        <div class="card mb-3">
                            <img src="../assets/images/players/player-12.png" class="card-img-top" alt="Post Image">
                            <div class="card-body">
                                <h5 class="card-title">Post Title 1</h5>
                                <div class="d-flex justify-content-between">
                                    <small class="text-muted">Likes: 10</small>
                                    <small class="text-muted">Comments: 5</small>
                                </div>
                                <p class="card-text mt-2">Author: {{ username }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card mb-3">
                            <img src="../assets/images/players/player-7.png" class="card-img-top" alt="Post Image">
                            <div class="card-body">
                                <h5 class="card-title">Post Title 2</h5>
                                <div class="d-flex justify-content-between">
                                    <small class="text-muted">Likes: 15</small>
                                    <small class="text-muted">Comments: 3</small>
                                </div>
                                <p class="card-text mt-2">Author: {{ username }} </p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card mb-3">
                            <img src="../assets/images/players/player-12.png" class="card-img-top" alt="Post Image">
                            <div class="card-body">
                                <h5 class="card-title">Post Title 1</h5>
                                <div class="d-flex justify-content-between">
                                    <small class="text-muted">Likes: 10</small>
                                    <small class="text-muted">Comments: 5</small>
                                </div>
                                <p class="card-text mt-2">Author: {{ username }} </p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card mb-3">
                            <img src="../assets/images/players/player-12.png" class="card-img-top" alt="Post Image">
                            <div class="card-body">
                                <h5 class="card-title">Post Title 1</h5>
                                <div class="d-flex justify-content-between">
                                    <small class="text-muted">Likes: 10</small>
                                    <small class="text-muted">Comments: 5</small>
                                </div>
                                <p class="card-text mt-2">Author: {{ username }}</p>
                            </div>
                        </div>
                    </div>
                    <!-- Add more posts here in the same format -->
                </div>
            </div>
        </div>
    </div>

    <FooterBar/>
</template>

<script>
import HeaderBar from "./Header.vue"
import FooterBar from "./Footer.vue"
export default {
    name: "UserProfile",
    data(){
        return{
            username:"",
        }
    },
    components:{
      HeaderBar,
      FooterBar
  },
  mounted(){
        let username = localStorage.getItem("blogger");
        this.username = JSON.parse(username).username;
  },
  
}
</script>

<style>
 @import "../assets/style.css"
</style>