#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Approx-Symbolic
%include	/usr/lib/rpm/macros.perl
Summary:	Math::Approx::Symbolic - symbolic representation of interpolated polynomials
Summary(pl.UTF-8):	Math::Approx::Symbolic - symboliczna reprezentacja interpolowanych wielomianów
Name:		perl-Math-Approx-Symbolic
Version:	0.100
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9af92c005543fd4da89d88bd5a012ec
URL:		http://search.cpan.org/dist/Math-Approx-Symbolic/
BuildRequires:	perl-Math-Approx >= 0.200
BuildRequires:	perl-Math-Symbolic >= 0.123
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a thin wrapper around the Math::Approx module. It
subclasses Math::Approx and adds the "symbolic" subroutine that return
a Math::Symbolic object representing the calculated approximation.

%description -l pl.UTF-8
Ten moduł to niewielki wrapper do modułu Math::Approx. Jest podklasą
Math::Approx i dodaje funkcję "symbolic", zwracającą obiekt
Math::Symbolic reprezentujący obliczoną aproksymację.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Approx
%{perl_vendorlib}/Math/Approx/Symbolic.pm
%{_mandir}/man3/*
