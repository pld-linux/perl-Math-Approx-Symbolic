#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Approx-Symbolic
Summary:	Math::Approx::Symbolic - symbolic representation of interpolated polynomials
Summary(pl):	Math::Approx::Symbolic - symboliczna reprezentacja interpolowanych wielomian�w
Name:		perl-Math-Approx-Symbolic
Version:	0.100
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9af92c005543fd4da89d88bd5a012ec
BuildRequires:	perl-Math-Approx >= 0.200
BuildRequires:	perl-Math-Symbolic >= 0.123
%if %{with_tests}
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a thin wrapper around the Math::Approx module. It
subclasses Math::Approx and adds the "symbolic" subroutine that return
a Math::Symbolic object representing the calculated approximation.

%description -l pl
Ten modu� to niewielki wrapper do modu�u Math::Approx. Jest podklas�
Math::Approx i dodaje funkcj� "symbolic", zwracaj�c� obiekt
Math::Symbolic reprezentuj�cy obliczon� aproksymacj�.

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
%{perl_vendorlib}/Math/Approx/Symbolic.pm
%{_mandir}/man3/*
