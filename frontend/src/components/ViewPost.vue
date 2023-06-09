<template>
    <HeaderBar />
    <!-- ------------
        header part html
    -------------------- -->
    <div class="container">
      <div class="post-container">
        <h1 class="post-title">Post Title</h1>
        <div class="post-details">
          <p class="blogger-name">Blogger Name</p>
          <img src="images/La Liga Dream League Soccer Kit (DLS Kits) by Kuchalana_com.png" alt="Post Image" width="400">
          <p class="post-content">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Inventore sed autem sint. Laboriosam quos ducimus explicabo ab, cupiditate voluptate repudiandae molestias ut at cum quasi incidunt tempore voluptatem sunt nihil!</p>
        </div>
        <div class="likes-comments">
          <p>Likes: <span class="likes-count">100</span></p>
          <p>Comments: <span class="comments-count">50</span></p>
        </div>
      </div>
    </div>
    <br>
    <FooterBar />
</template>

<script>
import HeaderBar from "./Header.vue"
import FooterBar from "./Footer.vue"
export default {
  name: 'ViewPost',
    components:{
      HeaderBar,
      FooterBar
  },
  
  }
</script>

<style>
  @import "../assets/style.css"
</style>