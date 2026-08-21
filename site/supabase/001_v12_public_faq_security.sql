begin;

create schema if not exists public_content;
create schema if not exists security;

create table if not exists public_content.faq (
  id uuid primary key default gen_random_uuid(),
  language_code text not null default 'it',
  category text not null default 'general',
  question text not null,
  answer text not null,
  keywords text[] not null default '{}',
  publication_status text not null default 'published',
  valid_from timestamptz default now(),
  valid_to timestamptz,
  sort_order integer not null default 100,
  updated_at timestamptz not null default now()
);

create table if not exists public_content.translations (
  id uuid primary key default gen_random_uuid(),
  content_key text not null,
  language_code text not null,
  value text not null,
  updated_at timestamptz not null default now(),
  unique(content_key, language_code)
);

create table if not exists security.visi_security_events (
  id uuid primary key default gen_random_uuid(),
  event_type text not null default 'SECURITY_SECRET_PROBING',
  session_id text,
  account_person_id uuid references core.persons(id) on delete set null,
  attempt_number smallint not null,
  page_path text,
  message_excerpt text,
  ip_address inet,
  user_agent text,
  risk_score numeric(5,2),
  status text not null default 'open',
  action_taken text,
  created_at timestamptz not null default now(),
  reviewed_at timestamptz,
  reviewed_by_person_id uuid references core.persons(id) on delete set null
);

create table if not exists security.visi_security_patterns (
  id uuid primary key default gen_random_uuid(),
  code text unique not null,
  category text not null,
  pattern_text text not null,
  severity smallint not null default 1,
  active boolean not null default true,
  approved_by_person_id uuid references core.persons(id) on delete set null,
  created_at timestamptz not null default now()
);

alter table public_content.faq enable row level security;
alter table public_content.translations enable row level security;
alter table security.visi_security_events enable row level security;
alter table security.visi_security_patterns enable row level security;

-- FAQ pubbliche: sola lettura anon/authenticated
drop policy if exists faq_public_read on public_content.faq;
create policy faq_public_read on public_content.faq
for select to anon, authenticated
using (publication_status='published' and (valid_from is null or valid_from<=now()) and (valid_to is null or valid_to>now()));

drop policy if exists translations_public_read on public_content.translations;
create policy translations_public_read on public_content.translations
for select to anon, authenticated
using (true);

insert into public_content.faq(language_code,category,question,answer,keywords,sort_order)
select 'it','general','Chi siete?',
'Vacanze Sicure è un ecosistema che aiuta Viaggiatori e Host a orientarsi tra annunci, strutture, informazioni, verifiche disponibili e assistenza. VìSì ti guida verso le informazioni pubbliche e l’iscrizione.',
array['chi siete','cosa fate','vacanze sicure'],10
where not exists(select 1 from public_content.faq where language_code='it' and question='Chi siete?');

insert into public_content.faq(language_code,category,question,answer,keywords,sort_order)
select 'it','account','Come posso iscrivermi?',
'Puoi iniziare dalla pagina Accesso/Registrazione. VìSì può aiutarti a scegliere il percorso per Viaggiatore, Host/Gestore o Professionista.',
array['iscrizione','registrazione','account'],20
where not exists(select 1 from public_content.faq where language_code='it' and question='Come posso iscrivermi?');

insert into public_content.faq(language_code,category,question,answer,keywords,sort_order)
select 'it','cin','Cos’è il CIN?',
'Il CIN è un dato importante da controllare. Vacanze Sicure distingue tra dato dichiarato, fonte consultata e risultato del controllo. Il CIN da solo non rappresenta una garanzia assoluta sull’affidabilità complessiva.',
array['cin','codice identificativo'],30
where not exists(select 1 from public_content.faq where language_code='it' and question='Cos’è il CIN?');

commit;