
%define realname   Language-Befunge-Vector-XS
%define version    1.0.0
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Language::Befunge::Vector rewritten for speed
Source:     http://www.cpan.org/modules/by-module/Language/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)



%description
The C<Language::Befunge> module makes heavy use of n-dims vectors,
mapped to the C<Language::Befunge::Vector> class. This allows to
abstract the funge dimension while still keeping the same code for the
operations.

However, such an heavy usage does have some impact on the performances.
Therefore, this modules is basically a rewrite of LBV in XS. If
installed, then LBV will automagically load it and replace its own
functions with the XS ones.



%prep
%setup -q -n %{realname}-%{version} 

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



