%define upstream_name    Language-Befunge-Vector-XS
%define upstream_version 1.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
