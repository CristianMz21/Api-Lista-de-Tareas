import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get Supabase credentials from environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: SUPABASE_URL or SUPABASE_KEY not found in environment variables")
    exit(1)

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    
    # Test connection by fetching information schema
    response = supabase.rpc('get_all_tables', {}).execute()
    
    # Print the response
    print("Connection successful!")
    print("Tables in database:", response.data if hasattr(response, 'data') else response)
    
except Exception as e:
    # Try alternative approach if first one fails
    try:
        supabase: Client = create_client(url, key)
        
        # Query information_schema for tables
        response = supabase.table("information_schema.tables").select("table_name").eq("table_schema", "public").execute()
        
        print("Connection successful!")
        print("Tables in database:", [table["table_name"] for table in response.data] if hasattr(response, 'data') else response)
    
    except Exception as e2:
        print(f"Error connecting to Supabase: {e}")
        print(f"Second attempt error: {e2}")
        
        # Try a simple connection test without specific table
        try:
            supabase: Client = create_client(url, key)
            print("Basic connection successful!")
        except Exception as e3:
            print(f"Basic connection failed: {e3}") 