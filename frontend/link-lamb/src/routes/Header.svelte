<script>
       import Menu from "./Menu.svelte";
         let showMenu  = false;
         function toggleMenu() {
        showMenu = !showMenu;
    }

    let y;
    let showHeader = true;
     
  
</script>


{#if y < 50}
<header class="header-bar">

    <button class="header-bar-icon-background" on:click={toggleMenu} aria-label="menu_button">
       <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M5 7h14M5 12h14M5 17h14"/>
</svg>
</button>

     <div class="header-logo">
        <img src="/src/images/link-lamb-colorless1.png" alt="link lamb logo" width="100vw">
    </div>


</header>
{/if}


 {#if showMenu}
    <Menu />
    {/if}

<svelte:window bind:scrollY={y} />
