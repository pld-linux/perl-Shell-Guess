#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Shell
%define		pnam	Guess
Summary:	Shell::Guess - make an educated guess about the shell in use
Summary(pl.UTF-8):	Shell::Guess - wyuczone zgadywanie używanej powłoki
Name:		perl-Shell-Guess
Version:	0.09
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Shell/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	030d92331738579c147782b2932b1015
URL:		https://metacpan.org/release/Shell-Guess
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.94
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shell::Guess makes a reasonably aggressive attempt to determine the
shell being employed by the user, either the shell that executed the
perl script directly (the "running" shell), or the users' login shell
(the "login" shell). It does this by a variety of means available to
it, depending on the platform that it is running on.

%description -l pl.UTF-8
Shell::Guess wykonuje umiarkowanie agresywną próbę określenia powłoki,
której używa użytkownik - albo powłoki wywoływanej bezpośrednio przez
skrypt perlowy (działającej powłoki), albo powłoki logowania
użytkownika. Robi to na wiele różnych sposobów, w zależności od
platformy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Shell/Guess.pm
%{_mandir}/man3/Shell::Guess.3pm*
