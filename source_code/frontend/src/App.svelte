<script>
    import Page1 from "../pages/Page1.svelte";
    import Page2 from "../pages/Page2.svelte";
    import { Router, Route } from "svelte-routing";
</script>

<Router>
    <Route path = "/" component = {Page1}/>
    <Route path = "/page2" component = {Page2}/>
</Router>