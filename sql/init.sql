drop schema public cascade;
create schema public;

create table Course
(
    year int not null primary key check ( year > 0 )
);

create table Student
(
    id     serial primary key,
    name   text not null,
    course int references Course
);

create table Class
(
    id          serial primary key,
    name        text not null,
    description text not null,
    course      int references Course
);

create table MarkFormulaUnit
(
    id          serial primary key,
    name        text  not null,
    coefficient float not null,
    lesson      int references Class
);

create table Unit
(
    id              serial primary key,
    name            text  not null,
    coefficient     float not null,
    markFormulaUnit int references MarkFormulaUnit
);

create table Mark
(
    student int references Student,
    unit    int references Unit,
    mark    int not null check ( 0 <= mark and mark <= 10 ),
    primary key (student, unit)
);

create table LessonVisiting
(
    student int references Student,
    lesson  int references Class,
    primary key (student, lesson)
);
