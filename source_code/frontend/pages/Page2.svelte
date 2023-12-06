<script>
    import { navigate } from "svelte-routing";
    import Component from "../components/Component.svelte"

    function handleButtonClick() {
        navigate("/");
    }

    let responseData = "";

    async function fetchData() {
        try {
            const response = await fetch("http://localhost:5000/");
            const data = await response.json();
            responseData = data.message;
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    }
</script>

<Component variable = "Page 2"/>
<button on:click = {handleButtonClick}>Go To Page 1</button>

<button on:click = {fetchData}>Fetch Data</button>
<h1>{responseData}</h1>

<style>
</style>