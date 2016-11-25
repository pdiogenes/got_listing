create table character_deaths(
	id serial not null,
	name varchar(255) not null,
	allegiances varchar(255) null,
	death_year int null,
	book_of_death int null,
	death_chapter int null,
	book_intro_chapter int null,
	gender  boolean null,
	nobility boolean null,
	got boolean null,
	cok boolean null,
	sos boolean null,
	ffc boolean null,
	dwd boolean null,
	primary key (id)
);