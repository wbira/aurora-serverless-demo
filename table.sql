create table credit_card
(
  reservation_id_prefix bigint       not null  primary key,
  card_number           varchar(64)  not null,
  card_type             varchar(32)  not null,
  token_url             varchar(255) not null,
  status                varchar(32)  not null,
  attempts              int          not null,
);

