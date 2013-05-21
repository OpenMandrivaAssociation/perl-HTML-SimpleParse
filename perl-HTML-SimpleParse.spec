%define upstream_name    HTML-SimpleParse
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	HTML::SimpleParse Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
HTML::SimpleParse module for Perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/HTML/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-4mdv2012.0
+ Revision: 765305
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-3
+ Revision: 763846
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-2
+ Revision: 667195
- mass rebuild

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 407760
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.12-7mdv2009.0
+ Revision: 223789
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.12-6mdv2008.1
+ Revision: 180407
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.12-5mdv2008.0
+ Revision: 64785
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.12-4mdv2008.0
+ Revision: 23392
- rebuild


* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-3mdk
- Rebuild; spec cleanup

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.12-2mdk
- rebuild for new perl
- drop Prefix tag
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Mon Jul 21 2003 François Pons <fpons@mandrakesoft.com> 0.12-1mdk
- 0.12.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.11-2mdk
- rebuild for new auto{prov,req}

