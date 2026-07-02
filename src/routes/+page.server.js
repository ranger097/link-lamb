import { supabase } from "$lib/supabaseClient";

  export async function load() {
    const { data } = await supabase.from("repos").select();
    return {
      repos: data ?? [],
    };
  }
