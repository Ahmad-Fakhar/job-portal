# How to Connect Django to Supabase PostgreSQL

## Current Issue
Your Django project is currently using **SQLite** (local file database) instead of **Supabase PostgreSQL**.

## Steps to Fix

### 1. Get Your Supabase Database Password

**Option A: From Supabase Dashboard**
1. Go to https://supabase.com/dashboard
2. Select your project
3. Go to **Settings** → **Database**
4. Scroll down to **Connection string** section
5. Look for **Connection pooling** tab
6. You'll see a connection string like:
   ```
   postgresql://postgres.pkrzxlevdcbiptggrxfv:[YOUR-PASSWORD]@aws-1-us-east-1.pooler.supabase.com:6543/postgres?pgbouncer=true
   ```
7. Copy the password from between `:` and `@` in the connection string

**Option B: From Connection String**
If you have the full connection string, the format is:
```
postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE
```
Extract the PASSWORD part.

### 2. Update Your .env File

Once you have the correct password, update your `.env` file:

```env
USE_POSTGRES=True
DB_PASSWORD=your_actual_password_here
```

### 3. Test the Connection

Run the test script:
```bash
python test_db_connection.py
```

### 4. Run Migrations

Once connection works:
```bash
python manage.py migrate
```

### 5. Verify Data is in Supabase

1. Go to Supabase Dashboard → Table Editor
2. You should see your Django tables (accounts_user, jobs_job, etc.)
3. Create a test record in Django and verify it appears in Supabase

## Current Status
- ❌ Database: SQLite (local file)
- ❌ Supabase: Not connected (password authentication failed)
- ✅ Server: Running on http://localhost:8000

## After Fixing
- ✅ Database: Supabase PostgreSQL
- ✅ All data will be stored in Supabase cloud database
- ✅ Accessible from anywhere via Supabase dashboard

