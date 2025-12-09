"""
Helper script to update Supabase password in .env file
Usage: python update_supabase_password.py YOUR_PASSWORD
"""
import sys
import os
from pathlib import Path

def update_password(new_password):
    """Update DB_PASSWORD in .env file"""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("❌ .env file not found!")
        return False
    
    # Read current .env
    with open(env_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Update password line
    updated = False
    new_lines = []
    for line in lines:
        if line.startswith('DB_PASSWORD='):
            new_lines.append(f'DB_PASSWORD={new_password}\n')
            updated = True
        else:
            new_lines.append(line)
    
    if not updated:
        # Add password line if it doesn't exist
        new_lines.append(f'DB_PASSWORD={new_password}\n')
    
    # Write back
    with open(env_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    # Also ensure USE_POSTGRES is True
    env_content = ''.join(new_lines)
    if 'USE_POSTGRES=True' not in env_content:
        env_content = env_content.replace('USE_POSTGRES=False', 'USE_POSTGRES=True')
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
    
    print("✓ Password updated in .env file")
    print("✓ USE_POSTGRES set to True")
    return True

def parse_connection_string(conn_string):
    """Parse Supabase connection string to extract password"""
    # Format: postgresql://user:password@host:port/database
    try:
        if '://' in conn_string:
            parts = conn_string.split('://')[1]
            if '@' in parts:
                user_pass = parts.split('@')[0]
                if ':' in user_pass:
                    password = user_pass.split(':', 1)[1]
                    return password
    except:
        pass
    return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("=" * 60)
        print("UPDATE SUPABASE PASSWORD")
        print("=" * 60)
        print("\nUsage:")
        print("  python update_supabase_password.py YOUR_PASSWORD")
        print("\nOr provide full connection string:")
        print("  python update_supabase_password.py 'postgresql://user:pass@host:port/db'")
        print("\n" + "=" * 60)
        sys.exit(1)
    
    input_value = sys.argv[1]
    
    # Try to parse as connection string first
    password = parse_connection_string(input_value)
    if not password:
        password = input_value
    
    if update_password(password):
        print("\n✓ Now test the connection:")
        print("  python test_db_connection.py")
        print("\n✓ Then run migrations:")
        print("  python manage.py migrate")

