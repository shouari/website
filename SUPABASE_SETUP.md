# Supabase Setup for Process Mapper

## Database Table: `mapper_users`

Create this table in Supabase to store user registrations and tokens:

```sql
CREATE TABLE mapper_users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    access_token UUID NOT NULL UNIQUE,
    token_used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for fast token lookups
CREATE INDEX idx_mapper_users_token ON mapper_users(access_token) WHERE NOT token_used;
```

## Database Table: `contact_messages`

Create this table to store contact form submissions:

```sql
CREATE TABLE contact_messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status TEXT DEFAULT 'new'
);
```

## Authentication Flow

### 1. Form Submission
- User fills form on `/mapper` (name + email)
- App generates UUID token
- Saves to `mapper_users` table with `token_used = FALSE`
- Returns success (email handled externally)

### 2. External Email (n8n + Brevo)
- n8n webhook receives user data + token
- Sends email via Brevo with magic link:
  ```
  http://localhost:3000/mapper?token={access_token}
  ```

### 3. Magic Link Click
- User clicks link → redirects to `/mapper?token=xyz`
- `on_load` handler validates token
- If valid and not used:
  - Marks `token_used = TRUE`
  - Grants access to mapper
  - Populates user data in state

## Testing

### Test Link (Console)
When form is submitted, check the backend console for:
```
🔗 Test Magic Link: http://localhost:3000/mapper?token=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Manual Test
1. Submit form on `/mapper`
2. Copy token from console
3. Open: `http://localhost:3000/mapper?token=<copied-token>`
4. Should grant access to Steps 1-4

## Environment Variables
Make sure these are set (`.env`):
```env
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```
