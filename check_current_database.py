"""Check what data is currently in the database"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
django.setup()

from django.conf import settings
from django.db import connection

print("=" * 60)
print("CURRENT DATABASE STATUS")
print("=" * 60)

db_config = settings.DATABASES['default']
print(f"\nDatabase Engine: {db_config['ENGINE']}")
print(f"Database Name: {db_config.get('NAME', 'N/A')}")

if 'sqlite3' in db_config['ENGINE']:
    print(f"\n⚠️  WARNING: Using SQLite (local file)")
    print(f"   Data is stored locally, NOT in Supabase")
    
    # Check if file exists and get size
    db_file = db_config['NAME']
    if os.path.exists(db_file):
        size = os.path.getsize(db_file)
        print(f"   Database file: {db_file}")
        print(f"   File size: {size:,} bytes ({size/1024:.2f} KB)")
        
        # Try to get table info
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
                tables = cursor.fetchall()
                if tables:
                    print(f"\n   Tables in database ({len(tables)}):")
                    for table in tables:
                        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
                        count = cursor.fetchone()[0]
                        print(f"     - {table[0]}: {count} records")
        except Exception as e:
            print(f"   Could not read tables: {e}")
else:
    print(f"\n✓ Using PostgreSQL")
    print(f"   Host: {db_config.get('HOST', 'N/A')}")
    print(f"   Port: {db_config.get('PORT', 'N/A')}")
    print(f"   User: {db_config.get('USER', 'N/A')}")
    
    # Test connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), version()")
            db_name, version = cursor.fetchone()
            print(f"\n✓ Connected to: {db_name}")
            print(f"  PostgreSQL version: {version[:50]}...")
    except Exception as e:
        print(f"\n✗ Connection failed: {e}")

print("\n" + "=" * 60)

