import HomePage from "./components/HomePage.vue";
import SignUp from "./components/SignUp.vue";
import LogIn from "./components/LogIn.vue";
import AddPost from "./components/AddPost.vue";
import UpdatePost from "./components/UpdatePost.vue";
import LogOut from "./components/LogOut.vue";
import UserProfile from "./components/UserProfile.vue";
import ViewPost from "./components/ViewPost.vue";
import ProfileUpdate from "./components/ProfileUpdate.vue"



import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        name: "HomePage",
        component: HomePage,
        path:"/"
    },
    {
        name: "SignUp",
        component: SignUp,
        path:"/sign_up"
    },
    {
        name: "LogIn",
        component: LogIn,
        path:"/login"
    },
    {
        name: "AddPost",
        component: AddPost,
        path:"/add_post"
    },
    {
        name: "Update",
        component: UpdatePost,
        path:"/update_post"
    },
    {
        name: "LogOut",
        component: LogOut,
        path:"/logout"
    },
    {
        name: "UserProfile",
        component: UserProfile,
        path:"/user_profile"
    },
    {
        name: "ViewPost",
        component: ViewPost,
        path:"/view_post"
    },
    {
        name: "ProfileUpdate",
        component: ProfileUpdate,
        path:"/profile_update"
    },
   
];

const router =  createRouter({
    history: createWebHistory(),
    routes
});

export default router;