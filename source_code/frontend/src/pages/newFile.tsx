import Layout from "@layouts/Layout.astro";
import Header from "@components/Header.astro";
import Footer from "@components/Footer.astro";

<Fragment>
<Layout>
<Header></Header>
<div>
<h1>cao</h1>
</div>
<Footer></Footer>
</Layout>

<style>{`
    div {
        position:absolute;
        top: 50px;
        left:0px;
        right:0px;
        bottom:0px;
        overflow-y: scroll;        
    }
    ​
    div::-webkit-scrollbar {
        width: 10px;
    }

    div::-webkit-scrollbar-track {
        background: rgb(241, 241, 241);
    }

    div::-webkit-scrollbar-thumb {
        background: rgb(136, 136, 136);
    }

    div::-webkit-scrollbar-thumb:hover {
        background: rgb(85, 85, 85);
    }
`}</style>
</Fragment>;
