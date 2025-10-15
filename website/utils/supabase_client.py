import os
from supabase import create_client, Client
from functools import lru_cache

@lru_cache()
def get_supabase_client() -> Client:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    if not supabase_url:
        raise ValueError("SUPABASE_URL is not set.")
    if not supabase_key:
        raise ValueError("SUPABASE_SERVICE_ROLE_KEY is not set.")

    return create_client(supabase_url, supabase_key)
