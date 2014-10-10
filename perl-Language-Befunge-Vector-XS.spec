%define upstream_name    Language-Befunge-Vector-XS
%define upstream_version 1.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Language::Befunge::Vector rewritten for speed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
The Language::Befunge module makes heavy use of n-dims vectors,
mapped to the Language::Befunge::Vector class. This allows to
abstract the funge dimension while still keeping the same code for the
operations.

However, such an heavy usage does have some impact on the performances.
Therefore, this modules is basically a rewrite of LBV in XS. If
installed, then LBV will automagically load it and replace its own
functions with the XS ones.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.1-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 555982
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 552379
- update to 1.1.1

* Fri Aug 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-3mdv2010.0
+ Revision: 418942
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-2mdv2009.0
+ Revision: 268537
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2009.0
+ Revision: 217097
- update to new version 1.1.0

* Sun Feb 10 2008 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-2mdv2008.1
+ Revision: 164786
- cleaning description (removing pod markers)

* Thu Feb 07 2008 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 163584
- import perl-Language-Befunge-Vector-XS


