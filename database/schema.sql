create table if not exists public.reports (
    id bigint generated always as identity primary key,
    created_at timestamptz not null default now(),
    company_name text not null,
    status text not null check (status in ('success', 'failed')),
    risk_score integer,
    report_filename text,
    error_message text,
    processing_seconds numeric
);

alter table public.reports enable row level security;