import { createClient } from "@supabase/supabase-js";
import { getSupabaseUrl, getSupabaseAnonKey, getSupabaseServiceRoleKey } from "./env";

// Server-side client with service role key (never expose to browser)
export function createServiceRoleClient() {
  return createClient(getSupabaseUrl(), getSupabaseServiceRoleKey(), {
    auth: { autoRefreshToken: false, persistSession: false },
  });
}

// Browser-safe client with anon key
export function createBrowserClient() {
  return createClient(getSupabaseUrl(), getSupabaseAnonKey());
}
