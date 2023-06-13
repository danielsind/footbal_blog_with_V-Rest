<template>
    <HeaderBar />
    <h2>Football Blog Input Form</h2>
    <body> 
        <div class="row">
            <div class="col-md-2"></div>
            <div class="col-md-8">
                <div class="add_post_container" style="align-items:center;">
                    <form>
                        <div class="mb-3" style="z-index:1;">
                          <label class="label" for="category">Category</label>
                          <select v-model="post.category" class="form-select" aria-label="Default select example">
                            <option selected>Choose the category for content</option>
                            <option value="1">Leagues</option>
                            <option value="2">Players</option>
                            <option value="3">Highlights</option>
                            <option value="3">News</option>
                            <option value="3">Videos</option>
                          </select>
                          </div>
                        <div class="form-group">
                          <label for="postTitle">Post Title</label>
                          <input v-model="post.post_title" type="text" class="form-control" id="postTitle" placeholder="Enter post title">
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="content">Content</label>
                          <div style="height: 400px;">
                            <QuillEditor v-model="post.content" theme="snow" toolbar="full"/>
                          </div>
                        </div>
                        <br><br><br><br>
                        <!-- <div class="form-group">
                          <label for="video">Image</label>

                          <input v-on="image" type="file" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload" />
                          
                        </div> -->
                        <br>
                        <div class="form-group">
                          <label for="basic-url" class="form-label">Video</label>
                          <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
                            <input
                              v-model="post.video"
                              type="text"
                              class="form-control"
                              id="basic-url1"
                              aria-describedby="basic-addon3"
                            />
                          </div>
                        </div>
                        <br>
                        <div class="form-group">
                          <label for="authorName">Author Name</label>
                          <input v-model="post.author" type="text" class="form-control" id="authorName" placeholder="Enter author name">
                        </div>
                        <br>
                        <button @click.prevent="addPost" type="submit" class="btn btn-primary">Submit</button>
                      </form>
                </div>
            </div>
            <div class="col-md-2"></div>
          </div>
    </body>
    <FooterBar />
</template>

<script>
import axios from "axios";
import HeaderBar from "./Header.vue";
import FooterBar from "./Footer.vue";
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';


export default{
    name:"AddPost",
    components:{
    HeaderBar,
    FooterBar,
    QuillEditor
    
},
data(){
  return {
    post:{
      category:"",
      post_title:"",
      content:"",
      video:"",
      author:""
    }
    
  }
},
methods:{
      async addPost(){
        
      let result = await axios.post( "http://localhost:3000/post",
        {
          
          category:this.post.category,
          post_title:this.post.post_title,
          content:this.post.content,
          video:this.post.video,
          author:this.post.author
        }
      );
        if(result.status==201) {

            console.warn(result.data)
            alert("Post Successful")
            
            localStorage.setItem("post",JSON.stringify(result.data))
            
            this.$router.push({name:"UserProfile"})

            }

  }
}


}
</script>

<style>
  @import "../assets/style.css"
</style>