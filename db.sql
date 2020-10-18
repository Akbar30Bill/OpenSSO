CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
create table opensso_user(
  user_uuid uuid primary key not null default uuid_generate_v4(),
  username text,
  hashed_password text,
  create_timestamp timestamp default now(),
  delete_timestamp timestamp default null
);
create table opensso_services(
  service_uuid uuid primary key not null default uuid_generate_v4(),
  service_name text,
  username text,
  hashed_password text,
  create_timestamp timestamp default now(),
  pre_shared_key text
);
create table opensso_user_service_relation(
  relation_uuid uuid primary key not null default uuid_generate_v4(),
  user_uuid uuid not null,
  service_uuid uuid not null,
  foreign key (user_uuid) references opensso_user(user_uuid),
  foreign key (service_uuid) references opensso_services(service_uuid),
  create_timestamp timestamp default now(),
  delete_timestamp timestamp default null
);
