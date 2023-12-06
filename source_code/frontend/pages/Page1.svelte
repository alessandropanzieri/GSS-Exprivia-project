<script>
    import { navigate } from "svelte-routing";
    import Component from "../components/Component.svelte"

    function handleButtonClick() {
        navigate("/page2");
    }
</script>

<Component variable = "Page 1"/>
<button on:click={handleButtonClick}>Go To Page 2</button>

<style>
</style>