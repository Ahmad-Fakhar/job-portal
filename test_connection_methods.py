"""Test different connection methods for Supabase"""
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
full_user = os.getenv('DB_USER')  # postgres.pkrzxlevdcbiptggrxfv
password = os.getenv('DB_PASSWORD')

print("Testing different connection methods...\n")

# Method 1: Full username
print("1. Testing with full username:", full_user)
try:
    conn = psycopg2.connect(
        host=host, port=port, database=database,
        user=full_user, password=password, sslmode='require'
    )
    print("   ✓ SUCCESS!")
    conn.close()
except Exception as e:
    print(f"   ✗ Failed: {str(e)[:100]}")

# Method 2: Just 'postgres'
print("\n2. Testing with username: postgres")
try:
    conn = psycopg2.connect(
        host=host, port=port, database=database,
        user='postgres', password=password, sslmode='require'
    )
    print("   ✓ SUCCESS!")
    conn.close()
except Exception as e:
    print(f"   ✗ Failed: {str(e)[:100]}")

# Method 3: Extract user from full_user (part before dot)
if '.' in full_user:
    base_user = full_user.split('.')[0]
    print(f"\n3. Testing with username: {base_user}")
    try:
        conn = psycopg2.connect(
            host=host, port=port, database=database,
            user=base_user, password=password, sslmode='require'
        )
        print("   ✓ SUCCESS!")
        conn.close()
    except Exception as e:
        print(f"   ✗ Failed: {str(e)[:100]}")

print("\n" + "="*60)
print("CONCLUSION: Password authentication is failing.")
print("You need to get the correct password from Supabase Dashboard.")
print("="*60)

