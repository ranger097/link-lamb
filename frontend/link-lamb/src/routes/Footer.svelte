<script>
    let scrollY = 0;
    let prevScrollY = 0;
    let scrollingUp = true;
    function handleScroll() {
      scrollingUp = window.scrollY < prevScrollY;
      prevScrollY = window.scrollY;
    }
</script>

{#if scrollingUp}
<footer class="background-footer">
<footer class="footer-bar">

  <div class="footer-label-and-icon">
    <div class="footer-bar-icon-background footer-bar-icons-anime-1">
       <svg class="w-6 h-6 text-800 dark:text-white footer-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
  </svg>
    </div>
    <div>
      
    </div>
  </div>

  <div class="footer-label-and-icon">
    <div class="footer-bar-icon-background footer-bar-icons-anime-2">
        <svg class="w-6 h-6 text-800 dark:text-white footer-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 8v8m0-8a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 8a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm8-8a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 0a4 4 0 0 1-4 4h-1a3 3 0 0 0-3 3"/>
</svg>
    </div>
    
    </div>

    <div class="footer-label-and-icon">
    <div class="footer-bar-icon-background footer-bar-icons-anime-3">
        <svg class="w-6 h-6 text-800 dark:text-white footer-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
</svg>
    </div>
    
    </div>

    <div class="footer-label-and-icon">
    <div class="footer-bar-icon-background footer-bar-icons-anime-4">
      <svg class="w-6 h-6 text-800 dark:text-white footer-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path fill-rule="evenodd" d="M3 6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-6.616l-2.88 2.592C8.537 20.461 7 19.776 7 18.477V17H5a2 2 0 0 1-2-2V6Zm4 2a1 1 0 0 0 0 2h5a1 1 0 1 0 0-2H7Zm8 0a1 1 0 1 0 0 2h2a1 1 0 1 0 0-2h-2Zm-8 3a1 1 0 1 0 0 2h2a1 1 0 1 0 0-2H7Zm5 0a1 1 0 1 0 0 2h5a1 1 0 1 0 0-2h-5Z" clip-rule="evenodd"/>
</svg>
    </div>
    
    </div>

    <div class="footer-label-and-icon">
    <div class="footer-bar-icon-background footer-bar-icons-anime-5">
        <svg class="w-6 h-6 text-800 dark:text-white footer-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path d="M17.133 12.632v-1.8a5.406 5.406 0 0 0-4.154-5.262.955.955 0 0 0 .021-.106V3.1a1 1 0 0 0-2 0v2.364a.955.955 0 0 0 .021.106 5.406 5.406 0 0 0-4.154 5.262v1.8C6.867 15.018 5 15.614 5 16.807 5 17.4 5 18 5.538 18h12.924C19 18 19 17.4 19 16.807c0-1.193-1.867-1.789-1.867-4.175ZM8.823 19a3.453 3.453 0 0 0 6.354 0H8.823Z"/>
</svg>
    </div>
    
    </div>
    
</footer>
</footer>
{/if}

<svelte:window onscroll={handleScroll} bind:scrollY/>