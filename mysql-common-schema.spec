Summary:	DBA's framework for MySQL
Name:		mysql-common-schema
Version:	2.2
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	https://common-schema.googlecode.com/files/common_schema-%{version}.sql
# Source0-md5:	6abb41fddafd5f2e9ae1aafe8446208b
Source1:	https://common-schema.googlecode.com/files/common_schema_doc_%{version}.tar.gz
# Source1-md5:	c11ff2f438b0dd3c004f481926a04084
URL:		https://code.google.com/p/common-schema/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
common_schema is a framework for MySQL server administration.

common_schema provides with:
- A function library (text functions, security routines, execution and
  flow control, more...)
- A set of informational and analysis views (security, schema design,
  processes, transactions, more...)
- QueryScript interpreter, allowing for server side scripting.
- rdebug: a debugger and debugging API for MySQL stored routines
  (alpha)

It introduces SQL based tools which simplify otherwise complex shell
and client scripts, allowing the DBA to be independent of operating
system, installed packages and dependencies.

It is a self contained schema, compatible with all MySQL >= 5.1
servers.

This version supports MySQL 5.1, 5.5, 5.6, Percona Server, MariaDB,
with/without InnoDB plugin, TokuDB.

%package doc
Summary:	Manual for common_schema
Summary(fr.UTF-8):	Documentation pour common_schema
Summary(it.UTF-8):	Documentazione di common_schema
Summary(pl.UTF-8):	Podręcznik dla common_schema
Group:		Documentation

%description doc
Documentation for common_schema.

%prep
%setup -qcT -a1
set -- *
install -d doc
mv "$@" doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/common-schema
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/common-schema/common_schema.sql

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/common-schema

%files doc
%defattr(644,root,root,755)
%doc doc/*
