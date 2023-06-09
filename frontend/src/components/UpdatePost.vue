<template>
    <HeaderBar />
    <h2>Football Blog Input Form</h2>
    <body> 
        <div class="row">
            <div class="col-md-3"></div>
            <div class="col-md-6">
                <div class="add_post_container" style="align-items:center;">
                    <form>
                        <div class="mb-3" >
                          <label for="category">Category:</label>
                          <input type="text" class="form-control" id="category" placeholder="Enter category">
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="postTitle">Post Title:</label>
                          <input type="text" class="form-control" id="postTitle" placeholder="Enter post title">
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="content">Content:</label>
                          <textarea class="form-control" id="content" rows="5" placeholder="Enter content"></textarea>
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="image">Image:</label>
                          <input type="file" class="form-control-file" id="image">
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="video">Video:</label>
                          <input type="text" class="form-control" id="video" placeholder="Enter video URL">
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="authorName">Author Name:</label>
                          <input type="text" class="form-control" id="authorName" placeholder="Enter author name">
                        </div>
                        <br>
                        <button type="submit" class="btn btn-primary">Submit</button>
                      </form>
                </div>
            </div>
            <div class="col-md-3"></div>
          </div>
    </body>
    <FooterBar />
</template>

<script>
import HeaderBar from "./Header.vue"
import FooterBar from "./Footer.vue"
export default{
    name:"UpdatePost",
    components:{
      HeaderBar,
      FooterBar
  },

}
</script>

<style>
  @import "../assets/style.css"
</style>