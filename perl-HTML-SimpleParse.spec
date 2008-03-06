%define real_name HTML-SimpleParse
%define name perl-%real_name
%define version 0.12
%define release %mkrel 6

Summary: HTML::SimpleParse Perl module
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL or Artistic
Group: Development/Perl
Source0: %{real_name}-%{version}.tar.bz2
Url: http://search.cpan.org/dist/%real_name/
Requires: perl
BuildRequires: perl-devel
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-root

%description
HTML::SimpleParse module for Perl

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTML/*
%{_mandir}/*/*

