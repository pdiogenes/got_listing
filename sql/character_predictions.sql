create table character_predictions(
    S_No int not null,
    actual int not null,
    pred int not null,
    alive decimal not null,
    plod int not null,
    name varchar not null,
    title varchar,
    male int not null,
    culture varchar,
    dateOfBirth int,
    DateoFdeath int,
    mother varchar,
    father varchar,
    heir varchar,
    house varchar,
    spouse varchar,
    book1 int not null,
    book2 int not null,
    book3 int not null,
    book4 int not null,
    book5 int not null,
    isAliveMother int,
    isAliveFather int,
    isAliveHeir int,
    isAliveSpouse int,
    isMarried int not null,
    isNoble int not null,
    age int,
    numDeadRelations int not null,
    boolDeadRelations int not null,
    isPopular int not null,
    popularity decimal not null,
    isAlive int not null,
    primary key (S_No)
);