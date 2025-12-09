"""
Test script to verify Supabase PostgreSQL connection
Run this to test your database credentials
"""
import os
from dotenv import load_dotenv
import psycopg2
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Get credentials
host = os.getenv('DB_HOST', '')
port = os.getenv('DB_PORT', '6543')
database = os.getenv('DB_NAME', 'postgres')
user = os.getenv('DB_USER', '')
password = os.getenv('DB_PASSWORD', '')

print("=" * 60)
print("TESTING SUPABASE CONNECTION")
print("=" * 60)
print(f"Host: {host}")
print(f"Port: {port}")
print(f"Database: {database}")
print(f"User: {user}")
print(f"Password: {'*' * len(password) if password else 'NOT SET'}")
print("=" * 60)

try:
    # Try connection with current password
    print("\nAttempting connection...")
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
        sslmode='require',
        connect_timeout=10
    )
    
    print("✓ CONNECTION SUCCESSFUL!")
    cursor = conn.cursor()
    cursor.execute('SELECT version()')
    version = cursor.fetchone()[0]
    print(f"PostgreSQL Version: {version}")
    
    # Test if we can query
    cursor.execute("SELECT current_database(), current_user;")
    db_info = cursor.fetchone()
    print(f"Connected to database: {db_info[0]}")
    print(f"Connected as user: {db_info[1]}")
    
    conn.close()
    print("\n✓ Database connection is working correctly!")
    
except psycopg2.OperationalError as e:
    print(f"\n✗ CONNECTION FAILED!")
    print(f"Error: {str(e)}")
    print("\n" + "=" * 60)
    print("TROUBLESHOOTING:")
    print("=" * 60)
    print("1. Verify your password in Supabase Dashboard:")
    print("   - Go to: Project Settings → Database")
    print("   - Look for 'Connection string' or 'Database password'")
    print("   - Copy the password exactly as shown")
    print("\n2. For Supabase Pooler (port 6543):")
    print("   - Make sure you're using the pooler connection string")
    print("   - The password should match your database password")
    print("\n3. Update your .env file with the correct password:")
    print("   DB_PASSWORD=your_actual_password_here")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ UNEXPECTED ERROR: {str(e)}")
    print(f"Error Type: {type(e).__name__}")

